
create database Prueba1
drop database Prueba1
---TIENEN QUE EJECUTAR HASTA COMPROBANTE Y SI O SI LA DATABASE DE LLAMA Prueba1----

--------------------------
-- Creación de la tabla Cliente
CREATE TABLE Cliente (
    ID_DNI CHAR(8) PRIMARY KEY,
    telefono char(9)
);

-- Creación de la tabla Producto
CREATE TABLE Producto (
    ID_producto char(4) PRIMARY KEY,
    nombre VARCHAR(50),
    precio_unitario DECIMAL(10, 2)
);

-- Creación de la tabla Empleado
CREATE TABLE Empleado (
    ID_empleado char(4) PRIMARY KEY,
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    cargo VARCHAR(25)
);
CREATE TABLE Venta (
    ID_venta char(4) PRIMARY KEY,
    ID_empleado char(4) NOT NULL,
    fecha DATE,
    Hora TIME,
    ID_DNI char(8),
    TOTAL DECIMAL(10, 2),
    FOREIGN KEY (ID_empleado) REFERENCES Empleado(ID_empleado),
    FOREIGN KEY (ID_DNI) REFERENCES Cliente(ID_DNI)
);
-- Creación de la tabla Detalle_Venta
CREATE TABLE Detalle_Venta (
    ID_dtVenta char(4) Primary key,
    Linea INT,
	ID_venta char(4),
    ID_producto char(4),
    cantidad INT,
    SUBTOTAL DECIMAL(10, 2),

	FOREIGN KEY (ID_venta) REFERENCES Venta(ID_venta),
    FOREIGN KEY (ID_producto) REFERENCES Producto(ID_producto)
); 


CREATE TABLE Proveedor (
    ID_proveedor char(5) PRIMARY KEY,
    nombre VARCHAR(50),
    telefono varchar(15),
    direccion VARCHAR(255)
);

CREATE TABLE Compra (
    ID_compra char(5) PRIMARY KEY,
    ID_proveedor char(5) NOT NULL,
    fecha date, -- Cambiado a DATE para almacenar la fecha correctamente
    total_compra DECIMAL(10, 2),
    FOREIGN KEY (ID_proveedor) REFERENCES Proveedor(ID_proveedor)
);
CREATE TABLE Cupones (
    ID_Promocion char(6) PRIMARY KEY,
    descuento DECIMAL(3, 2)
);

CREATE TABLE Detalle_Compra (
    ID_detalle_compra CHAR(4) PRIMARY KEY,
    ID_compra CHAR(5) NOT NULL,
    ID_producto CHAR(4) NOT NULL,
    cantidad INT,
    precio_unitario DECIMAL(10, 2),
    FOREIGN KEY (ID_compra) REFERENCES Compra(ID_compra),
    FOREIGN KEY (ID_producto) REFERENCES Producto(ID_producto)
);
CREATE TABLE Inventario (
    ID_inventario CHAR(4) PRIMARY KEY,
    ID_producto CHAR(4) NOT NULL,
    cantidad_disponible INT,
    FOREIGN KEY (ID_producto) REFERENCES Producto(ID_producto)
);
CREATE TABLE Pago (
    ID_pago CHAR(4) PRIMARY KEY,
    ID_DNI CHAR(8) ,
    ID_Venta CHAR(4),
	ID_Promocion char(6),
	NuevoTotal decimal(10,2)
    FOREIGN KEY (ID_DNI) REFERENCES Cliente(ID_DNI),
    FOREIGN KEY (ID_Venta) REFERENCES Venta(ID_venta),
	foreign Key (ID_Promocion) REFERENCES Cupones(ID_Promocion)
);
CREATE TABLE Forma_Pago (
    ID_forma_pago CHAR(6) PRIMARY KEY,
    nombre varCHAR(10)
);
CREATE TABLE Impuesto (
    ID_impuesto char(5) PRIMARY KEY,
    nombre VARCHAR(5),
    tasa DECIMAL(3, 2)
);
CREATE TABLE Comprobante (
    ID_Comprobante char(5) PRIMARY KEY,
    ID_venta char(4),
    ID_impuesto cHAR(5),
    ID_forma_pago CHAR(6),
    FOREIGN KEY (ID_venta) REFERENCES Venta(ID_venta),
    FOREIGN KEY (ID_impuesto) REFERENCES Impuesto(ID_impuesto),
    FOREIGN KEY (ID_forma_pago) REFERENCES Forma_Pago(ID_forma_pago)
);

INSERT INTO Cliente (ID_DNI, telefono)
VALUES ('60805652', '998745632'),
       ('87877878', '975864125'),
       ('32323123', '903258457');

Insert Into Producto (ID_producto, nombre, precio_unitario)
values	('9001','Bloqueador',10.00),
		('9002','M.blanqueador',20.00),
		('9003','L.fria',30.00),
		('9004','M.Negra',40.00),
		('9005','Serum',50.00),
		('9006','J. Facial',60.00),
		('9007','C. Anti Arrugas',70.00),
		('9008','C. Aclarador',80.00),
		('9009','C.AntiEstrias ',90.00),
		('9010','L.Desengrasante',100.00),
		('9011','L.Secativa',110.00),
		('9012','C.Hidratante',120.00)
INSERT INTO Empleado (ID_empleado, nombre, apellido, cargo) VALUES
    ('3001', 'Carlos', 'Sanchez', 'Administrador'),
    ('3002', 'Maria', 'Rodriguez', 'Caja'),
    ('3003', 'Jorge', 'Gonzales', 'Secretaria');
INSERT INTO Venta (ID_venta, ID_empleado, fecha, Hora, ID_DNI, TOTAL)
VALUES
    ('1001', '3002', '2024-04-12', '18:27:26', '60805652', 200.00),
    ('1002', '3002', '2024-04-12', '20:27:26', '87877878', 140.00);
INSERT INTO Detalle_Venta (ID_dtVenta, Linea, ID_venta, ID_producto, cantidad, SUBTOTAL)
VALUES
    ('D001', 1, '1001', '9001', 4, 40.00),
    ('D002', 2, '1001', '9003', 2, 60.00),
    ('D003', 3, '1001', '9010', 1, 100.00),
    ('D004', 1, '1002', '9003', 3, 90.00),
    ('D005', 2, '1002', '9005', 1, 50.00);
INSERT INTO Proveedor(ID_proveedor, nombre, telefono, direccion) VALUES
    ('P0001', 'Pablo', '918273645', 'Av. Proveedores 123'),
    ('P0002', 'ANA', '997755443', 'Calle de los Suministros');
INSERT INTO Compra (ID_compra, ID_proveedor, fecha, total_compra)
VALUES
    ('C4001', 'P0001', '2024-04-01', 850.00),
    ('C4002', 'P0002', '2024-04-01', 450.00);
INSERT INTO Detalle_Compra (ID_detalle_compra, ID_compra, ID_producto, cantidad, precio_unitario) VALUES
    ('5001', 'C4001', '9001', 50, 8.00),
    ('5002', 'C4002', '9002', 30, 15.00);
INSERT INTO Inventario (ID_inventario, ID_producto, cantidad_disponible)
VALUES
    ('6001', '9001', 100),
    ('6002', '9002', 100),
	('6003', '9003', 100),
	('6004', '9004', 100),
	('6005', '9005', 100),
	('6006', '9006', 100),
	('6007', '9007', 100),
	('6008', '9008', 100),
	('6009', '9009', 100),
	('6010', '9010', 100),
	('6011', '9011', 100),
	('6012', '9012', 100);

INSERT INTO Cupones (ID_promocion, descuento)
VALUES
    ('ABC123', 0.1),
    ('QWE123', 0.15),
    ('ASD123', 0.2),
    ('ZXC123', 0.3);

INSERT INTO Pago (ID_pago, ID_DNI, ID_Venta, ID_promocion, NuevoTotal)
VALUES
    ('8001', '60805652', '1001', 'ABC123', 180),
    ('8002', '87877878', '1002', 'ASD123', 160);

INSERT INTO Forma_Pago (ID_forma_pago, nombre)
VALUES
    ('FP0001', 'Efectivo'),
    ('FP0002', 'Tarjeta');

INSERT INTO Impuesto (ID_impuesto, nombre, tasa)
VALUES
    ('I0001', 'IGV', 0.18),
    ('I0002', 'ISC', 0.1);

INSERT INTO Comprobante (ID_Comprobante, ID_venta, ID_impuesto, ID_forma_pago) 
VALUES ('F0001', '1001', 'I0001', 'FP0001')


select * from Cliente
select * from Inventario
SELECT MAX(ID_Comprobante) AS Ultimo_ID_Comprobante
FROM Comprobante;


---SELECT cantidad_disponible, ID_producto FROM Inventario
select * from Venta
---update Inventario set cantidad_disponible = '95' where ID_producto = 'A010'
---update Inventario set cantidad_disponible = ? where ID_producto = ?
---SELEct * from Inventario
---UPDATE Producto SET nombre = 'name',precio_unitario = 15  WHERE ID_producto  = 'A001'; 
---update Inventario set cantidad_disponible = 101 where ID_inventario = '6001'

