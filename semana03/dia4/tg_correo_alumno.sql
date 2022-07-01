--TRIGGER
DELIMITER $$
DROP TRIGGER IF EXISTS tg_correo_alumno;
CREATE TRIGGER tg_correo_alumno
BEFORE INSERT
ON tbl_alumno FOR EACH ROW
BEGIN
    SET NEW.alumno_email = CONCAT(LOWER(REPLACE(NEW.alumno_nombre,' ','.')),'@codigo.edu.pe');

END
$$

DELIMITER ;

INSERT INTO tbl_alumno(alumno_nombre) VALUES('Gino Carranza');

SELECT * FROM tbl_alumno;