CREATE TABLE Actor (
    CodiActor INT (5) PRIMARY KEY,
    Nom VARCHAR (15)
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

CREATE TABLE Genere (
    CodiGenere INT (5) PRIMARY KEY,
    Descripcio VARCHAR (15)
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


INSERT INTO Actor() VALUES
(1, '', ''),
(2, '', '');

INSERT INTO Client(DNI, Nom, Adreca, Telefon) VALUES
(4948584K, 'Xavi', 'Bon matí 48, mataró', '632417589'),
(4945872S, 'Izan', ''),
(4875236P, 'Khalid', '')

INSERT INTO Copia() VALUES
(),
();

INSERT INTO DetallFactura() VALUES
(),
();

INSERT INTO Factura() VALUES
(),
();

INSERT INTO Genere() VALUES
(),
();

INSERT INTO Interpretada() VALUES
(),
();

INSERT INTO Pelicula() VALUES
(),
();

INSERT INTO Prestec() VALUES
(),
();