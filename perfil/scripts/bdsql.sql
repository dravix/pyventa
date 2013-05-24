CREATE TABLE IF NOT EXISTS `cajas` (
  `num_caja` INTEGER NOT NULL UNIQUE PRIMARY KEY AUTOINCREMENT,
  `nombre` varchar(45)   NOT NULL,
  `maquina` varchar(15)   DEFAULT NULL,
  `saldo_inicial` float unsigned NOT NULL,
  `estado` date NOT NULL,
  `efectivo` float unsigned NOT NULL);


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
  `id` integer NOT NULL UNIQUE PRIMARY KEY AUTOINCREMENT,
  `nombre` varchar   NOT NULL,
  `rfc` varchar   NOT NULL,
  `direccion` varchar   NOT NULL,
  `poblacion` varchar   NOT NULL,
  `estado` varchar   NOT NULL,
  `tel` varchar   NOT NULL,
  `correo` varchar   NOT NULL,
  `tipo` INTEGER NOT NULL,
  `credito` float NOT NULL
   
)  ;


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
  `codigo` varchar(20)   NOT NULL,
  PRIMARY KEY (`producto``codigo`)
)   ;


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
  PRIMARY KEY (`compra``producto`)
   );


-- --------------------------------------------------------

--
-- Table structure for table `compras`
--

CREATE TABLE IF NOT EXISTS `compras` (
  `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `fecha` datetime NOT NULL,
  `proveedor` INT NOT NULL,
  `comprador` int(11) NOT NULL,
  `total` float NOT NULL);


-- --------------------------------------------------------

--
-- Table structure for table `consultas`
--

CREATE TABLE IF NOT EXISTS `consultas` (
  `id_consulta` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `titulo` varchar(100) NOT NULL,
  `descripcion` text NOT NULL,
  `query` text NOT NULL);


-- --------------------------------------------------------

--
-- Table structure for table `departamentos`
--

CREATE TABLE IF NOT EXISTS `departamentos` (
  `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `nombre` varchar(100) CHARACTER SET latin1   NOT NULL);


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
  PRIMARY KEY (`producto``inventario`)
)  ;


-- --------------------------------------------------------

--
-- Table structure for table `faltantes`
--

CREATE TABLE IF NOT EXISTS `faltantes` (
  `producto` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `usuario` int(11) NOT NULL,
  `cantidad` float NOT NULL,
  `prioridad` int(11) NOT NULL,
  `fecha` date NOT NULL);


-- --------------------------------------------------------

--
-- Table structure for table `familias`
--

CREATE TABLE IF NOT EXISTS `familias` (
  `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `nombre` varchar(100) NOT NULL,
  `departamento` int(11) NOT NULL);


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
  `num_gasto` integer NOT NULL PRIMARY KEY AUTOINCREMENT,
  `usuario` INTEGER NOT NULL,
  `caja` INTEGER NOT NULL,
  `fecha` datetime NOT NULL,
  `concepto` varchar   NOT NULL,
  `cantidad` float NOT NULL,
  PRIMARY KEY ,
  KEY `autorizado_por` 
  KEY `hecho_en` 
)  ;


-- --------------------------------------------------------

--
-- Table structure for table `impuestos`
--

CREATE TABLE IF NOT EXISTS `impuestos` (
  `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `nombre` varchar(100) CHARACTER SET latin1   NOT NULL,
  `porcentaje` float NOT NULL);


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
  `id_inventario` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `fecha` datetime NOT NULL,
  `saldo` float NOT NULL,
  `dominio` varchar(120)   DEFAULT NULL,
  `orden` varchar(20)   DEFAULT NULL,
  `estado` tinyint(4) NOT NULL,
  `auditor` int(20) NOT NULL,
  `gerente` int(20) NOT NULL);


-- --------------------------------------------------------

--
-- Table structure for table `movimientos`
--

CREATE TABLE IF NOT EXISTS `movimientos` (
  `id_movimiento` INTEGER unsigned NOT NULL PRIMARY KEY AUTOINCREMENT,
  `usuario` int(20) unsigned NOT NULL,
  `caja` int(10) NOT NULL,
  `detalle` varchar(100)   DEFAULT NULL,
  `tipo` VARCHAR(1)   NOT NULL,
  `monto` float NOT NULL,
  `fecha` datetime NOT NULL);
 --   `tipo`  ENUM('R','D','T') convertido! 

-- --------------------------------------------------------

--
-- Table structure for table `notas`
--

CREATE TABLE IF NOT EXISTS `notas` (
  `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `cliente` int(123) NOT NULL,
  `usuario` int(20) NOT NULL,
  `caja` int(11) NOT NULL,
  `total` float NOT NULL,
  `fecha` datetime NOT NULL
  `tipo` tinyint(4) NOT NULL COMMENT '0:Not);
1:Factura);
 2: Devolucion',
  `status` tinyint(4) NOT NULL COMMENT '0:sin paga);
 1:pagado, 2:en credito, 3:devolucion',
  PRIMARY KEY (`id`),
  KEY `fk_notas_clientes1` (`cliente`),
  KEY `fk_notas_usuarios1` (`usuario`),
  KEY `fk_notas_cajas1` (`caja`)
)   DEFAULT CHARSET=latin1 AUTO_INCREMENT=1);


-- --------------------------------------------------------

--
-- Table structure for table `notas_cobradas`
--

CREATE TABLE IF NOT EXISTS `notas_cobradas` (
  `id` integer NOT NULL PRIMARY KEY AUTOINCREMENT,
  `nota` INTEGER NOT NULL,
  UNIQUE KEY `nota` 
)   DEFAULT CHARSET=latin1 PRIMARY KEY AUTOINCREMENT=1);


-- --------------------------------------------------------

--
-- Table structure for table `ofertas`
--

CREATE TABLE IF NOT EXISTS `ofertas` (
  `promocion` int(11) NOT NULL,
  `conjunto` int(11) NOT NULL,
  `tipo` int(3) NOT NULL,
  PRIMARY KEY (`promocion`,`conjunto``tipo`)
)    ;


-- --------------------------------------------------------

--
-- Table structure for table `productos`
--

CREATE TABLE IF NOT EXISTS `productos` (
  `codigo` bigINTEGER NOT NULL DEFAULT '0',
  `ref` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `descripcion` varchar(100)   NOT NULL,
  `familia` int(5) DEFAULT '0',
  `costo` double NOT NULL,
  `ganancia` double NOT NULL,
  `precio` double NOT NULL,
  `stock` float DEFAULT '0',
  `unidad` int(5) NOT NULL,
  `vendidas` float NOT NULL,
  `impuesto` int(11) NOT NULL,
  `ultima_modificacion` datetime NOT NULL);


-- --------------------------------------------------------

--
-- Table structure for table `promociones`
--

CREATE TABLE IF NOT EXISTS `promociones` (
  `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `nombre` varchar(50) CHARACTER SET latin1   NOT NULL,
  `descuento` FLOAT NOT NULL,
  `inicio` date NOT NULL,
  `fin` date NOT NULL,
  `minimo` float NOT NULL,
  `maximo` FLOAT NOT NULL);


-- --------------------------------------------------------

--
-- Table structure for table `subproductos`
--

CREATE TABLE IF NOT EXISTS `subproductos` (
  `subproducto` int(11) NOT NULL,
  `cantidad` float NOT NULL,
  `producto` int(200) NOT NULL,
 
)    ;


-- --------------------------------------------------------

--
-- Table structure for table `unidades`
--

CREATE TABLE IF NOT EXISTS `unidades` (
  `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `nombre` varchar(20) CHARACTER SET latin1   NOT NULL);


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
  `id_usuario` integer NOT NULL PRIMARY KEY AUTOINCREMENT,
  `nombre` varchar   NOT NULL,
  `usuario` varchar   NOT NULL,
  `clave` varchar   NOT NULL,
  `nivel` INTEGER NOT NULL,
  UNIQUE KEY `usuario_UNIQUE` 
)   PRIMARY KEY AUTOINCREMENT=3);


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
  PRIMARY KEY (`venta`,`producto`,`tipo`)
 
)    ;


-- --------------------------------------------------------

--
-- Table structure for table `ventas`
--

CREATE TABLE IF NOT EXISTS `ventas` (
  `fecha` date NOT NULL,
  `subtotal` float unsigned NOT NULL,
  `descuentos` float unsigned NOT NULL,
  `total` float unsigned NOT NULL,
  `efectivo` float unsigned NOT NULL);

