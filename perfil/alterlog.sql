-- ----3--
CREATE TABLE IF NOT EXISTS `inventarios` (
  `id_inventario` int(11) NOT NULL AUTO_INCREMENT,
  `fecha` datetime NOT NULL,
  `saldo` float NOT NULL,
  `dominio` varchar(120) COLLATE latin1_spanish_ci DEFAULT NULL,
  `orden` varchar(20) COLLATE latin1_spanish_ci DEFAULT NULL,
  `estado` tinyint(4) NOT NULL,
  `auditor` int(20) NOT NULL,
  `gerente` int(20) NOT NULL,
  PRIMARY KEY (`id_inventario`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci ;

CREATE  TABLE IF NOT EXISTS `movimientos` (
  `id_movimiento` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT ,
  `usuario` INT(20) UNSIGNED NOT NULL ,
  `caja` INT(10) NOT NULL ,
  `detalle` VARCHAR(100) CHARACTER SET 'latin1' COLLATE 'latin1_spanish_ci' NULL DEFAULT NULL ,
  `tipo` ENUM('R','D','T') CHARACTER SET 'latin1' COLLATE 'latin1_spanish_ci' NOT NULL ,
  `monto` FLOAT(11) NOT NULL ,
  `fecha` DATETIME NOT NULL ,
  PRIMARY KEY (`id_movimiento`) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1
COLLATE = latin1_spanish_ci;

ALTER TABLE `notas` COLLATE = latin1_bin , ADD COLUMN `caja` INT(11) NOT NULL  AFTER `usuario` , CHANGE COLUMN `cliente` `cliente` INT(123) NOT NULL  , CHANGE COLUMN `usuario` `usuario` INT(20) NOT NULL  , CHANGE COLUMN `tipo` `tipo` TINYINT(4) NOT NULL COMMENT '0:Nota;1:Factura; 2: Devolucion'  , CHANGE COLUMN `status` `status` TINYINT(4) NOT NULL COMMENT '0:sin pagar; 1:pagado, 2:en credito, 3:devolucion'  
, ADD INDEX `fk_notas_clientes1` (`cliente` ASC) 
, ADD INDEX `fk_notas_usuarios1` (`usuario` ASC) 
, ADD INDEX `fk_notas_cajas1` (`caja` ASC) ;

ALTER TABLE `notas_cobradas` COLLATE = latin1_bin ;
ALTER TABLE  `cajas` CHANGE  `num_caja`  `num_caja` INT( 100 ) NOT NULL AUTO_INCREMENT

ALTER TABLE `ofertas` COLLATE = latin1_bin ;



ALTER TABLE `promociones` COLLATE = latin1_bin ;

ALTER TABLE `subproductos` COLLATE = latin1_bin , CHANGE COLUMN `producto` `producto` INT(200) NOT NULL  
, ADD INDEX `fk_subproductos_productos1` (`producto` ASC) ;

ALTER TABLE `unidades` COLLATE = latin1_bin ;

ALTER TABLE `usuarios` CHANGE `id` `id_usuario` INT( 20 ) NOT NULL AUTO_INCREMENT ,
CHANGE `name` `nombre` VARCHAR( 50 ) CHARACTER SET latin1 COLLATE latin1_spanish_ci NOT NULL ,
CHANGE `user` `usuario` VARCHAR( 50 ) CHARACTER SET latin1 COLLATE latin1_spanish_ci NOT NULL ,
CHANGE `pass` `clave` VARCHAR( 50 ) CHARACTER SET ascii COLLATE ascii_bin NOT NULL ,
CHANGE `level` `nivel` INT( 10 ) NOT NULL DEFAULT '0';

ALTER TABLE `vendidos` COLLATE = latin1_bin , CHANGE COLUMN `producto` `producto` INT(200) NOT NULL  
, ADD INDEX `fk_vendidos_productos1` (`producto` ASC) ;

ALTER TABLE `ventas` DROP COLUMN `inicial` , ADD COLUMN `subtotal` FLOAT(10) UNSIGNED NOT NULL  AFTER `fecha` , ADD COLUMN `descuentos` FLOAT(10) UNSIGNED NOT NULL  AFTER `subtotal` , ADD COLUMN `efectivo` FLOAT(10) UNSIGNED NOT NULL  AFTER `total` , CHANGE COLUMN `total` `total` FLOAT(10) UNSIGNED NOT NULL  ;

DROP TABLE IF EXISTS `facturas` ;

UPDATE `productos` SET ultima_modificacion=now() where ultima_modificacion='0000-00-00 00:00:00';
ALTER TABLE `productos` COLLATE = latin1_spanish_ci ,  CHANGE `desc` `descripcion` VARCHAR(100) CHARACTER SET 'latin1' COLLATE 'latin1_spanish_ci' NOT NULL  AFTER `ref` , CHANGE COLUMN `codigo` `codigo` BIGINT(20) UNSIGNED NOT NULL DEFAULT '0'  ;

CREATE TABLE IF NOT EXISTS `cajas` (
  `num_caja` int(10) NOT NULL,
  `nombre` varchar(45) COLLATE latin1_spanish_ci NOT NULL,
  `maquina` varchar(15) COLLATE latin1_spanish_ci DEFAULT NULL,
  `saldo_inicial` float unsigned NOT NULL,
  `estado` date NOT NULL,
  `efectivo` float unsigned NOT NULL,
  PRIMARY KEY (`num_caja`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

CREATE TABLE IF NOT EXISTS `codigos` (
  `producto` int(200) NOT NULL,
  `codigo` varchar(20) COLLATE latin1_spanish_ci NOT NULL,
  PRIMARY KEY (`producto`,`codigo`),
  KEY `fk_codigos_productos1` (`producto`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

CREATE TABLE IF NOT EXISTS `consultas` (
  `id_consulta` int(11) NOT NULL AUTO_INCREMENT,
  `titulo` varchar(100) NOT NULL,
  `descripcion` text NOT NULL,
  `query` text NOT NULL,
  PRIMARY KEY (`id_consulta`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

CREATE TABLE IF NOT EXISTS `existencia` (
  `producto` int(200) NOT NULL,
  `inventario` int(11) NOT NULL,
  `stock_fisico` float NOT NULL,
  `stock_logico` float NOT NULL,
  `inconsistencia` float DEFAULT NULL,
  PRIMARY KEY (`producto`,`inventario`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

INSERT INTO existencia SELECT ref,1,0,0,0 FROM productos WHERE ref NOT IN (SELECT producto from existencia)
UPDATE existencia, productos SET stock_logico=stock WHERE producto=ref;
UPDATE productos SET stock=0;

-- ----3.1--
ALTER TABLE `promociones` CHANGE `descuento` `descuento` FLOAT NOT NULL ;
ALTER TABLE `promociones` ADD `maximo` FLOAT NOT NULL ;
ALTER TABLE `compras` ADD `proveedor` INT NOT NULL AFTER `fecha` ;



-- ----3.2--
UPDATE notas SET caja=1 where caja=-1;

ALTER TABLE  `compras` ADD  `estado` INT NOT NULL

-- ----3.5--
ALTER TABLE  `movimientos` CHANGE  `tipo`  `tipo` VARCHAR( 10 ) CHARACTER SET latin1 COLLATE latin1_spanish_ci NOT NULL
-- ALTER TABLE  `clientes` ADD  `limite_credito` FLOAT NULL
ALTER TABLE `subproductos`
  DROP PRIMARY KEY,
   ADD PRIMARY KEY(
     `subproducto`,
     `producto`);
