-- phpMyAdmin SQL Dump
-- version 3.4.5
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Oct 16, 2011 at 05:21 AM
-- Server version: 5.1.58
-- PHP Version: 5.3.8

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `pyventa`
--

-- --------------------------------------------------------

--
-- Table structure for table `cajas`
--

CREATE TABLE IF NOT EXISTS `cajas` (
  `num_caja` int(10) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) COLLATE latin1_spanish_ci NOT NULL,
  `maquina` varchar(15) COLLATE latin1_spanish_ci DEFAULT NULL,
  `saldo_inicial` float unsigned NOT NULL,
  `estado` date NOT NULL,
  `efectivo` float unsigned NOT NULL,
  PRIMARY KEY (`num_caja`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci AUTO_INCREMENT=2 ;

--
-- Dumping data for table `cajas`
--

INSERT INTO `cajas` (`num_caja`, `nombre`, `maquina`, `saldo_inicial`, `estado`, `efectivo`) VALUES
(1, 'Caja 1', 'localhost', 0, '0000-00-00', 0);

-- --------------------------------------------------------

--
-- Table structure for table `clientes`
--

CREATE TABLE IF NOT EXISTS `clientes` (
  `id` int(123) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(150) COLLATE latin1_spanish_ci NOT NULL,
  `rfc` varchar(15) COLLATE latin1_spanish_ci NOT NULL,
  `direccion` varchar(100) COLLATE latin1_spanish_ci NOT NULL,
  `poblacion` varchar(100) COLLATE latin1_spanish_ci NOT NULL,
  `estado` varchar(100) COLLATE latin1_spanish_ci NOT NULL,
  `tel` varchar(15) COLLATE latin1_spanish_ci NOT NULL,
  `correo` varchar(50) COLLATE latin1_spanish_ci NOT NULL,
  `tipo` int(2) NOT NULL,
  `credito` float NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `rfc` (`rfc`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci AUTO_INCREMENT=2 ;

--
-- Dumping data for table `clientes`
--

INSERT INTO `clientes` (`id`, `nombre`, `rfc`, `direccion`, `poblacion`, `estado`, `tel`, `correo`, `tipo`, `credito`) VALUES
(1, 'Cliente mostrador', '-', '-', '-', '-', '(000)-000-00-00', '00000', 0, 0);

-- --------------------------------------------------------

--
-- Table structure for table `codigos`
--

CREATE TABLE IF NOT EXISTS `codigos` (
  `producto` int(200) NOT NULL,
  `codigo` varchar(20) COLLATE latin1_spanish_ci NOT NULL,
  PRIMARY KEY (`producto`,`codigo`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

-- --------------------------------------------------------

--
-- Table structure for table `comprados`
--

CREATE TABLE IF NOT EXISTS `comprados` (
  `compra` int(11) NOT NULL,
  `producto` int(11) NOT NULL,
  `cantidad` float NOT NULL,
  `costo` float NOT NULL,
  `total` float NOT NULL,
  PRIMARY KEY (`compra`,`producto`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 COLLATE=latin1_bin;

-- --------------------------------------------------------

--
-- Table structure for table `compras`
--

CREATE TABLE IF NOT EXISTS `compras` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fecha` datetime NOT NULL,
  `proveedor` INT NOT NULL,
  `comprador` int(11) NOT NULL,
  `total` float NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 COLLATE=latin1_bin AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `consultas`
--

CREATE TABLE IF NOT EXISTS `consultas` (
  `id_consulta` int(11) NOT NULL AUTO_INCREMENT,
  `titulo` varchar(100) NOT NULL,
  `descripcion` text NOT NULL,
  `query` text NOT NULL,
  PRIMARY KEY (`id_consulta`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `departamentos`
--

CREATE TABLE IF NOT EXISTS `departamentos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) CHARACTER SET latin1 COLLATE latin1_spanish_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 COLLATE=latin1_bin AUTO_INCREMENT=2 ;

--
-- Dumping data for table `departamentos`
--

INSERT INTO `departamentos` (`id`, `nombre`) VALUES
(1, 'NINGUNO');

-- --------------------------------------------------------

--
-- Table structure for table `existencia`
--

CREATE TABLE IF NOT EXISTS `existencia` (
  `producto` int(200) NOT NULL,
  `inventario` int(11) NOT NULL,
  `stock_fisico` float NOT NULL,
  `stock_logico` float NOT NULL,
  `inconsistencia` float DEFAULT NULL,
  PRIMARY KEY (`producto`,`inventario`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

-- --------------------------------------------------------

--
-- Table structure for table `faltantes`
--

CREATE TABLE IF NOT EXISTS `faltantes` (
  `producto` int(11) NOT NULL AUTO_INCREMENT,
  `usuario` int(11) NOT NULL,
  `cantidad` float NOT NULL,
  `prioridad` int(11) NOT NULL,
  `fecha` date NOT NULL,
  PRIMARY KEY (`producto`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 COLLATE=latin1_bin AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `familias`
--

CREATE TABLE IF NOT EXISTS `familias` (
  `id` int(12) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `departamento` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `familias`
--

INSERT INTO `familias` (`id`, `nombre`, `departamento`) VALUES
(1, 'NINGUNA', 1);

-- --------------------------------------------------------

--
-- Table structure for table `gastos`
--

CREATE TABLE IF NOT EXISTS `gastos` (
  `num_gasto` int(11) NOT NULL AUTO_INCREMENT,
  `usuario` int(20) NOT NULL,
  `caja` int(11) NOT NULL,
  `fecha` datetime NOT NULL,
  `concepto` varchar(200) COLLATE latin1_spanish_ci NOT NULL,
  `cantidad` float NOT NULL,
  PRIMARY KEY (`num_gasto`,`usuario`,`caja`),
  KEY `autorizado_por` (`usuario`),
  KEY `hecho_en` (`caja`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `impuestos`
--

CREATE TABLE IF NOT EXISTS `impuestos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) CHARACTER SET latin1 COLLATE latin1_spanish_ci NOT NULL,
  `porcentaje` float NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `impuestos`
--

INSERT INTO `impuestos` (`id`, `nombre`, `porcentaje`) VALUES
(1, 'I.V.A', 16);

-- --------------------------------------------------------

--
-- Table structure for table `inventarios`
--

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
) ENGINE=MyISAM DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `movimientos`
--

CREATE TABLE IF NOT EXISTS `movimientos` (
  `id_movimiento` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `usuario` int(20) unsigned NOT NULL,
  `caja` int(10) NOT NULL,
  `detalle` varchar(100) COLLATE latin1_spanish_ci DEFAULT NULL,
  `tipo` varchar(10) COLLATE latin1_spanish_ci NOT NULL,
  `monto` float NOT NULL,
  `fecha` datetime NOT NULL,
  PRIMARY KEY (`id_movimiento`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `notas`
--

CREATE TABLE IF NOT EXISTS `notas` (
  `id` int(30) NOT NULL AUTO_INCREMENT,
  `cliente` int(123) NOT NULL,
  `usuario` int(20) NOT NULL,
  `caja` int(11) NOT NULL,
  `total` float NOT NULL,
  `fecha` datetime NOT NULL,
  `tipo` tinyint(4) NOT NULL COMMENT '0:Nota;1:Factura; 2: Devolucion',
  `status` tinyint(4) NOT NULL COMMENT '0:sin pagar; 1:pagado, 2:en credito, 3:devolucion',
  PRIMARY KEY (`id`),
  KEY `fk_notas_clientes1` (`cliente`),
  KEY `fk_notas_usuarios1` (`usuario`),
  KEY `fk_notas_cajas1` (`caja`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `notas_cobradas`
--

CREATE TABLE IF NOT EXISTS `notas_cobradas` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nota` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nota` (`nota`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `ofertas`
--

CREATE TABLE IF NOT EXISTS `ofertas` (
  `promocion` int(11) NOT NULL,
  `conjunto` int(11) NOT NULL,
  `tipo` int(3) NOT NULL,
  PRIMARY KEY (`promocion`,`conjunto`,`tipo`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `productos`
--

CREATE TABLE IF NOT EXISTS `productos` (
  `codigo` bigint(20) NOT NULL DEFAULT '0',
  `ref` int(200) NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(100) COLLATE latin1_spanish_ci NOT NULL,
  `familia` int(5) DEFAULT '0',
  `costo` double NOT NULL,
  `ganancia` double NOT NULL,
  `precio` double NOT NULL,
  `stock` float DEFAULT '0',
  `unidad` int(5) NOT NULL,
  `vendidas` float NOT NULL,
  `impuesto` int(11) NOT NULL,
  `ultima_modificacion` datetime NOT NULL,
  PRIMARY KEY (`ref`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `promociones`
--

CREATE TABLE IF NOT EXISTS `promociones` (
  `id` int(13) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) CHARACTER SET latin1 COLLATE latin1_spanish_ci NOT NULL,
  `descuento` FLOAT NOT NULL,
  `inicio` date NOT NULL,
  `fin` date NOT NULL,
  `minimo` float NOT NULL,
  `maximo` FLOAT NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `subproductos`
--

CREATE TABLE IF NOT EXISTS `subproductos` (
  `subproducto` int(11) NOT NULL,
  `cantidad` float NOT NULL,
  `producto` int(200) NOT NULL,
  PRIMARY KEY (`subproducto`),
  KEY `fk_subproductos_productos1` (`producto`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `unidades`
--

CREATE TABLE IF NOT EXISTS `unidades` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(20) CHARACTER SET latin1 COLLATE latin1_spanish_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `unidades`
--

INSERT INTO `unidades` (`id`, `nombre`) VALUES
(1, 'PZA');

-- --------------------------------------------------------

--
-- Table structure for table `usuarios`
--

CREATE TABLE IF NOT EXISTS `usuarios` (
  `id_usuario` int(20) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) COLLATE latin1_spanish_ci NOT NULL,
  `usuario` varchar(50) COLLATE latin1_spanish_ci NOT NULL,
  `clave` varchar(50) COLLATE latin1_spanish_ci NOT NULL,
  `nivel` tinyint(4) NOT NULL,
  PRIMARY KEY (`id_usuario`),
  UNIQUE KEY `usuario_UNIQUE` (`usuario`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci AUTO_INCREMENT=3 ;

--
-- Dumping data for table `usuarios`
--

INSERT INTO `usuarios` (`id_usuario`, `nombre`, `usuario`, `clave`, `nivel`) VALUES
(1, 'Usuario', 'user', 'd41d8cd98f00b204e9800998ecf8427e', 1),
(2, 'Administrador', 'admin', '1ddff545424249df81f3c4ab552dbb3d', 5);

-- --------------------------------------------------------

--
-- Table structure for table `vendidos`
--

CREATE TABLE IF NOT EXISTS `vendidos` (
  `venta` int(12) NOT NULL,
  `producto` int(200) NOT NULL,
  `tipo` tinyint(1) NOT NULL,
  `cantidad` float NOT NULL,
  `total` float NOT NULL,
  PRIMARY KEY (`venta`,`producto`,`tipo`),
  KEY `fk_vendidos_productos1` (`producto`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `ventas`
--

CREATE TABLE IF NOT EXISTS `ventas` (
  `fecha` date NOT NULL,
  `subtotal` float unsigned NOT NULL,
  `descuentos` float unsigned NOT NULL,
  `total` float unsigned NOT NULL,
  `efectivo` float unsigned NOT NULL,
  PRIMARY KEY (`fecha`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
