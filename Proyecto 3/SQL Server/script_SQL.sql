create database Proyecto3Aplicada
use Proyecto3Aplicada

create table Cliente  (
	ID_Cliente	int identity(1,1) NOT NULL constraint CLIENTE_PK PRIMARY KEY,
	nombre		VARCHAR(50),
	apellido	VARCHAR(50),
	edad		INT,
	genero		VARCHAR(50),
	dirección	VARBINARY(MAX)
);

create table Tarjeta  (
	ID_Tarjeta	int identity(1,1) NOT NULL constraint TARJETA_PK PRIMARY KEY,
	tipo		VARCHAR(50),
	numero		VARBINARY(MAX),
	monto		VARBINARY(MAX),
	moneda		VARCHAR(50),
);

create table Cliente_Tarjeta  (
	ID_Cliente	int not null,
	ID_Tarjeta	int not null unique,
	primary key(ID_Cliente,ID_Tarjeta),
	foreign key (ID_Cliente) references Cliente(ID_Cliente)ON DELETE Cascade ON UPDATE CASCADE, 
	foreign key (ID_Tarjeta) references Tarjeta(ID_Tarjeta)ON DELETE Cascade ON UPDATE CASCADE,
);

create table Compra  (
	ID_Compra	int identity(1,1) NOT NULL constraint COMPRA_PK PRIMARY KEY,
	monto		VARCHAR(50),
	fecha		DATE
);

create table Cliente_Compra (
	ID_Cliente	int not null,
	ID_Compra	int not null unique,
	primary key(ID_Cliente,ID_Compra),
	foreign key (ID_Cliente) references Cliente(ID_Cliente)ON DELETE Cascade ON UPDATE CASCADE, 
	foreign key (ID_Compra) references Compra(ID_Compra)ON DELETE Cascade ON UPDATE CASCADE,
);

create table Cliente_Telefono (
	ID_Cliente	int not null,
	telefono 	VARBINARY(MAX),
	primary key(ID_Cliente),
	foreign key (ID_Cliente) references Cliente(ID_Cliente)ON DELETE Cascade ON UPDATE CASCADE,
);

create table Cliente_Correo (
	ID_Cliente	int not null,
	correo 	VARBINARY(MAX),
	primary key(ID_Cliente),
	foreign key (ID_Cliente) references Cliente(ID_Cliente)ON DELETE Cascade ON UPDATE CASCADE,
);

select * from Cliente;
select * from Tarjeta;
select * from Cliente_Tarjeta;
select * from Compra;
select * from Cliente_Compra;
select * from Cliente_Telefono;
select * from Cliente_Correo;



/*drop table */
drop table Cliente_Correo
drop table Cliente_Telefono
drop table Cliente_Compra
drop table Compra
drop table Cliente_Tarjeta
drop table Tarjeta
drop table Cliente


/*SECCION SOBRE LA ENCRIPTACION*/
SELECT *
FROM master.sys.symmetric_keys AS SK
WHERE SK.name = '##MS_ServiceMasterKey##'

/*Crear clave maestra*/
CREATE MASTER KEY ENCRYPTION BY PASSWORD = 'clave123456789';
GO

/*Crear certificado*/
CREATE CERTIFICATE CertificadoProyectoAplicada   
   WITH SUBJECT = 'Protect Data';  
GO 

/*Create clave simetrica*/
create symmetric key ClaveSimetricaProyectoAplicada
	with algorithm = AES_128
	Encryption by certificate CertificadoProyectoAplicada;
	go


GO
OPEN SYMMETRIC KEY ClaveSimetricaProyectoAplicada  
   DECRYPTION BY CERTIFICATE CertificadoProyectoAplicada;
   GO
insert into Cliente  (nombre, apellido, edad, genero, dirección) values ('Shaine', 'Frostdick', 1, 'M', EncryptByKey(Key_GUID('ClaveSimetricaProyectoAplicada'), 'Logan'));
GO
CLOSE SYMMETRIC KEY ClaveSimetricaProyectoAplicada
	SELECT*FROM Cliente


/*select desencriptado*/
	GO
OPEN SYMMETRIC KEY ClaveSimetricaProyectoAplicada  
   DECRYPTION BY CERTIFICATE CertificadoProyectoAplicada;
   GO
	select nombre, apellido, edad, genero,CONVERT(varchar, DecryptByKey(dirección)) as dirección from Cliente
	GO
CLOSE SYMMETRIC KEY ClaveSimetricaProyectoAplicada

/*Procedures 1*/
CREATE PROCEDURE SP_OBTENER_Cliente_Correo
AS
BEGIN
	SET NOCOUNT ON;
	OPEN SYMMETRIC KEY ClaveSimetricaProyectoAplicada 
	DECRYPTION BY CERTIFICATE CertificadoProyectoAplicada;
	SELECT ID_Cliente,CONVERT(varchar, DecryptByKey(correo)) as correo FROM Cliente_Correo
	CLOSE SYMMETRIC KEY ClaveSimetricaProyectoAplicada
END 
GO

EXECUTE [dbo].[SP_OBTENER_Cliente_Correo]

/*Procedures 2*/
CREATE PROCEDURE SP_OBTENER_Cliente_Telefono
AS
BEGIN
	SET NOCOUNT ON;
	OPEN SYMMETRIC KEY ClaveSimetricaProyectoAplicada 
	DECRYPTION BY CERTIFICATE CertificadoProyectoAplicada;
	SELECT ID_Cliente,CONVERT(varchar, DecryptByKey(telefono)) as telefono FROM Cliente_Telefono
	CLOSE SYMMETRIC KEY ClaveSimetricaProyectoAplicada
END 
GO

EXECUTE [dbo].[SP_OBTENER_Cliente_Telefono] 

/*Procedures 3*/
CREATE PROCEDURE SP_OBTENER_Cliente_Compra
AS
BEGIN
	SET NOCOUNT ON;
	SELECT ID_Cliente, ID_Compra FROM Cliente_Compra
END 
GO

EXECUTE [dbo].[SP_OBTENER_Cliente_Compra]

/*Procedures 4*/
CREATE PROCEDURE SP_OBTENER_Compra
AS
BEGIN
	SET NOCOUNT ON;
	SELECT ID_Compra, monto, fecha FROM Compra
END 
GO

EXECUTE [dbo].[SP_OBTENER_Compra]

/*Procedures 5*/
CREATE PROCEDURE SP_OBTENER_Cliente_Tarjeta
AS
BEGIN
	SET NOCOUNT ON;
	SELECT ID_Cliente, ID_Tarjeta	FROM Cliente_Tarjeta
END 
GO

EXECUTE [dbo].[SP_OBTENER_Cliente_Tarjeta] 

/*Procedures 6*/
CREATE PROCEDURE SP_OBTENER_Tarjeta
AS
BEGIN
	SET NOCOUNT ON;
	OPEN SYMMETRIC KEY ClaveSimetricaProyectoAplicada 
	DECRYPTION BY CERTIFICATE CertificadoProyectoAplicada;
	SELECT ID_Tarjeta, tipo,CONVERT(varchar, DecryptByKey(numero)) as numero,CONVERT(varchar, DecryptByKey(monto)) as monto , moneda FROM Tarjeta
	CLOSE SYMMETRIC KEY ClaveSimetricaProyectoAplicada
END 
GO

EXECUTE [dbo].[SP_OBTENER_Tarjeta]

/*Procedures 7*/
CREATE PROCEDURE SP_OBTENER_CLIENTES
AS BEGIN
	SET NOCOUNT ON;
	OPEN SYMMETRIC KEY ClaveSimetricaProyectoAplicada 
	DECRYPTION BY CERTIFICATE CertificadoProyectoAplicada;
	SELECT ID_Cliente,nombre,apellido,edad,genero,CONVERT(varchar, DecryptByKey(dirección)) as dirección FROM Cliente
	CLOSE SYMMETRIC KEY ClaveSimetricaProyectoAplicada
END 
GO

EXECUTE [dbo].[SP_OBTENER_CLIENTES] 