--FUNCIONES DE AGRUPACION

--contar registros

SELECT COUNT(*) FROM alumno;

SELECT SUM(nota)/ COUNT(*) FROM alumno;

SELECT AVG(nota),MIN(nota), MAX(nota) FROM alumno;

SELECT MIN(pais),MAX(pais),AVG(pais) FROM alumno;

SELECT MAX(id) FROM alumno;

--GROUP BY

SELECT
    pais,
    COUNT(*) AS cantidad
FROM alumno
GROUP BY pais
ORDER BY COUNT(*) DESC;

--CREAR CONSULTA SQL QUE RETORNE LA NOTA PROMEDIO, MINIMA Y MAXIMA POR PAIS ORDENADO POR PROMEDIO MAS ALTO POR PAIS

SELECT
    pais,
    avg(nota) ASC promedio,
    min(nota) ASC minimo,
    max(nota) ASC maximo
FROM alumno
WHERE nota > 10
GROUP BY pais
HAVING avg(nota) < 16
ORDER BY avg(nota) DESC;

--

SELECT * FROM alumno;

SELECT
    pais,
    AVG(nota) as promedio
FROM alumno
WHERE nota > 10
GROUP BY pais;