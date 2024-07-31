
from PySide2.QtWidgets import QWidget,QApplication,QTableWidgetItem,QMessageBox
from PySide2.QtCore import Qt
from Imports.imp_Registro import Ui_MainWindow
from TABLERO2 import Tablucho
from datetime import datetime #DA LA HORA
import pyodbc
import subprocess #Abre el blc de notas

class Registro(QWidget,Ui_MainWindow):
    def __init__(self,Total,User,Precios,Productos,Cantidad,PreUni):
        
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.Total = Total
        self.User = User
        # Boleta
        self.Precios, self.Productos, self.Cantidad, self.PreUni = Precios, Productos, Cantidad, PreUni
        
        #JDAS
        self.conn = pyodbc.connect('DRIVER={SQL Server};'
                            'SERVER=DESKTOP-BLVHCB2;'
                            'DATABASE=Prueba1;'
                            'Trusted_Connection=yes;')
        self.acursor = self.conn.cursor()
        self.acursor.execute("SELECT MAX(ID_comprobante) FROM comprobante;")
        self.id_ultimoComprobante = self.acursor.fetchall()
        #id_ultimo comprobante = 
        # Conexiones de señales y ranuras
        self.ui.Btn_Atras.clicked.connect(self.Atras)
        self.ui.Btn_Salir.clicked.connect(self.Salir)
        self.ui.Btn_Calcular.clicked.connect(self.Calcular)
        self.ui.label_2.setText(f"{Total}")

        self.Descuentos = [0.10, 0.15, 0.20, 0.3]
        self.ListaCupones = ["ABC123", "QWE123", "ASD123", "ZXC123"]

        self.NumeroBoleta = 15345134141


                
        self.acursor.execute("SELECT MAX(ID_comprobante) FROM comprobante;")
        self.id_ultimoComprobante1 = str(self.acursor.fetchall())  
        dni = self.ui.Line_DNI.text()
        self.cursorda = self.conn.cursor()
        
        self.cursorda.execute("Select ID_DNI from Cliente")
        self.listacliente = self.cursorda.fetchall()
        self.listacliente = [item[0] for item in self.listacliente]

    def Calcular(self):
        Cupon = self.ui.Line_Cupon.text()
        if Cupon in self.ListaCupones:
            ind = self.ListaCupones.index(Cupon)
            self.descuento = self.Descuentos[ind]
            NewTotal = self.Total * (1 - self.descuento)
            self.ui.label_2.setText(f"{NewTotal}")
            self.newTotal = NewTotal
        else:
            self.descuento = 0
            self.newTotal = self.Total

    def Atras(self):
        self.Tablero = Tablucho()
        self.Tablero.show()
        self.close()

    def Salir(self):
  
        telefono = self.ui.Line_Tel.text()
        Indice = len(self.Precios)
        

        # FECHA Y HORA
        hora_actual = datetime.now().strftime("%H:%M:%S")
        fecha_actual = datetime.now().strftime("%Y-%m-%d")

        if self.ui.Line_Cupon.text() == "":
            self.descuento = 0
            self.newTotal = self.Total
            
        listacliente = self.listacliente
        dni = self.ui.Line_DNI.text()
        if dni not in listacliente and dni != "" and len(dni)==8:
            comandoIntgerar = ("INSERT INTO Cliente (ID_DNI, telefono) VALUES (?, ?)")
            self.cursorda.execute(comandoIntgerar,(dni,telefono))
        elif len(dni)<8:
            mensaje = QMessageBox()
            mensaje.setIcon(QMessageBox.Warning)
            mensaje.setWindowTitle("Advertencia")
            mensaje.setText("Ingresa correctamente el DNI")
            mensaje.exec_()
            return
        id_ultimoComprobante = self.id_ultimoComprobante1

        empleado = self.User
        digito = int(str(id_ultimoComprobante[4:8]))
        digito +=1
        id_ultimoComprobante = "F" + str(digito)
        codigo_rellenado = f"{id_ultimoComprobante[0]}{int(id_ultimoComprobante[1:]):04d}"

        with open(f'Comprobantes\C_{codigo_rellenado}.txt', 'w') as archivo:

            # Escribe en el archivo

            archivo.write("             Empresa de Productos de belleza        \n                      Sumaq Runakay                 \n")
            archivo.write("                   R.U.C. 999999999999              \n           Avenida Tacna Parque Central Chosica      ")
            archivo.write(f"\n                   BOLETA ELECTRONICA               ")
            archivo.write(f"\n                         {codigo_rellenado}                       ")

            archivo.write(f"\n  Fecha Emision:                             {fecha_actual}")
            archivo.write(f"\n  Hora                                         {hora_actual}\n")
            cajero = f"  Cajero                                               "
            cajero = cajero[0:len(cajero) - len(self.User)] + self.User + "  "
            archivo.write(cajero)
            archivo.write(f"\n  Doc. Identidad:                              {dni}   \n")

            archivo.write("_________________________________________________________\n\n")
            archivo.write("  Cantidad         Producto        P.Unit       TOTAL  \n")
            archivo.write("_________________________________________________________\n\n")

            def espaciador(Limite, Palabra):
                Palabra = Palabra
                for i in range(Limite):
                    if len(Palabra) == Limite: break
                    else:
                        if i % 2 == 0: Palabra += " "
                        else: Palabra = " " + Palabra
                return Palabra

            def Quitaspacio(q1, Total):
                q1 = q1[0:len(q1) - len(Total) - 3] + "S/. " + Total + "  "
                return q1

            for i in range(Indice):
                newproducto = espaciador(20, self.Productos[i])
                newCantidad = espaciador(12, str(self.Cantidad[i]))
                newPreuni = espaciador(12, str("S./ " + str(self.PreUni[i])))
                newTotal = espaciador(14, str("S./ " + str(self.Cantidad[i] * self.PreUni[i])))
                Linea = str(newCantidad + newproducto + newPreuni + newTotal)
                archivo.write(f"{Linea}\n")

            archivo.write("_________________________________________________________\n\n")

            total = f"TOTAL:                                              \n"
            total = Quitaspacio(total, str(self.Total))
            
            if self.ui.Line_Cupon.text() != "":
                descuento = f"DESCUENTO:                                          \n"
                descuento = Quitaspacio(descuento, str(self.Total * (self.descuento)))
            else:
                descuento = ""

            newTotal = f"TOTAL:                                              \n"
            newTotal = Quitaspacio(newTotal, str(self.newTotal))

            archivo.write(f"{total}\n")
            if descuento != "":
                archivo.write(f"{descuento}\n")
                archivo.write(f"{newTotal}\n")

            subprocess.Popen(["notepad.exe", f"Comprobantes\C_{codigo_rellenado}.txt"])
        
        idventa = self.conn.cursor()
        idventa.execute("SELECT MAX(ID_venta) FROM Venta;")
        idultimaVenta = str(self.acursor.fetchall())
        idultimaVenta = int(idultimaVenta[3:7])
        idultimaVenta+=1
        idultimaVenta = str(idultimaVenta)

        empleado = "3002"
        integrar = self.conn.cursor()
        comandoIntgerar = ("INSERT INTO Venta (ID_venta, ID_empleado, fecha, Hora, ID_DNI, TOTAL) VALUES (?, ?, ?, ?,?, ?)")
        self.acursor.execute(comandoIntgerar, (idultimaVenta,empleado,fecha_actual,hora_actual,dni,self.newTotal))
        self.conn.commit()

        Comprobante = ("INSERT INTO Comprobante (ID_Comprobante, ID_venta, ID_impuesto, ID_forma_pago) VALUES (?, ?, 'I0001', 'FP0001')")
        integrar.execute(Comprobante,(codigo_rellenado,idultimaVenta))
        self.conn.commit()
        self.close()
    def Total1(self):
        return self.Total
    

if __name__ == "__main__":
    
    app = QApplication()
    ventana = Registro()
    ventana.show()
    app.exec_()