\c postgres
DROP DATABASE IF EXISTS sql1;
CREATE DATABASE sql1;
\c sql1;

CREATE TABLE prueba(
    id serial,
    nombre varchar(50),
    dni integer
);

INSERT INTO prueba(nombre,dni) VALUES('samuca',42443064);
INSERT INTO prueba(nombre,dni) VALUES('chuck',22738308);


SELECT * 
FROM 
    prueba
;