#EJERCICIO 1: Empresa

CREATE TABLE DEPT (
    DEPT_NO TINYINT(2) PRIMARY KEY,
    DNOM VARCHAR(14),
    LOC VARCHAR(14)
);

CREATE TABLE  PRODUCTE (
    PROD_NUM INT(6) PRIMARY KEY,
    DESCRIPCIO VARCHAR(30)
);

CREATE TABLE CLIENT (
    CLIENT_COD INT(6) PRIMARY KEY,
    NOM VARCHAR(45),
    ADRECA VARCHAR(40),
    CIUTAT VARCHAR(30),
    ESTAT VARCHAR(2),
    CODI_POSTAL VARCHAR(9),
    AREA SMALLINT(3),
    TELEFON VARCHAR(9),
    REPR_COD SMALLINT(4),
    LIMIT_CREDIT DECIMAL(9,2),
    OBSERVACIONS TEXT
);

CREATE TABLE EMP (
    EMP_NO SMALLINT(4) PRIMARY KEY,
    COGNOM VARCHAR(10),
    OFICI VARCHAR(10),
    CAP SMALLINT(4),
    DATA_ALTA DATE,
    SALARI INT,
    COMISSIO INT,
    DEPT_NO TINYINT(2),
    FOREIGN KEY (DEPT_NO) REFERENCES DEPT(DEPT_NO)
);

CREATE TABLE DETALL (
    DETALL_NUM SMALLINT(4) PRIMARY KEY,
    PREU_VENDA DECIMAL(8,2),
    QUANTITAT INT(8),
    IMPORT DECIMAL(8,2),
    COM_NUM SMALLINT(4),
    PROD_NUM INT(6),
    FOREIGN KEY (COM_NUM) REFERENCES COMANDA(COM_NUM),
    FOREIGN KEY (PROD_NUM) REFERENCES PRODUCTE(PROD_NUM) 
);

CREATE TABLE COMANDA (
    COM_NUM SMALLINT(4) PRIMARY KEY,
    COM_DATA DATE,
    CLIENT_COD INT(6),
    COM_TIPUS CHAR(1),
    DATA_TRAMESA DATE,
    TOTAL DECIMAL(8,2),
    FOREIGN KEY (CLIENT_COD) REFERENCES CLIENT (CLIENT_COD)
);


INSERT INTO DEPT(DEPT_NO, DNOM, LOC) VALUES
(1, 'AQUARIUSITO', 'MARRUECOS'),
(2, 'ESCOBADERO', 'ANTARTIDA');

INSERT INTO PRODUCTE(PROD_NUM, DESCRIPCIO) VALUES
(01, 'AQUARIUS'),
(02, 'ESCOBA');

INSERT INTO CLIENT() VALUES
(),
();


INSERT INTO EMP() VALUES
(),
();

INSERT INTO DETALL() VALUES
(),
();

INSERT INTO COMANDA() VALUES
(),
();




#EJERCICIO 2: VideoClub




CREATE TABLE Actor (
    CodiActor INT (5) PRIMARY KEY,
    Nom VARCHAR (15)
);

CREATE TABLE Genere (
    CodiGenere INT (5) PRIMARY KEY,
    Descripcio VARCHAR (15)
);

CREATE TABLE Pelicula (
    CodiPeli INT (5) PRIMARY KEY,
    Titol VARCHAR(15),
    CodiGenere INT (5),
    SegonaPart INT (5),
    CodiActor INT (5),
    FOREIGN KEY (CodiGenere) REFERENCES Genere (CodiGenere),
    FOREIGN KEY (CodiActor) REFERENCES Actor (CodiActor)
);

CREATE TABLE Client (
    DNI CHAR (10) PRIMARY KEY,
    Nom VARCHAR (20),
    Adreca VARCHAR (20),
    Telefon CHAR (9)
);

CREATE TABLE Factura (
    CodiFactura INT (5) PRIMARY KEY,
    Data DATE,
    Import DECIMAL (9,2),
    DNI CHAR (10)
);

CREATE TABLE DetallFactura (
    CodiFactura INT (5),
    LiniaFactura INT (5) PRIMARY KEY,
    Descripcio VARCHAR (15),
    PreuUnitari DECIMAL(9,2),
    NumeroUnitats INT (5),
    FOREIGN KEY (CodiFactura) REFERENCES Factura (CodiFactura)
);

CREATE TABLE Copia (
    CodiPeli INT (5),
    CodiCopia INT (5) PRIMARY KEY,
    FOREIGN KEY (CodiPeli) REFERENCES Pelicula (CodiPeli)
);

CREATE TABLE Interpretada (
    CodiPeli INT (5),
    CodiActor INT(5),
    FOREIGN KEY (CodiPeli) REFERENCES Pelicula (CodiPeli),
    FOREIGN KEY (CodiActor) REFERENCES Actor (COdiActor)
);

CREATE TABLE Prestec (
    CodiPeli INT (5),
    CodiCopia INT (5),
    Data DATE,
    DNI CHAR (10),
    PRIMARY KEY (CodiPeli, CodiCopia, Data),
    FOREIGN KEY (CodiPeli) REFERENCES Pelicula (CodiPeli),
    FOREIGN KEY (CodiCopia) REFERENCES Copia (CodiCopia)    
);


INSERT INTO Copia(CodiPeli, CodiCopia) VALUES 
(11, 1), 
(12, 2), 
(13, 3), 
(14, 4), 
(15, 5), 
(16, 6);

INSERT INTO DetallFactura(CodiFactura, LineaFactura, Descripcio, PreuUnitari, NumeroUnitats) VALUES
(),
(),
(),
(),
(),
();

INSERT INTO Interpretada(CodiPeli, CodiActor) VALUES
(11, 1),
(12, 2),
(13, 3),
(14, 4),
(15, 5),
(16, 6);

INSERT INTO Prestec(CodiPeli, CodiCopia, Data, DNI) VALUES
(11, 1, '2023-03-12', '4948584K'),
(12, 2, '2023-06-13', '4945872S'),
(13, 3, '2023-05-16', '4875236P'),
(14, 4, '2023-03-19', '4948585K'),
(15, 5, '2023-01-25', '4945873S'),
(16, 6, '2023-10-01', '4875237P');

INSERT INTO Pelicula(CodiPeli, Titol, CodiGenere, SegonaPart, CodiActor) VALUES 
(11, 'Tony',1, 0, 1), 
(12, 'Pelao', 2, 0, 2), 
(13, 'El Rey', 3, 0, 3), 
(14, 'Terror', 4, 0, 4), 
(15, 'Futuro', 5, 0, 5), 
(16, 'Retorno', 2, 1, 6);

INSERT INTO Factura(CodiFactura, Data, Import, DNI) VALUES
(1, '2022-01-03', 12, '4948584K'),
(2, '2022-01-04', 15, '4945872S'),
(3, '2022-01-05', 10, '4875236P'),
(4, '2022-01-06', 05, '4948585K'),
(5, '2022-01-07', 50, '4945873S'),
(6, '2022-01-08', 20, '4875237P');

INSERT INTO Genere(CodiGenere, Descripcio) VALUES
(1, 'Aventura'),
(2, 'Comèdia'),
(3, 'Drama'),
(4, 'Terror'),
(5, 'Ciència-ficció');

INSERT INTO Actor(CodiActor, Nom) VALUES  
(1, 'Xavier'),  
(2, 'Izan'),  
(3, 'Khalid'),  
(4, 'Alice'),  
(5, 'Bob'),  
(6, 'Carol');

INSERT INTO Client(DNI, Nom, Adreca, Telefon) VALUES  
('4948584K', 'Xavi', 'Bon mat', '632417589'),  
('4945872S', 'Izan', 'C de la Pau', '632417589'),  
('4875236P', 'Khalid', 'C de la Llibertat', '632417589'),  
('4948585K', 'Alice', 'C de la Indstria', '632417589'),  
('4945873S', 'Bob', 'C de la Ciutat', '632417589'),  
('4875237P', 'Carol', 'C. de la Cultura', '632417589');
