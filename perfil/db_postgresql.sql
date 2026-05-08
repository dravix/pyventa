-- =============================================================================
-- pyventa — PostgreSQL 14+ schema (redesigned)
-- Generated: 2026-05-07
--
-- Usage:
--   psql -U postgres -d pyventa < db_postgresql.sql
--
-- Changes from original (db.sql):
--   • Full translation of table/column names Spanish → English
--   • MyISAM → PostgreSQL native (InnoDB concepts natively supported)
--   • latin1 → UTF-8 (PostgreSQL default; set at cluster or DB level)
--   • FLOAT/DOUBLE monetary → NUMERIC(12,2) / NUMERIC(12,4)
--   • INT AUTO_INCREMENT → GENERATED ALWAYS AS IDENTITY
--   • DATETIME → TIMESTAMPTZ (timezone-aware, correct for multi-timezone POS)
--   • Proper FK constraints with ON DELETE / ON UPDATE
--   • updated_at maintained by trigger function (PostgreSQL has no ON UPDATE)
--   • ENUM types defined as CREATE TYPE
--   • ventas redesigned: auto-increment PK + unique date index
--   • proveedores table added (was missing)
--   • password_hash widened to VARCHAR(72) for bcrypt
--   • BOOLEAN used for binary flags; SMALLINT for multi-value status codes
--   • All seed data preserved
-- =============================================================================

BEGIN;

-- -----------------------------------------------------------------------------
-- Schema
-- -----------------------------------------------------------------------------
CREATE SCHEMA IF NOT EXISTS pyventa;
SET search_path TO pyventa;

-- -----------------------------------------------------------------------------
-- Shared trigger function: auto-update updated_at on any mutable table
-- -----------------------------------------------------------------------------
CREATE OR REPLACE FUNCTION pyventa.set_updated_at()
RETURNS TRIGGER
LANGUAGE plpgsql AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$;

-- Helper macro: attach the trigger to a table
-- Usage: SELECT pyventa.create_updated_at_trigger('table_name');
CREATE OR REPLACE FUNCTION pyventa.create_updated_at_trigger(tbl TEXT)
RETURNS VOID
LANGUAGE plpgsql AS $$
BEGIN
    EXECUTE format(
        'CREATE TRIGGER trg_%I_updated_at
         BEFORE UPDATE ON pyventa.%I
         FOR EACH ROW EXECUTE FUNCTION pyventa.set_updated_at()',
        tbl, tbl
    );
END;
$$;

-- -----------------------------------------------------------------------------
-- ENUM types
-- -----------------------------------------------------------------------------

-- Cash movement type: W=withdrawal (retiro), D=deposit, T=transfer
DO $$ BEGIN
    CREATE TYPE pyventa.movement_type_enum AS ENUM ('W', 'D', 'T');
EXCEPTION WHEN duplicate_object THEN NULL;
END $$;

-- -----------------------------------------------------------------------------
-- Drop tables (reverse dependency order for idempotent reruns)
-- -----------------------------------------------------------------------------
DROP TABLE IF EXISTS pyventa.sale_items           CASCADE;
DROP TABLE IF EXISTS pyventa.collected_sales       CASCADE;
DROP TABLE IF EXISTS pyventa.sales                 CASCADE;
DROP TABLE IF EXISTS pyventa.daily_sales_summary   CASCADE;
DROP TABLE IF EXISTS pyventa.cash_movements        CASCADE;
DROP TABLE IF EXISTS pyventa.expenses              CASCADE;
DROP TABLE IF EXISTS pyventa.purchase_items        CASCADE;
DROP TABLE IF EXISTS pyventa.purchases             CASCADE;
DROP TABLE IF EXISTS pyventa.inventory_counts      CASCADE;
DROP TABLE IF EXISTS pyventa.inventory_audits      CASCADE;
DROP TABLE IF EXISTS pyventa.shortages             CASCADE;
DROP TABLE IF EXISTS pyventa.promotion_items       CASCADE;
DROP TABLE IF EXISTS pyventa.promotions            CASCADE;
DROP TABLE IF EXISTS pyventa.product_components    CASCADE;
DROP TABLE IF EXISTS pyventa.barcodes              CASCADE;
DROP TABLE IF EXISTS pyventa.products              CASCADE;
DROP TABLE IF EXISTS pyventa.product_families      CASCADE;
DROP TABLE IF EXISTS pyventa.departments           CASCADE;
DROP TABLE IF EXISTS pyventa.units                 CASCADE;
DROP TABLE IF EXISTS pyventa.taxes                 CASCADE;
DROP TABLE IF EXISTS pyventa.registers             CASCADE;
DROP TABLE IF EXISTS pyventa.customers             CASCADE;
DROP TABLE IF EXISTS pyventa.suppliers             CASCADE;
DROP TABLE IF EXISTS pyventa.users                 CASCADE;
DROP TABLE IF EXISTS pyventa.saved_queries         CASCADE;

-- -----------------------------------------------------------------------------
-- users
-- access_level: 1=cashier … 5=admin
-- password_hash: VARCHAR(72) holds bcrypt output (≤72 chars)
-- -----------------------------------------------------------------------------
CREATE TABLE pyventa.users (
    user_id         INTEGER         GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    full_name       VARCHAR(100)    NOT NULL,
    username        VARCHAR(50)     NOT NULL,
    password_hash   VARCHAR(72)     NOT NULL,   -- bcrypt; old MD5 migrated on first login
    access_level    SMALLINT        NOT NULL DEFAULT 1
                                    CHECK (access_level BETWEEN 1 AND 5),
    created_at      TIMESTAMPTZ     NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMPTZ     NOT NULL DEFAULT NOW(),
    CONSTRAINT uq_users_username UNIQUE (username)
);

CREATE INDEX idx_users_access_level ON pyventa.users (access_level);
SELECT pyventa.create_updated_at_trigger('users');

INSERT INTO pyventa.users (user_id, full_name, username, password_hash, access_level)
OVERRIDING SYSTEM VALUE VALUES
    (1, 'Usuario',       'user',  'd41d8cd98f00b204e9800998ecf8427e', 1),
    (2, 'Administrador', 'admin', '1ddff545424249df81f3c4ab552dbb3d', 5);
-- Advance the sequence past the seeded IDs
SELECT setval(pg_get_serial_sequence('pyventa.users','user_id'), 2, true);

-- -----------------------------------------------------------------------------
-- registers (cajas)
-- opened_date: the date this register session was opened.
-- -----------------------------------------------------------------------------
CREATE TABLE pyventa.registers (
    register_id         INTEGER         GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name                VARCHAR(45)     NOT NULL,
    hostname            VARCHAR(15)     NULL,           -- machine name / IP
    opening_balance     NUMERIC(12,2)   NOT NULL DEFAULT 0.00,
    opened_date         DATE            NOT NULL DEFAULT CURRENT_DATE,
    cash_amount         NUMERIC(12,2)   NOT NULL DEFAULT 0.00,
    created_at          TIMESTAMPTZ     NOT NULL DEFAULT NOW(),
    updated_at          TIMESTAMPTZ     NOT NULL DEFAULT NOW()
);

SELECT pyventa.create_updated_at_trigger('registers');

INSERT INTO pyventa.registers (register_id, name, hostname, opening_balance, opened_date, cash_amount)
OVERRIDING SYSTEM VALUE VALUES
    (1, 'Caja 1', 'localhost', 0.00, '2000-01-01', 0.00);
SELECT setval(pg_get_serial_sequence('pyventa.registers','register_id'), 1, true);

-- -----------------------------------------------------------------------------
-- customers (clientes)
-- type: 0=walk-in, 1=regular, 2=wholesale
-- tax_id: RFC (Mexican taxpayer ID). '-' is used for anonymous customers.
-- -----------------------------------------------------------------------------
CREATE TABLE pyventa.customers (
    customer_id     INTEGER         GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    full_name       VARCHAR(150)    NOT NULL,
    tax_id          VARCHAR(15)     NOT NULL DEFAULT '-',
    address         TEXT            NOT NULL DEFAULT '-',
    city            VARCHAR(100)    NOT NULL DEFAULT '-',
    state           VARCHAR(100)    NOT NULL DEFAULT '-',
    phone           VARCHAR(20)     NOT NULL DEFAULT '',
    email           VARCHAR(100)    NOT NULL DEFAULT '',
    type            SMALLINT        NOT NULL DEFAULT 0
                                    CHECK (type IN (0, 1, 2)),
    credit_limit    NUMERIC(12,2)   NOT NULL DEFAULT 0.00,
    created_at      TIMESTAMPTZ     NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMPTZ     NOT NULL DEFAULT NOW(),
    CONSTRAINT uq_customers_tax_id UNIQUE (tax_id)
);

CREATE INDEX idx_customers_type ON pyventa.customers (type);
SELECT pyventa.create_updated_at_trigger('customers');

INSERT INTO pyventa.customers (customer_id, full_name, tax_id, address, city, state, phone, email, type, credit_limit)
OVERRIDING SYSTEM VALUE VALUES
    (1, 'Cliente mostrador', '-', '-', '-', '-', '(000)-000-00-00', '', 0, 0.00);
SELECT setval(pg_get_serial_sequence('pyventa.customers','customer_id'), 1, true);

-- -----------------------------------------------------------------------------
-- suppliers (proveedores)
-- New table. Original stored suppliers in clientes with tipo=1.
-- Mirrors customers contact structure for compatibility with Admin1 widget.
-- -----------------------------------------------------------------------------
CREATE TABLE pyventa.suppliers (
    supplier_id     INTEGER         GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    full_name       VARCHAR(150)    NOT NULL,
    tax_id          VARCHAR(15)     NOT NULL DEFAULT '-',
    address         TEXT            NOT NULL DEFAULT '-',
    city            VARCHAR(100)    NOT NULL DEFAULT '-',
    state           VARCHAR(100)    NOT NULL DEFAULT '-',
    phone           VARCHAR(20)     NOT NULL DEFAULT '',
    email           VARCHAR(100)    NOT NULL DEFAULT '',
    type            SMALLINT        NOT NULL DEFAULT 0,   -- supplier category
    credit_limit    NUMERIC(12,2)   NOT NULL DEFAULT 0.00,  -- credit extended by supplier
    created_at      TIMESTAMPTZ     NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMPTZ     NOT NULL DEFAULT NOW(),
    CONSTRAINT uq_suppliers_tax_id UNIQUE (tax_id)
);

SELECT pyventa.create_updated_at_trigger('suppliers');

-- -----------------------------------------------------------------------------
-- departments (departamentos)
-- -----------------------------------------------------------------------------
CREATE TABLE pyventa.departments (
    department_id   INTEGER         GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name            VARCHAR(100)    NOT NULL,
    created_at      TIMESTAMPTZ     NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMPTZ     NOT NULL DEFAULT NOW(),
    CONSTRAINT uq_departments_name UNIQUE (name)
);

SELECT pyventa.create_updated_at_trigger('departments');

INSERT INTO pyventa.departments (department_id, name)
OVERRIDING SYSTEM VALUE VALUES (1, 'NINGUNO');
SELECT setval(pg_get_serial_sequence('pyventa.departments','department_id'), 1, true);

-- -----------------------------------------------------------------------------
-- product_families (familias)
-- -----------------------------------------------------------------------------
CREATE TABLE pyventa.product_families (
    family_id       INTEGER         GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name            VARCHAR(100)    NOT NULL,
    department_id   INTEGER         NOT NULL DEFAULT 1
                                    REFERENCES pyventa.departments (department_id)
                                    ON DELETE RESTRICT ON UPDATE CASCADE,
    created_at      TIMESTAMPTZ     NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMPTZ     NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_product_families_department_id ON pyventa.product_families (department_id);
SELECT pyventa.create_updated_at_trigger('product_families');

INSERT INTO pyventa.product_families (family_id, name, department_id)
OVERRIDING SYSTEM VALUE VALUES (1, 'NINGUNA', 1);
SELECT setval(pg_get_serial_sequence('pyventa.product_families','family_id'), 1, true);

-- -----------------------------------------------------------------------------
-- units (unidades)
-- -----------------------------------------------------------------------------
CREATE TABLE pyventa.units (
    unit_id         INTEGER         GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name            VARCHAR(20)     NOT NULL,
    created_at      TIMESTAMPTZ     NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMPTZ     NOT NULL DEFAULT NOW(),
    CONSTRAINT uq_units_name UNIQUE (name)
);

SELECT pyventa.create_updated_at_trigger('units');

INSERT INTO pyventa.units (unit_id, name)
OVERRIDING SYSTEM VALUE VALUES (1, 'PZA');
SELECT setval(pg_get_serial_sequence('pyventa.units','unit_id'), 1, true);

-- -----------------------------------------------------------------------------
-- taxes (impuestos)
-- rate stored as decimal factor: 0.1600 = 16% IVA.
-- Original stored integer 16; converted here for cleaner application math.
-- -----------------------------------------------------------------------------
CREATE TABLE pyventa.taxes (
    tax_id          INTEGER         GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name            VARCHAR(100)    NOT NULL,
    rate            NUMERIC(6,4)    NOT NULL    -- e.g. 0.1600 for 16%
                                    CHECK (rate >= 0 AND rate < 1),
    created_at      TIMESTAMPTZ     NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMPTZ     NOT NULL DEFAULT NOW()
);

SELECT pyventa.create_updated_at_trigger('taxes');

INSERT INTO pyventa.taxes (tax_id, name, rate)
OVERRIDING SYSTEM VALUE VALUES (1, 'I.V.A', 0.1600);
SELECT setval(pg_get_serial_sequence('pyventa.taxes','tax_id'), 1, true);

-- -----------------------------------------------------------------------------
-- products (productos)
-- product_id (was ref): internal surrogate PK.
-- primary_barcode (was codigo): main barcode as BIGINT (EAN-13 fits in BIGINT).
-- markup (ganancia): percentage e.g. 20.0000 = 20%.
-- stock: legacy column kept for backward compat; canonical stock = inventory_counts.
-- total_sold: denormalised lifetime counter; recalculable from sale_items.
-- -----------------------------------------------------------------------------
CREATE TABLE pyventa.products (
    product_id          INTEGER         GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    primary_barcode     BIGINT          NOT NULL DEFAULT 0,
    description         VARCHAR(100)    NOT NULL,
    family_id           INTEGER         NOT NULL DEFAULT 1
                                        REFERENCES pyventa.product_families (family_id)
                                        ON DELETE RESTRICT ON UPDATE CASCADE,
    unit_cost           NUMERIC(12,4)   NOT NULL DEFAULT 0.0000,
    markup              NUMERIC(8,4)    NOT NULL DEFAULT 0.0000,  -- % e.g. 20.0000
    price               NUMERIC(12,4)   NOT NULL DEFAULT 0.0000,
    stock               NUMERIC(12,4)   NOT NULL DEFAULT 0.0000,  -- legacy; see inventory_counts
    unit_id             INTEGER         NOT NULL DEFAULT 1
                                        REFERENCES pyventa.units (unit_id)
                                        ON DELETE RESTRICT ON UPDATE CASCADE,
    total_sold          NUMERIC(12,4)   NOT NULL DEFAULT 0.0000,
    tax_id              INTEGER         NOT NULL DEFAULT 1
                                        REFERENCES pyventa.taxes (tax_id)
                                        ON DELETE RESTRICT ON UPDATE CASCADE,
    created_at          TIMESTAMPTZ     NOT NULL DEFAULT NOW(),
    updated_at          TIMESTAMPTZ     NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_products_primary_barcode ON pyventa.products (primary_barcode);
CREATE INDEX idx_products_description     ON pyventa.products (description);
CREATE INDEX idx_products_family_id       ON pyventa.products (family_id);
CREATE INDEX idx_products_unit_id         ON pyventa.products (unit_id);
CREATE INDEX idx_products_tax_id          ON pyventa.products (tax_id);
SELECT pyventa.create_updated_at_trigger('products');

-- -----------------------------------------------------------------------------
-- barcodes (codigos)
-- Barcode aliases per product. Enables multi-barcode scanning.
-- -----------------------------------------------------------------------------
CREATE TABLE pyventa.barcodes (
    product_id      INTEGER         NOT NULL
                                    REFERENCES pyventa.products (product_id)
                                    ON DELETE CASCADE ON UPDATE CASCADE,
    barcode         VARCHAR(25)     NOT NULL,
    created_at      TIMESTAMPTZ     NOT NULL DEFAULT NOW(),
    PRIMARY KEY (product_id, barcode)
);

CREATE INDEX idx_barcodes_barcode ON pyventa.barcodes (barcode);  -- fast lookup by code

-- -----------------------------------------------------------------------------
-- product_components (subproductos)
-- Bundle / kit relationships.
-- component_product_id: the child product (part of a kit)
-- product_id: the parent / bundle product
-- One component can only belong to one bundle (PK on component_product_id).
-- -----------------------------------------------------------------------------
CREATE TABLE pyventa.product_components (
    component_product_id    INTEGER         NOT NULL
                                            REFERENCES pyventa.products (product_id)
                                            ON DELETE CASCADE ON UPDATE CASCADE,
    product_id              INTEGER         NOT NULL
                                            REFERENCES pyventa.products (product_id)
                                            ON DELETE CASCADE ON UPDATE CASCADE,
    quantity                NUMERIC(12,4)   NOT NULL DEFAULT 1.0000,
    created_at              TIMESTAMPTZ     NOT NULL DEFAULT NOW(),
    updated_at              TIMESTAMPTZ     NOT NULL DEFAULT NOW(),
    PRIMARY KEY (component_product_id)
);

CREATE INDEX idx_product_components_product_id ON pyventa.product_components (product_id);
SELECT pyventa.create_updated_at_trigger('product_components');

-- -----------------------------------------------------------------------------
-- promotions (promociones)
-- discount_rate: decimal factor e.g. 0.1000 = 10% off.
-- Original stored integer percentage; converted here for consistent math.
-- -----------------------------------------------------------------------------
CREATE TABLE pyventa.promotions (
    promotion_id    INTEGER         GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name            VARCHAR(50)     NOT NULL,
    discount_rate   NUMERIC(6,4)    NOT NULL    -- e.g. 0.1000 = 10%
                                    CHECK (discount_rate >= 0 AND discount_rate <= 1),
    start_date      DATE            NOT NULL,
    end_date        DATE            NOT NULL,
    min_quantity    NUMERIC(12,4)   NOT NULL DEFAULT 0.0000,
    max_quantity    NUMERIC(12,4)   NOT NULL DEFAULT 0.0000,
    created_at      TIMESTAMPTZ     NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMPTZ     NOT NULL DEFAULT NOW(),
    CONSTRAINT chk_promotions_dates CHECK (end_date >= start_date)
);

CREATE INDEX idx_promotions_dates ON pyventa.promotions (start_date, end_date);
SELECT pyventa.create_updated_at_trigger('promotions');

-- -----------------------------------------------------------------------------
-- promotion_items (ofertas)
-- Polymorphic link: a promotion targets a product, family, or department.
-- item_type: 0=product, 1=family, 2=department
-- product_group_id references different tables depending on item_type —
--   no FK constraint possible; application must enforce referential integrity.
-- -----------------------------------------------------------------------------
CREATE TABLE pyventa.promotion_items (
    promotion_id        INTEGER     NOT NULL
                                    REFERENCES pyventa.promotions (promotion_id)
                                    ON DELETE CASCADE ON UPDATE CASCADE,
    product_group_id    INTEGER     NOT NULL,
    item_type           SMALLINT    NOT NULL
                                    CHECK (item_type IN (0, 1, 2)),
    created_at          TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    PRIMARY KEY (promotion_id, product_group_id, item_type)
);

CREATE INDEX idx_promotion_items_promotion_id ON pyventa.promotion_items (promotion_id);

-- -----------------------------------------------------------------------------
-- inventory_audits (inventarios)
-- Formal inventory count sessions.
-- status: 0=in-progress, 1=completed, 2=cancelled
-- Note: audit_id=0 is reserved as the "live tracking" sentinel in inventory_counts;
--   it is NOT a row in this table.
-- -----------------------------------------------------------------------------
CREATE TABLE pyventa.inventory_audits (
    audit_id            INTEGER         GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    balance             NUMERIC(12,2)   NOT NULL DEFAULT 0.00,
    scope               VARCHAR(120)    NULL,       -- which warehouse / area
    order_number        VARCHAR(20)     NULL,
    status              SMALLINT        NOT NULL DEFAULT 0
                                        CHECK (status IN (0, 1, 2)),
    auditor_user_id     INTEGER         NOT NULL
                                        REFERENCES pyventa.users (user_id)
                                        ON DELETE RESTRICT ON UPDATE CASCADE,
    manager_user_id     INTEGER         NOT NULL
                                        REFERENCES pyventa.users (user_id)
                                        ON DELETE RESTRICT ON UPDATE CASCADE,
    created_at          TIMESTAMPTZ     NOT NULL DEFAULT NOW(),
    updated_at          TIMESTAMPTZ     NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_inventory_audits_auditor ON pyventa.inventory_audits (auditor_user_id);
CREATE INDEX idx_inventory_audits_manager ON pyventa.inventory_audits (manager_user_id);
SELECT pyventa.create_updated_at_trigger('inventory_audits');

-- -----------------------------------------------------------------------------
-- inventory_counts (existencia)
-- Per-product stock levels per audit session.
-- audit_id=0 is the live tracking row (updated on every purchase/sale/adjustment).
-- discrepancy = physical_stock - logical_stock (NULL until physical count entered).
-- No FK on audit_id because audit_id=0 is a sentinel value, not a real audit row.
-- -----------------------------------------------------------------------------
CREATE TABLE pyventa.inventory_counts (
    product_id      INTEGER         NOT NULL
                                    REFERENCES pyventa.products (product_id)
                                    ON DELETE CASCADE ON UPDATE CASCADE,
    audit_id        INTEGER         NOT NULL DEFAULT 0,  -- 0 = live row
    physical_stock  NUMERIC(12,4)   NOT NULL DEFAULT 0.0000,
    logical_stock   NUMERIC(12,4)   NOT NULL DEFAULT 0.0000,
    discrepancy     NUMERIC(12,4)   NULL,
    PRIMARY KEY (product_id, audit_id)
);

CREATE INDEX idx_inventory_counts_product_id ON pyventa.inventory_counts (product_id);

-- -----------------------------------------------------------------------------
-- shortages (faltantes)
-- One active shortage request per product.
-- -----------------------------------------------------------------------------
CREATE TABLE pyventa.shortages (
    product_id      INTEGER         NOT NULL
                                    REFERENCES pyventa.products (product_id)
                                    ON DELETE CASCADE ON UPDATE CASCADE,
    user_id         INTEGER         NOT NULL
                                    REFERENCES pyventa.users (user_id)
                                    ON DELETE RESTRICT ON UPDATE CASCADE,
    quantity        NUMERIC(12,4)   NOT NULL DEFAULT 0.0000,
    priority        SMALLINT        NOT NULL DEFAULT 0,
    created_at      DATE            NOT NULL DEFAULT CURRENT_DATE,
    updated_at      TIMESTAMPTZ     NOT NULL DEFAULT NOW(),
    PRIMARY KEY (product_id)
);

CREATE INDEX idx_shortages_user_id ON pyventa.shortages (user_id);

-- Trigger for updated_at (DATE-based created_at is intentional — stays as-is)
CREATE TRIGGER trg_shortages_updated_at
    BEFORE UPDATE ON pyventa.shortages
    FOR EACH ROW EXECUTE FUNCTION pyventa.set_updated_at();

-- -----------------------------------------------------------------------------
-- purchases (compras)
-- status: 0=draft, 1=received, 2=cancelled (added from alterlog v3.2)
-- -----------------------------------------------------------------------------
CREATE TABLE pyventa.purchases (
    purchase_id     INTEGER         GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    supplier_id     INTEGER         NOT NULL
                                    REFERENCES pyventa.suppliers (supplier_id)
                                    ON DELETE RESTRICT ON UPDATE CASCADE,
    buyer_user_id   INTEGER         NOT NULL
                                    REFERENCES pyventa.users (user_id)
                                    ON DELETE RESTRICT ON UPDATE CASCADE,
    total_amount    NUMERIC(12,2)   NOT NULL DEFAULT 0.00,
    status          SMALLINT        NOT NULL DEFAULT 0
                                    CHECK (status IN (0, 1, 2)),
    created_at      TIMESTAMPTZ     NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMPTZ     NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_purchases_supplier_id   ON pyventa.purchases (supplier_id);
CREATE INDEX idx_purchases_buyer_user_id ON pyventa.purchases (buyer_user_id);
CREATE INDEX idx_purchases_created_at    ON pyventa.purchases (created_at DESC);
SELECT pyventa.create_updated_at_trigger('purchases');

-- -----------------------------------------------------------------------------
-- purchase_items (comprados)
-- unit_cost: historical cost at time of purchase (not a FK to products.unit_cost).
-- -----------------------------------------------------------------------------
CREATE TABLE pyventa.purchase_items (
    purchase_id     INTEGER         NOT NULL
                                    REFERENCES pyventa.purchases (purchase_id)
                                    ON DELETE CASCADE ON UPDATE CASCADE,
    product_id      INTEGER         NOT NULL
                                    REFERENCES pyventa.products (product_id)
                                    ON DELETE RESTRICT ON UPDATE CASCADE,
    quantity        NUMERIC(12,4)   NOT NULL,
    unit_cost       NUMERIC(12,4)   NOT NULL,
    total_amount    NUMERIC(12,2)   NOT NULL,
    created_at      TIMESTAMPTZ     NOT NULL DEFAULT NOW(),
    PRIMARY KEY (purchase_id, product_id)
);

CREATE INDEX idx_purchase_items_product_id ON pyventa.purchase_items (product_id);

-- -----------------------------------------------------------------------------
-- sales (notas)
-- sale_type:      0=receipt, 1=invoice, 2=return
-- payment_status: 0=unpaid, 1=paid, 2=on-credit, 3=returned
-- -----------------------------------------------------------------------------
CREATE TABLE pyventa.sales (
    sale_id         INTEGER         GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    customer_id     INTEGER         NOT NULL DEFAULT 1
                                    REFERENCES pyventa.customers (customer_id)
                                    ON DELETE RESTRICT ON UPDATE CASCADE,
    user_id         INTEGER         NOT NULL
                                    REFERENCES pyventa.users (user_id)
                                    ON DELETE RESTRICT ON UPDATE CASCADE,
    register_id     INTEGER         NOT NULL
                                    REFERENCES pyventa.registers (register_id)
                                    ON DELETE RESTRICT ON UPDATE CASCADE,
    subtotal        NUMERIC(12,2)   NOT NULL DEFAULT 0.00,
    discounts       NUMERIC(12,2)   NOT NULL DEFAULT 0.00,
    total_amount    NUMERIC(12,2)   NOT NULL DEFAULT 0.00,
    sale_type       SMALLINT        NOT NULL DEFAULT 0
                                    CHECK (sale_type IN (0, 1, 2)),
    payment_status  SMALLINT        NOT NULL DEFAULT 0
                                    CHECK (payment_status IN (0, 1, 2, 3)),
    created_at      TIMESTAMPTZ     NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMPTZ     NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_sales_customer_id    ON pyventa.sales (customer_id);
CREATE INDEX idx_sales_user_id        ON pyventa.sales (user_id);
CREATE INDEX idx_sales_register_id    ON pyventa.sales (register_id);
CREATE INDEX idx_sales_created_at     ON pyventa.sales (created_at DESC);
CREATE INDEX idx_sales_payment_status ON pyventa.sales (payment_status);

-- Partial index: unpaid credit sales — the most-queried subset for AR
CREATE INDEX idx_sales_unpaid_credit  ON pyventa.sales (customer_id, created_at)
    WHERE payment_status = 2;

SELECT pyventa.create_updated_at_trigger('sales');

-- -----------------------------------------------------------------------------
-- sale_items (vendidos)
-- line_type: line item flag (0=normal; usage defined by application).
-- unit_price: historical price at time of sale.
-- -----------------------------------------------------------------------------
CREATE TABLE pyventa.sale_items (
    sale_id         INTEGER         NOT NULL
                                    REFERENCES pyventa.sales (sale_id)
                                    ON DELETE CASCADE ON UPDATE CASCADE,
    product_id      INTEGER         NOT NULL
                                    REFERENCES pyventa.products (product_id)
                                    ON DELETE RESTRICT ON UPDATE CASCADE,
    line_type       SMALLINT        NOT NULL DEFAULT 0,
    quantity        NUMERIC(12,4)   NOT NULL,
    unit_price      NUMERIC(12,4)   NOT NULL DEFAULT 0.0000,
    total_amount    NUMERIC(12,2)   NOT NULL,
    created_at      TIMESTAMPTZ     NOT NULL DEFAULT NOW(),
    PRIMARY KEY (sale_id, product_id, line_type)
);

CREATE INDEX idx_sale_items_product_id ON pyventa.sale_items (product_id);

-- -----------------------------------------------------------------------------
-- collected_sales (notas_cobradas)
-- Records when a credit sale is finally paid off.
-- -----------------------------------------------------------------------------
CREATE TABLE pyventa.collected_sales (
    id              INTEGER         GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    sale_id         INTEGER         NOT NULL
                                    REFERENCES pyventa.sales (sale_id)
                                    ON DELETE CASCADE ON UPDATE CASCADE,
    collected_at    TIMESTAMPTZ     NOT NULL DEFAULT NOW(),
    CONSTRAINT uq_collected_sales_sale_id UNIQUE (sale_id)
);

-- -----------------------------------------------------------------------------
-- daily_sales_summary (ventas)
-- REDESIGNED: original used date as PK (one row per day maximum).
-- New: GENERATED ALWAYS AS IDENTITY PK + UNIQUE constraint on summary_date.
-- Populated by the end-of-day close procedure.
-- -----------------------------------------------------------------------------
CREATE TABLE pyventa.daily_sales_summary (
    summary_id      INTEGER         GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    summary_date    DATE            NOT NULL,
    subtotal        NUMERIC(12,2)   NOT NULL DEFAULT 0.00,
    discounts       NUMERIC(12,2)   NOT NULL DEFAULT 0.00,
    total_amount    NUMERIC(12,2)   NOT NULL DEFAULT 0.00,
    cash_amount     NUMERIC(12,2)   NOT NULL DEFAULT 0.00,
    created_at      TIMESTAMPTZ     NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMPTZ     NOT NULL DEFAULT NOW(),
    CONSTRAINT uq_daily_sales_summary_date UNIQUE (summary_date)
);

SELECT pyventa.create_updated_at_trigger('daily_sales_summary');

-- -----------------------------------------------------------------------------
-- cash_movements (movimientos)
-- Uses the movement_type_enum defined above.
-- W=withdrawal (retiro), D=deposit, T=transfer
-- -----------------------------------------------------------------------------
CREATE TABLE pyventa.cash_movements (
    movement_id     INTEGER                     GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    user_id         INTEGER                     NOT NULL
                                                REFERENCES pyventa.users (user_id)
                                                ON DELETE RESTRICT ON UPDATE CASCADE,
    register_id     INTEGER                     NOT NULL
                                                REFERENCES pyventa.registers (register_id)
                                                ON DELETE RESTRICT ON UPDATE CASCADE,
    detail          VARCHAR(100)                NULL,
    movement_type   pyventa.movement_type_enum  NOT NULL,
    amount          NUMERIC(12,2)               NOT NULL,
    created_at      TIMESTAMPTZ                 NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_cash_movements_user_id     ON pyventa.cash_movements (user_id);
CREATE INDEX idx_cash_movements_register_id ON pyventa.cash_movements (register_id);
CREATE INDEX idx_cash_movements_created_at  ON pyventa.cash_movements (created_at DESC);

-- -----------------------------------------------------------------------------
-- expenses (gastos)
-- Petty-cash / expense withdrawals from a register.
-- -----------------------------------------------------------------------------
CREATE TABLE pyventa.expenses (
    expense_id      INTEGER         GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    user_id         INTEGER         NOT NULL
                                    REFERENCES pyventa.users (user_id)
                                    ON DELETE RESTRICT ON UPDATE CASCADE,
    register_id     INTEGER         NOT NULL
                                    REFERENCES pyventa.registers (register_id)
                                    ON DELETE RESTRICT ON UPDATE CASCADE,
    description     VARCHAR(200)    NOT NULL,
    amount          NUMERIC(12,2)   NOT NULL,
    created_at      TIMESTAMPTZ     NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMPTZ     NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_expenses_user_id     ON pyventa.expenses (user_id);
CREATE INDEX idx_expenses_register_id ON pyventa.expenses (register_id);
CREATE INDEX idx_expenses_created_at  ON pyventa.expenses (created_at DESC);
SELECT pyventa.create_updated_at_trigger('expenses');

-- -----------------------------------------------------------------------------
-- saved_queries (consultas)
-- User-defined report queries stored in the DB.
-- WARNING: query_text must be validated before execution to prevent SQL injection.
-- -----------------------------------------------------------------------------
CREATE TABLE pyventa.saved_queries (
    query_id        INTEGER         GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    title           VARCHAR(100)    NOT NULL,
    description     TEXT            NOT NULL DEFAULT '',
    query_text      TEXT            NOT NULL,
    created_at      TIMESTAMPTZ     NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMPTZ     NOT NULL DEFAULT NOW()
);

SELECT pyventa.create_updated_at_trigger('saved_queries');

-- =============================================================================
-- Useful views
-- =============================================================================

-- Current stock levels (live rows only, audit_id = 0)
CREATE OR REPLACE VIEW pyventa.v_current_stock AS
SELECT
    p.product_id,
    p.primary_barcode,
    p.description,
    pf.name             AS family,
    d.name              AS department,
    ic.logical_stock,
    ic.physical_stock,
    p.price,
    u.name              AS unit
FROM pyventa.products          p
JOIN pyventa.inventory_counts  ic ON ic.product_id = p.product_id AND ic.audit_id = 0
JOIN pyventa.product_families  pf ON pf.family_id  = p.family_id
JOIN pyventa.departments       d  ON d.department_id = pf.department_id
JOIN pyventa.units             u  ON u.unit_id = p.unit_id;

-- Active promotions as of today
CREATE OR REPLACE VIEW pyventa.v_active_promotions AS
SELECT
    pr.promotion_id,
    pr.name,
    pr.discount_rate,
    pr.start_date,
    pr.end_date,
    pr.min_quantity,
    pr.max_quantity,
    pi.product_group_id,
    pi.item_type
FROM pyventa.promotions      pr
JOIN pyventa.promotion_items pi ON pi.promotion_id = pr.promotion_id
WHERE CURRENT_DATE BETWEEN pr.start_date AND pr.end_date;

COMMIT;
