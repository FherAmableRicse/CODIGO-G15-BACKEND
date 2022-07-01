--VISTAS
CREATE VIEW vw_matricula_alumno AS
SELECT
a.alumno_nombre AS alumno,
n.nivel_nombre AS nivel,
m.modulo_nombre AS modulo
FROM tbl_matricula mat
INNER JOIN tbl_alumno a ON mat.alumno_id = a.alumno_id
INNER JOIN tbl_nivel n ON mat.nivel_id = n.nivel_id
INNER JOIN tbl_modulo m ON mat.modulo_id = m.modulo_id;

SELECT * FROM vw_matricula_alumno
WHERE nivel = 'BASICO'