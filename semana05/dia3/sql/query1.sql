

INSERT INTO `tbl_categoria` (`categoria_id`, `categoria_nom`) VALUES
	(1, 'BEBIDAS'),
	(2, 'COMBOS'),
	(3, 'PIQUEOS');

INSERT INTO `tbl_plato` (`plato_id`, `plato_nom`, `plato_img`, `plato_pre`, `categoria_id`) VALUES
	(1, 'ANTICUCHOS', 'image/upload/v1657767778/cnf1lc7ctwd4rbmti1ya.jpg', 15.00, 3),
	(2, 'YUQUITAS FRITAS', 'image/upload/v1657767796/aei24rfolzvgpyjmtaki.jpg', 10.00, 3),
	(3, 'LOMO SALTADO', 'image/upload/v1657767864/xa11rbx7whfdlvdrgwwm.jpg', 16.00, 2),
	(4, 'DESAYUNO CRIOLLO', 'image/upload/v1657767962/nhla8dpnc7f64cplrekh.png', 20.00, 2),
	(5, 'INKA KOLA', 'image/upload/v1657768028/myvqimm4epqrgcd3jxoh.jpg', 7.00, 1),
	(6, 'ARROZ CHAUFA', 'image/upload/v1657771504/b8jgmetyusbycae0cnof.jpg', 15.00, 2);

INSERT INTO `tbl_mesa` (`mesa_id`, `mesa_nro`, `mesa_cap`) VALUES
	(4, '1', 5);

