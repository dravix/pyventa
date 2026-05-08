-- =============================================================================
-- pyventa — MySQL 8.0+ schema (redesigned)
-- Generated: 2026-05-07
--
-- Changes from original (db.sql):
--   • Engine: MyISAM → InnoDB (transactions, FK enforcement)
--   • Charset: latin1 → utf8mb4 / utf8mb4_unicode_ci (full Spanish + emoji)
--   • All table/column names translated Spanish → English (see mapping in README)
--   • Integer display widths removed (deprecated in MySQL 8.0.17)
--   • FLOAT/DOUBLE monetary columns → DECIMAL(12,2) (exact arithmetic)
--   • Proper FOREIGN KEY constraints with ON DELETE / ON UPDATE policies
--   • created_at / updated_at audit columns on every mutable table
--   • ventas (daily summary): was keyed on date (one row/day max) → redesigned
--     with auto-increment PK and a UNIQUE date index
--   • proveedores table added (was missing; original reused clientes with tipo=1)
--   • usuarios.password_hash widened to VARCHAR(72) for bcrypt
--   • compras.status column added (present in alterlog v3.2 but missing in db.sql)
--   • All seed data preserved (column names translated)
-- =============================================================================

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;
SET SQL_MODE = 'STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------------------------------
-- Drop all tables in reverse dependency order
-- -----------------------------------------------------------------------------
DROP TABLE IF EXISTS `sale_items`;
DROP TABLE IF EXISTS `collected_sales`;
DROP TABLE IF EXISTS `sales`;
DROP TABLE IF EXISTS `daily_sales_summary`;
DROP TABLE IF EXISTS `cash_movements`;
DROP TABLE IF EXISTS `expenses`;
DROP TABLE IF EXISTS `purchase_items`;
DROP TABLE IF EXISTS `purchases`;
DROP TABLE IF EXISTS `inventory_counts`;
DROP TABLE IF EXISTS `inventory_audits`;
DROP TABLE IF EXISTS `shortages`;
DROP TABLE IF EXISTS `promotion_items`;
DROP TABLE IF EXISTS `promotions`;
DROP TABLE IF EXISTS `product_components`;
DROP TABLE IF EXISTS `barcodes`;
DROP TABLE IF EXISTS `products`;
DROP TABLE IF EXISTS `product_families`;
DROP TABLE IF EXISTS `departments`;
DROP TABLE IF EXISTS `units`;
DROP TABLE IF EXISTS `taxes`;
DROP TABLE IF EXISTS `registers`;
DROP TABLE IF EXISTS `customers`;
DROP TABLE IF EXISTS `suppliers`;
DROP TABLE IF EXISTS `users`;
DROP TABLE IF EXISTS `saved_queries`;

-- -----------------------------------------------------------------------------
-- users
-- Widened password_hash to VARCHAR(72) to hold bcrypt hashes (60 chars).
-- access_level: 1=cashier, 2=inventory, 3=purchases, 4=supervisor, 5=admin
-- -----------------------------------------------------------------------------
CREATE TABLE `users` (
    `user_id`       INT            NOT NULL AUTO_INCREMENT,
    `full_name`     VARCHAR(100)   NOT NULL,
    `username`      VARCHAR(50)    NOT NULL,
    `password_hash` VARCHAR(72)    NOT NULL,  -- bcrypt output is ≤72 chars
    `access_level`  TINYINT        NOT NULL DEFAULT 1,
    `created_at`    TIMESTAMP      NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `updated_at`    TIMESTAMP      NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`user_id`),
    UNIQUE KEY `uq_users_username` (`username`),
    KEY `idx_users_access_level` (`access_level`)
) ENGINE=InnoDB
  DEFAULT CHARSET=utf8mb4
  COLLATE=utf8mb4_unicode_ci;

-- Seed data: passwords are MD5 hashes from the original (to be migrated to bcrypt on first login)
INSERT INTO `users` (`user_id`, `full_name`, `username`, `password_hash`, `access_level`) VALUES
    (1, 'Usuario',       'user',  'd41d8cd98f00b204e9800998ecf8427e', 1),
    (2, 'Administrador', 'admin', '1ddff545424249df81f3c4ab552dbb3d', 5);

-- -----------------------------------------------------------------------------
-- registers (cajas)
-- opened_date: the date the register was opened/initialized (not a status enum).
-- cash_amount: current cash on hand (updated after each sale/movement).
-- -----------------------------------------------------------------------------
CREATE TABLE `registers` (
    `register_id`       INT             NOT NULL AUTO_INCREMENT,
    `name`              VARCHAR(45)     NOT NULL,
    `hostname`          VARCHAR(15)     NULL DEFAULT NULL,   -- machine name / IP
    `opening_balance`   DECIMAL(12,2)   NOT NULL DEFAULT 0.00,
    `opened_date`       DATE            NOT NULL,
    `cash_amount`       DECIMAL(12,2)   NOT NULL DEFAULT 0.00,
    `created_at`        TIMESTAMP       NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `updated_at`        TIMESTAMP       NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`register_id`)
) ENGINE=InnoDB
  DEFAULT CHARSET=utf8mb4
  COLLATE=utf8mb4_unicode_ci;

INSERT INTO `registers` (`register_id`, `name`, `hostname`, `opening_balance`, `opened_date`, `cash_amount`) VALUES
    (1, 'Caja 1', 'localhost', 0.00, '2000-01-01', 0.00);

-- -----------------------------------------------------------------------------
-- customers (clientes)
-- Original design stored both customers (tipo=0) and suppliers (tipo=1) in this
-- table. Suppliers are now a separate table. tipo values: 0=walk-in, 1=regular,
-- 2=wholesale. tax_id (RFC) can be '-' for anonymous walk-in customer.
-- -----------------------------------------------------------------------------
CREATE TABLE `customers` (
    `customer_id`   INT             NOT NULL AUTO_INCREMENT,
    `full_name`     VARCHAR(150)    NOT NULL,
    `tax_id`        VARCHAR(15)     NOT NULL DEFAULT '-',    -- RFC (Mexican tax ID)
    `address`       VARCHAR(100)    NOT NULL DEFAULT '-',
    `city`          VARCHAR(100)    NOT NULL DEFAULT '-',
    `state`         VARCHAR(100)    NOT NULL DEFAULT '-',
    `phone`         VARCHAR(20)     NOT NULL DEFAULT '',
    `email`         VARCHAR(100)    NOT NULL DEFAULT '',
    `type`          TINYINT         NOT NULL DEFAULT 0,      -- 0=walk-in, 1=regular, 2=wholesale
    `credit_limit`  DECIMAL(12,2)   NOT NULL DEFAULT 0.00,
    `created_at`    TIMESTAMP       NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `updated_at`    TIMESTAMP       NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`customer_id`),
    UNIQUE KEY `uq_customers_tax_id` (`tax_id`),
    KEY `idx_customers_type` (`type`)
) ENGINE=InnoDB
  DEFAULT CHARSET=utf8mb4
  COLLATE=utf8mb4_unicode_ci;

INSERT INTO `customers` (`customer_id`, `full_name`, `tax_id`, `address`, `city`, `state`, `phone`, `email`, `type`, `credit_limit`) VALUES
    (1, 'Cliente mostrador', '-', '-', '-', '-', '(000)-000-00-00', '', 0, 0.00);

-- -----------------------------------------------------------------------------
-- suppliers (proveedores)
-- New table. Original app stored suppliers in clientes with tipo=1.
-- Mirrors the same contact structure so the Python Admin1 widget reuse works.
-- -----------------------------------------------------------------------------
CREATE TABLE `suppliers` (
    `supplier_id`   INT             NOT NULL AUTO_INCREMENT,
    `full_name`     VARCHAR(150)    NOT NULL,
    `tax_id`        VARCHAR(15)     NOT NULL DEFAULT '-',    -- RFC
    `address`       VARCHAR(100)    NOT NULL DEFAULT '-',
    `city`          VARCHAR(100)    NOT NULL DEFAULT '-',
    `state`         VARCHAR(100)    NOT NULL DEFAULT '-',
    `phone`         VARCHAR(20)     NOT NULL DEFAULT '',
    `email`         VARCHAR(100)    NOT NULL DEFAULT '',
    `type`          TINYINT         NOT NULL DEFAULT 0,      -- supplier category (0-2)
    `credit_limit`  DECIMAL(12,2)   NOT NULL DEFAULT 0.00,  -- credit extended by supplier
    `created_at`    TIMESTAMP       NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `updated_at`    TIMESTAMP       NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`supplier_id`),
    UNIQUE KEY `uq_suppliers_tax_id` (`tax_id`)
) ENGINE=InnoDB
  DEFAULT CHARSET=utf8mb4
  COLLATE=utf8mb4_unicode_ci;

-- -----------------------------------------------------------------------------
-- departments (departamentos)
-- Top-level product category.
-- -----------------------------------------------------------------------------
CREATE TABLE `departments` (
    `department_id` INT             NOT NULL AUTO_INCREMENT,
    `name`          VARCHAR(100)    NOT NULL,
    `created_at`    TIMESTAMP       NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `updated_at`    TIMESTAMP       NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`department_id`),
    UNIQUE KEY `uq_departments_name` (`name`)
) ENGINE=InnoDB
  DEFAULT CHARSET=utf8mb4
  COLLATE=utf8mb4_unicode_ci;

INSERT INTO `departments` (`department_id`, `name`) VALUES (1, 'NINGUNO');

-- -----------------------------------------------------------------------------
-- product_families (familias)
-- Sub-category belonging to a department.
-- -----------------------------------------------------------------------------
CREATE TABLE `product_families` (
    `family_id`     INT             NOT NULL AUTO_INCREMENT,
    `name`          VARCHAR(100)    NOT NULL,
    `department_id` INT             NOT NULL DEFAULT 1,
    `created_at`    TIMESTAMP       NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `updated_at`    TIMESTAMP       NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`family_id`),
    KEY `idx_product_families_department_id` (`department_id`),
    CONSTRAINT `fk_families_department`
        FOREIGN KEY (`department_id`) REFERENCES `departments` (`department_id`)
        ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB
  DEFAULT CHARSET=utf8mb4
  COLLATE=utf8mb4_unicode_ci;

INSERT INTO `product_families` (`family_id`, `name`, `department_id`) VALUES (1, 'NINGUNA', 1);

-- -----------------------------------------------------------------------------
-- units (unidades)
-- Unit of measure: PZA, KG, LT, MT, etc.
-- -----------------------------------------------------------------------------
CREATE TABLE `units` (
    `unit_id`       INT             NOT NULL AUTO_INCREMENT,
    `name`          VARCHAR(20)     NOT NULL,
    `created_at`    TIMESTAMP       NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `updated_at`    TIMESTAMP       NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`unit_id`),
    UNIQUE KEY `uq_units_name` (`name`)
) ENGINE=InnoDB
  DEFAULT CHARSET=utf8mb4
  COLLATE=utf8mb4_unicode_ci;

INSERT INTO `units` (`unit_id`, `name`) VALUES (1, 'PZA');

-- -----------------------------------------------------------------------------
-- taxes (impuestos)
-- Tax rates. IVA=16% is standard Mexican VAT (may change, so stored as data).
-- -----------------------------------------------------------------------------
CREATE TABLE `taxes` (
    `tax_id`        INT             NOT NULL AUTO_INCREMENT,
    `name`          VARCHAR(100)    NOT NULL,
    `rate`          DECIMAL(6,4)    NOT NULL,   -- e.g. 0.1600 for 16%
    `created_at`    TIMESTAMP       NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `updated_at`    TIMESTAMP       NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`tax_id`)
) ENGINE=InnoDB
  DEFAULT CHARSET=utf8mb4
  COLLATE=utf8mb4_unicode_ci;

-- Original stored 16 (integer percent). Stored as 0.1600 (factor) for cleaner math.
INSERT INTO `taxes` (`tax_id`, `name`, `rate`) VALUES (1, 'I.V.A', 0.1600);

-- -----------------------------------------------------------------------------
-- products (productos)
-- primary_barcode: the main barcode (stored as BIGINT to handle EAN-13/UPC-A).
-- product_id (ref): internal auto-increment surrogate key.
-- total_sold: denormalised lifetime counter (updated on each sale). Kept for
--   quick reporting; accurate totals can always be recalculated from sale_items.
-- markup: margin percentage (ganancia), e.g. 20.00 = 20%.
-- -----------------------------------------------------------------------------
CREATE TABLE `products` (
    `product_id`        INT             NOT NULL AUTO_INCREMENT,
    `primary_barcode`   BIGINT          NOT NULL DEFAULT 0,
    `description`       VARCHAR(100)    NOT NULL,
    `family_id`         INT             NOT NULL DEFAULT 1,
    `unit_cost`         DECIMAL(12,4)   NOT NULL DEFAULT 0.0000,  -- 4 decimals for fractional-unit costs
    `markup`            DECIMAL(8,4)    NOT NULL DEFAULT 0.0000,  -- percentage e.g. 20.0000
    `price`             DECIMAL(12,4)   NOT NULL DEFAULT 0.0000,
    `stock`             DECIMAL(12,4)   NOT NULL DEFAULT 0.0000,  -- kept for legacy; authoritative = inventory_counts
    `unit_id`           INT             NOT NULL DEFAULT 1,
    `total_sold`        DECIMAL(12,4)   NOT NULL DEFAULT 0.0000,
    `tax_id`            INT             NOT NULL DEFAULT 1,
    `created_at`        TIMESTAMP       NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `updated_at`        TIMESTAMP       NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`product_id`),
    KEY `idx_products_primary_barcode` (`primary_barcode`),
    KEY `idx_products_family_id` (`family_id`),
    KEY `idx_products_unit_id` (`unit_id`),
    KEY `idx_products_tax_id` (`tax_id`),
    KEY `idx_products_description` (`description`),
    CONSTRAINT `fk_products_family`
        FOREIGN KEY (`family_id`) REFERENCES `product_families` (`family_id`)
        ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT `fk_products_unit`
        FOREIGN KEY (`unit_id`) REFERENCES `units` (`unit_id`)
        ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT `fk_products_tax`
        FOREIGN KEY (`tax_id`) REFERENCES `taxes` (`tax_id`)
        ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB
  DEFAULT CHARSET=utf8mb4
  COLLATE=utf8mb4_unicode_ci;

-- -----------------------------------------------------------------------------
-- barcodes (codigos)
-- One product can have multiple barcode aliases (e.g., box barcode, unit barcode).
-- -----------------------------------------------------------------------------
CREATE TABLE `barcodes` (
    `product_id`    INT             NOT NULL,
    `barcode`       VARCHAR(25)     NOT NULL,
    `created_at`    TIMESTAMP       NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (`product_id`, `barcode`),
    KEY `idx_barcodes_barcode` (`barcode`),      -- for fast barcode lookups
    CONSTRAINT `fk_barcodes_product`
        FOREIGN KEY (`product_id`) REFERENCES `products` (`product_id`)
        ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB
  DEFAULT CHARSET=utf8mb4
  COLLATE=utf8mb4_unicode_ci;

-- -----------------------------------------------------------------------------
-- product_components (subproductos)
-- Represents bundle / kit relationships.
-- component_product_id: the component (child) product
-- product_id: the bundle (parent) product that contains this component
-- quantity: how many units of the component are in one bundle
-- -----------------------------------------------------------------------------
CREATE TABLE `product_components` (
    `component_product_id`  INT             NOT NULL,
    `product_id`            INT             NOT NULL,
    `quantity`              DECIMAL(12,4)   NOT NULL DEFAULT 1.0000,
    `created_at`            TIMESTAMP       NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `updated_at`            TIMESTAMP       NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    -- Original had component_product_id as sole PK (one component belongs to one bundle)
    PRIMARY KEY (`component_product_id`),
    KEY `idx_product_components_product_id` (`product_id`),
    CONSTRAINT `fk_components_component`
        FOREIGN KEY (`component_product_id`) REFERENCES `products` (`product_id`)
        ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT `fk_components_bundle`
        FOREIGN KEY (`product_id`) REFERENCES `products` (`product_id`)
        ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB
  DEFAULT CHARSET=utf8mb4
  COLLATE=utf8mb4_unicode_ci;

-- -----------------------------------------------------------------------------
-- promotions (promociones)
-- Discount promotions active during a date range.
-- discount_rate: percentage e.g. 10.00 = 10% off.
-- min_quantity / max_quantity: the promotion applies when quantity is in this range.
-- -----------------------------------------------------------------------------
CREATE TABLE `promotions` (
    `promotion_id`  INT             NOT NULL AUTO_INCREMENT,
    `name`          VARCHAR(50)     NOT NULL,
    `discount_rate` DECIMAL(6,4)    NOT NULL,   -- e.g. 0.1000 = 10%
    `start_date`    DATE            NOT NULL,
    `end_date`      DATE            NOT NULL,
    `min_quantity`  DECIMAL(12,4)   NOT NULL DEFAULT 0.0000,
    `max_quantity`  DECIMAL(12,4)   NOT NULL DEFAULT 0.0000,
    `created_at`    TIMESTAMP       NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `updated_at`    TIMESTAMP       NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`promotion_id`),
    KEY `idx_promotions_dates` (`start_date`, `end_date`)   -- range queries: WHERE CURDATE() BETWEEN start_date AND end_date
) ENGINE=InnoDB
  DEFAULT CHARSET=utf8mb4
  COLLATE=utf8mb4_unicode_ci;

-- -----------------------------------------------------------------------------
-- promotion_items (ofertas)
-- Maps a promotion to a product / family / department (polymorphic reference).
-- item_type: 0=product (product_group_id → products.product_id),
--            1=family  (product_group_id → product_families.family_id),
--            2=department (product_group_id → departments.department_id)
-- No FK on product_group_id because the target table depends on item_type.
-- -----------------------------------------------------------------------------
CREATE TABLE `promotion_items` (
    `promotion_id`      INT         NOT NULL,
    `product_group_id`  INT         NOT NULL,
    `item_type`         TINYINT     NOT NULL,   -- 0=product, 1=family, 2=department
    `created_at`        TIMESTAMP   NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (`promotion_id`, `product_group_id`, `item_type`),
    KEY `idx_promotion_items_promotion_id` (`promotion_id`),
    CONSTRAINT `fk_promotion_items_promotion`
        FOREIGN KEY (`promotion_id`) REFERENCES `promotions` (`promotion_id`)
        ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB
  DEFAULT CHARSET=utf8mb4
  COLLATE=utf8mb4_unicode_ci;

-- -----------------------------------------------------------------------------
-- inventory_audits (inventarios)
-- Each row represents one full inventory-count session.
-- status: 0=in progress, 1=completed, 2=cancelled
-- audit_id=0 is reserved for live/current inventory tracking (not a real audit).
-- -----------------------------------------------------------------------------
CREATE TABLE `inventory_audits` (
    `audit_id`          INT             NOT NULL AUTO_INCREMENT,
    `created_at`        TIMESTAMP       NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `balance`           DECIMAL(12,2)   NOT NULL DEFAULT 0.00,
    `scope`             VARCHAR(120)    NULL DEFAULT NULL,
    `order_number`      VARCHAR(20)     NULL DEFAULT NULL,
    `status`            TINYINT         NOT NULL DEFAULT 0,  -- 0=open, 1=closed, 2=cancelled
    `auditor_user_id`   INT             NOT NULL,
    `manager_user_id`   INT             NOT NULL,
    `updated_at`        TIMESTAMP       NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`audit_id`),
    KEY `idx_inventory_audits_auditor` (`auditor_user_id`),
    KEY `idx_inventory_audits_manager` (`manager_user_id`),
    CONSTRAINT `fk_audits_auditor`
        FOREIGN KEY (`auditor_user_id`) REFERENCES `users` (`user_id`)
        ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT `fk_audits_manager`
        FOREIGN KEY (`manager_user_id`) REFERENCES `users` (`user_id`)
        ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB
  DEFAULT CHARSET=utf8mb4
  COLLATE=utf8mb4_unicode_ci;

-- -----------------------------------------------------------------------------
-- inventory_counts (existencia)
-- Per-product count within an audit session.
-- audit_id=0 is the "live" row updated in real-time (logical stock tracking).
-- The composite PK (product_id, audit_id) means each product has exactly one
-- live row (audit_id=0) and one row per formal audit.
-- discrepancy = physical_stock - logical_stock (NULL until physical count done)
-- -----------------------------------------------------------------------------
CREATE TABLE `inventory_counts` (
    `product_id`        INT             NOT NULL,
    `audit_id`          INT             NOT NULL DEFAULT 0,  -- 0 = live tracking row
    `physical_stock`    DECIMAL(12,4)   NOT NULL DEFAULT 0.0000,
    `logical_stock`     DECIMAL(12,4)   NOT NULL DEFAULT 0.0000,
    `discrepancy`       DECIMAL(12,4)   NULL DEFAULT NULL,
    PRIMARY KEY (`product_id`, `audit_id`),
    KEY `idx_inventory_counts_product_id` (`product_id`),
    -- Note: audit_id=0 is NOT a FK to inventory_audits (it's the live-tracking sentinel)
    CONSTRAINT `fk_inv_counts_product`
        FOREIGN KEY (`product_id`) REFERENCES `products` (`product_id`)
        ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB
  DEFAULT CHARSET=utf8mb4
  COLLATE=utf8mb4_unicode_ci;

-- -----------------------------------------------------------------------------
-- shortages (faltantes)
-- Tracks products flagged as out-of-stock / needing reorder.
-- One row per product (product_id is PK) — a product can only have one active
-- shortage request at a time, matching original design intent.
-- -----------------------------------------------------------------------------
CREATE TABLE `shortages` (
    `product_id`    INT             NOT NULL,
    `user_id`       INT             NOT NULL,
    `quantity`      DECIMAL(12,4)   NOT NULL DEFAULT 0.0000,
    `priority`      TINYINT         NOT NULL DEFAULT 0,
    `created_at`    DATE            NOT NULL DEFAULT (CURRENT_DATE),
    `updated_at`    TIMESTAMP       NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`product_id`),
    KEY `idx_shortages_user_id` (`user_id`),
    CONSTRAINT `fk_shortages_product`
        FOREIGN KEY (`product_id`) REFERENCES `products` (`product_id`)
        ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT `fk_shortages_user`
        FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`)
        ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB
  DEFAULT CHARSET=utf8mb4
  COLLATE=utf8mb4_unicode_ci;

-- -----------------------------------------------------------------------------
-- purchases (compras)
-- Purchase orders from suppliers.
-- status: added from alterlog v3.2 (was missing in db.sql). 0=draft, 1=received, 2=cancelled
-- -----------------------------------------------------------------------------
CREATE TABLE `purchases` (
    `purchase_id`   INT             NOT NULL AUTO_INCREMENT,
    `supplier_id`   INT             NOT NULL,
    `buyer_user_id` INT             NOT NULL,
    `total_amount`  DECIMAL(12,2)   NOT NULL DEFAULT 0.00,
    `status`        TINYINT         NOT NULL DEFAULT 0,  -- 0=draft, 1=received, 2=cancelled
    `created_at`    TIMESTAMP       NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `updated_at`    TIMESTAMP       NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`purchase_id`),
    KEY `idx_purchases_supplier_id` (`supplier_id`),
    KEY `idx_purchases_buyer_user_id` (`buyer_user_id`),
    KEY `idx_purchases_created_at` (`created_at`),
    CONSTRAINT `fk_purchases_supplier`
        FOREIGN KEY (`supplier_id`) REFERENCES `suppliers` (`supplier_id`)
        ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT `fk_purchases_buyer`
        FOREIGN KEY (`buyer_user_id`) REFERENCES `users` (`user_id`)
        ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB
  DEFAULT CHARSET=utf8mb4
  COLLATE=utf8mb4_unicode_ci;

-- -----------------------------------------------------------------------------
-- purchase_items (comprados)
-- Line items within a purchase order.
-- unit_cost: the cost per unit AT TIME OF PURCHASE (historical snapshot).
-- total_amount: quantity × unit_cost (denormalised for fast reporting).
-- -----------------------------------------------------------------------------
CREATE TABLE `purchase_items` (
    `purchase_id`   INT             NOT NULL,
    `product_id`    INT             NOT NULL,
    `quantity`      DECIMAL(12,4)   NOT NULL,
    `unit_cost`     DECIMAL(12,4)   NOT NULL,
    `total_amount`  DECIMAL(12,2)   NOT NULL,
    `created_at`    TIMESTAMP       NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (`purchase_id`, `product_id`),
    KEY `idx_purchase_items_product_id` (`product_id`),
    CONSTRAINT `fk_purchase_items_purchase`
        FOREIGN KEY (`purchase_id`) REFERENCES `purchases` (`purchase_id`)
        ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT `fk_purchase_items_product`
        FOREIGN KEY (`product_id`) REFERENCES `products` (`product_id`)
        ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB
  DEFAULT CHARSET=utf8mb4
  COLLATE=utf8mb4_unicode_ci;

-- -----------------------------------------------------------------------------
-- sales (notas)
-- Sale headers (receipts / invoices / returns).
-- sale_type: 0=receipt (nota), 1=invoice (factura), 2=return (devolución)
-- payment_status: 0=unpaid, 1=paid, 2=on credit, 3=returned
-- -----------------------------------------------------------------------------
CREATE TABLE `sales` (
    `sale_id`           INT             NOT NULL AUTO_INCREMENT,
    `customer_id`       INT             NOT NULL DEFAULT 1,  -- 1=walk-in customer
    `user_id`           INT             NOT NULL,
    `register_id`       INT             NOT NULL,
    `subtotal`          DECIMAL(12,2)   NOT NULL DEFAULT 0.00,
    `discounts`         DECIMAL(12,2)   NOT NULL DEFAULT 0.00,
    `total_amount`      DECIMAL(12,2)   NOT NULL DEFAULT 0.00,
    `sale_type`         TINYINT         NOT NULL DEFAULT 0,  -- 0=receipt, 1=invoice, 2=return
    `payment_status`    TINYINT         NOT NULL DEFAULT 0,  -- 0=unpaid, 1=paid, 2=credit, 3=returned
    `created_at`        TIMESTAMP       NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `updated_at`        TIMESTAMP       NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`sale_id`),
    KEY `idx_sales_customer_id` (`customer_id`),
    KEY `idx_sales_user_id` (`user_id`),
    KEY `idx_sales_register_id` (`register_id`),
    KEY `idx_sales_created_at` (`created_at`),
    KEY `idx_sales_payment_status` (`payment_status`),
    CONSTRAINT `fk_sales_customer`
        FOREIGN KEY (`customer_id`) REFERENCES `customers` (`customer_id`)
        ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT `fk_sales_user`
        FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`)
        ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT `fk_sales_register`
        FOREIGN KEY (`register_id`) REFERENCES `registers` (`register_id`)
        ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB
  DEFAULT CHARSET=utf8mb4
  COLLATE=utf8mb4_unicode_ci;

-- -----------------------------------------------------------------------------
-- sale_items (vendidos)
-- Line items within a sale.
-- line_type: flag from original (purpose unclear from source; preserved as-is)
-- unit_price: price per unit at time of sale (historical snapshot).
-- total_amount: quantity × unit_price after discounts (denormalised).
-- -----------------------------------------------------------------------------
CREATE TABLE `sale_items` (
    `sale_id`       INT             NOT NULL,
    `product_id`    INT             NOT NULL,
    `line_type`     TINYINT         NOT NULL DEFAULT 0,
    `quantity`      DECIMAL(12,4)   NOT NULL,
    `unit_price`    DECIMAL(12,4)   NOT NULL DEFAULT 0.0000,
    `total_amount`  DECIMAL(12,2)   NOT NULL,
    `created_at`    TIMESTAMP       NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (`sale_id`, `product_id`, `line_type`),
    KEY `idx_sale_items_product_id` (`product_id`),
    CONSTRAINT `fk_sale_items_sale`
        FOREIGN KEY (`sale_id`) REFERENCES `sales` (`sale_id`)
        ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT `fk_sale_items_product`
        FOREIGN KEY (`product_id`) REFERENCES `products` (`product_id`)
        ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB
  DEFAULT CHARSET=utf8mb4
  COLLATE=utf8mb4_unicode_ci;

-- -----------------------------------------------------------------------------
-- collected_sales (notas_cobradas)
-- Tracks which credit sales have been collected (paid off).
-- Separate from payment_status in sales to preserve audit trail.
-- -----------------------------------------------------------------------------
CREATE TABLE `collected_sales` (
    `id`            INT             NOT NULL AUTO_INCREMENT,
    `sale_id`       INT             NOT NULL,
    `collected_at`  TIMESTAMP       NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`),
    UNIQUE KEY `uq_collected_sales_sale_id` (`sale_id`),
    CONSTRAINT `fk_collected_sales_sale`
        FOREIGN KEY (`sale_id`) REFERENCES `sales` (`sale_id`)
        ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB
  DEFAULT CHARSET=utf8mb4
  COLLATE=utf8mb4_unicode_ci;

-- -----------------------------------------------------------------------------
-- daily_sales_summary (ventas)
-- REDESIGNED: original used fecha (DATE) as PK, allowing only one row per day.
-- New design: auto-increment PK + UNIQUE index on summary_date.
-- This table is populated by an end-of-day close procedure.
-- -----------------------------------------------------------------------------
CREATE TABLE `daily_sales_summary` (
    `summary_id`    INT             NOT NULL AUTO_INCREMENT,
    `summary_date`  DATE            NOT NULL,
    `subtotal`      DECIMAL(12,2)   NOT NULL DEFAULT 0.00,
    `discounts`     DECIMAL(12,2)   NOT NULL DEFAULT 0.00,
    `total_amount`  DECIMAL(12,2)   NOT NULL DEFAULT 0.00,
    `cash_amount`   DECIMAL(12,2)   NOT NULL DEFAULT 0.00,
    `created_at`    TIMESTAMP       NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `updated_at`    TIMESTAMP       NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`summary_id`),
    UNIQUE KEY `uq_daily_sales_summary_date` (`summary_date`)  -- one summary per day
) ENGINE=InnoDB
  DEFAULT CHARSET=utf8mb4
  COLLATE=utf8mb4_unicode_ci;

-- -----------------------------------------------------------------------------
-- cash_movements (movimientos)
-- All cash register movements: withdrawals (W), deposits (D), transfers (T).
-- Renamed enum values: R→W (withdrawal/retiro) to be unambiguous in English.
-- -----------------------------------------------------------------------------
CREATE TABLE `cash_movements` (
    `movement_id`   INT             NOT NULL AUTO_INCREMENT,
    `user_id`       INT             NOT NULL,
    `register_id`   INT             NOT NULL,
    `detail`        VARCHAR(100)    NULL DEFAULT NULL,
    `movement_type` ENUM('W','D','T') NOT NULL,  -- W=withdrawal, D=deposit, T=transfer
    `amount`        DECIMAL(12,2)   NOT NULL,
    `created_at`    TIMESTAMP       NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (`movement_id`),
    KEY `idx_cash_movements_user_id` (`user_id`),
    KEY `idx_cash_movements_register_id` (`register_id`),
    KEY `idx_cash_movements_created_at` (`created_at`),
    CONSTRAINT `fk_cash_movements_user`
        FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`)
        ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT `fk_cash_movements_register`
        FOREIGN KEY (`register_id`) REFERENCES `registers` (`register_id`)
        ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB
  DEFAULT CHARSET=utf8mb4
  COLLATE=utf8mb4_unicode_ci;

-- -----------------------------------------------------------------------------
-- expenses (gastos)
-- Cash register expenses / petty cash withdrawals.
-- -----------------------------------------------------------------------------
CREATE TABLE `expenses` (
    `expense_id`    INT             NOT NULL AUTO_INCREMENT,
    `user_id`       INT             NOT NULL,
    `register_id`   INT             NOT NULL,
    `description`   VARCHAR(200)    NOT NULL,
    `amount`        DECIMAL(12,2)   NOT NULL,
    `created_at`    TIMESTAMP       NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `updated_at`    TIMESTAMP       NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`expense_id`),
    KEY `idx_expenses_user_id` (`user_id`),
    KEY `idx_expenses_register_id` (`register_id`),
    KEY `idx_expenses_created_at` (`created_at`),
    CONSTRAINT `fk_expenses_user`
        FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`)
        ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT `fk_expenses_register`
        FOREIGN KEY (`register_id`) REFERENCES `registers` (`register_id`)
        ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB
  DEFAULT CHARSET=utf8mb4
  COLLATE=utf8mb4_unicode_ci;

-- -----------------------------------------------------------------------------
-- saved_queries (consultas)
-- User-defined report queries stored in the database.
-- WARNING: executing arbitrary SQL from this table is a SQL injection risk.
--   The application must validate/sanitise query_text before execution.
-- -----------------------------------------------------------------------------
CREATE TABLE `saved_queries` (
    `query_id`      INT             NOT NULL AUTO_INCREMENT,
    `title`         VARCHAR(100)    NOT NULL,
    `description`   TEXT            NOT NULL,
    `query_text`    TEXT            NOT NULL,
    `created_at`    TIMESTAMP       NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `updated_at`    TIMESTAMP       NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`query_id`)
) ENGINE=InnoDB
  DEFAULT CHARSET=utf8mb4
  COLLATE=utf8mb4_unicode_ci;

-- -----------------------------------------------------------------------------
-- Re-enable FK checks
-- -----------------------------------------------------------------------------
SET FOREIGN_KEY_CHECKS = 1;
