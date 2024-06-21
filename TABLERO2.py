from PySide2.QtCore import Qt,QCoreApplication
from PySide2 import QtWidgets
from PySide2.QtWidgets import QWidget,QApplication,QTableWidgetItem,QMessageBox,QMainWindow
from Imports.imp_Tablero import Ui_MainWindow
import pyodbc
class Tablucho(QMainWindow):
    def __init__(self,User=""):
        
        self.User=User
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ProductoComprado = ""
        self.intento = True
        self.sumas = 0
        self.modified_values = []
        self.conn = pyodbc.connect('DRIVER={SQL Server};'
                            'SERVER=DESKTOP-BLVHCB2;'
                            'DATABASE=Prueba1;'
                            'Trusted_Connection=yes;')
        #self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)   #Vuleve tranparente la parte de arriba
        #self.setAttribute(Qt.WA_TranslucentBackground)
        self.resize(828, 506)
        self.ui.stackedWidget.setFixedSize(695, 429)
        self.ui.tableWidget.setColumnWidth(1, 130)

        self.productos = []
        #self.ui.boton_minimizar.clicked.connect(self.Minimizar)
        #self.ui.boton_eliminar.clicked.connect(self.Salir)
        self.ui.btn_Actualizar.clicked.connect(self.Actualizar)
        self.ui.BOTON_TABLA.clicked.connect(self.mostrar_pagina_tabla)
        self.ui.BOTON_rEGISTRAR.clicked.connect(self.mostrar_pagina_registrar)
        self.ui.BOTON_ACTUALIZAR.clicked.connect(self.mostrar_pagina_actualizar)
        self.ui.BOTON_eLIMINAR.clicked.connect(self.mostrar_pagina_eliminar)

        self.ui.BOTON_ACTUALIZAR_3.clicked.connect(self.actualizar_producto)
        self.ui.BOTON_BUSCAR_3.clicked.connect(self.Actualizar_Buscar)
        
        
        self.ui.push.clicked.connect(self.Agregar)
        self.ui.Btn_Eliminar.clicked.connect(self.Eliminar)
        self.ui.Btn_Siguiente.clicked.connect(self.Siguiente)
        self.ui.Btn_Barcode.clicked.connect(self.Barcode)
        
        self.RestacodProductos =[]
        self.RestaCantidad = []
        
        # BOLETA
        self.BO_Productos=[]
        self.BO_Precios =[]
        self.BO_Cantidad=[]
        self.BO_PREUNI=[]

        # Variables adicionales
        self.alfa = 0
        self.vueltas= 0
        self.totales = 0
        self.indice_seleccionado = -1

    def mostrar_pagina_tabla(self):

        # Crear un cursor para ejecutar consultas SQL
        cursor = self.conn.cursor()
        cursor.execute("SELECT ID_producto, nombre, precio_unitario FROM Producto ")
        self.ui.stackedWidget.setCurrentWidget(self.ui.pagina1)

        self.ui.tableWidget.cellClicked.connect(self.registrar_seleccion)

        #Sustraccion de productos comprados
        """
        self.RestacodProductos =[]
        self.RestaCantidad = []
        """
        # Datos de productos
        filas = cursor.fetchall()
        self.ListaProductos = []
        self.PreciosProductos = []
        self.CodigoProductos = []
        for fila in filas:
            id_producto, nombre_producto, precio_unitario = fila
            self.CodigoProductos.append(id_producto)
            self.ListaProductos.append(nombre_producto)
            self.PreciosProductos.append(float(precio_unitario))
        """# BOLETA
        self.BO_Productos=[]
        self.BO_Precios =[]
        self.BO_Cantidad=[]
        self.BO_PREUNI=[]

        # Variables adicionales
        self.alfa = 0
        self.vueltas= 0
        self.totales = 0
        self.indice_seleccionado = -1"""
    def Agregar(self):
        
        self.indice = -1
        row_total = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.removeRow(row_total - 1) 
        #self.ui.tableWidget.removeRow(self.indice_seleccionado)
        # CARGA EL PRODUCTO CON EL VALOR DE R.BUTTON
        if self.ui.Btn_1.isChecked() == True: self.indice = 0
        elif self.ui.Btn_2.isChecked() == True:self.indice = 1
        elif self.ui.Btn_3.isChecked() == True:self.indice = 2
        elif self.ui.Btn_4.isChecked() == True:self.indice = 3
        elif self.ui.Btn_5.isChecked() == True:self.indice = 4
        elif self.ui.Btn_6.isChecked() == True:self.indice = 5
        elif self.ui.Btn_7.isChecked() == True:self.indice = 6
        elif self.ui.Btn_8.isChecked() == True:self.indice = 7
        elif self.ui.Btn_9.isChecked() == True:self.indice = 8
        elif self.ui.Btn_10.isChecked() == True:self.indice = 9
        elif self.ui.Btn_11.isChecked() == True:self.indice = 10
        elif self.ui.Btn_12.isChecked() == True:self.indice = 11
        else: self.indice = -1 
        # Con el indice carga el precio dentro de precio
        self.codigo = self.CodigoProductos[self.indice]
        self.Producto = self.ListaProductos[self.indice]
        self.Precio = self.PreciosProductos[self.indice]
        self.Cantidad = self.ui.spinBox.value()
        self.subtotal = float(self.Cantidad * self.Precio)
        self.totales += self.subtotal

        #Resta Productos
        self.RestacodProductos.append(self.codigo)
        self.RestaCantidad.append(self.Cantidad)



            # Boleta
        self.BO_Productos.append(self.Producto)
        self.BO_Precios.append(self.subtotal)
        self.BO_Cantidad.append(self.Cantidad)
        self.BO_PREUNI.append(self.Precio)
        cursor = self.conn.cursor()
        a = ("select cantidad_disponible from Inventario where ID_producto = ?")
        cursor.execute(a,(self.codigo))
        stock = str(cursor.fetchall())
        limite = stock.index(",")
        stock = int(str(stock)[2:limite])
        
        if self.Producto != self.ProductoComprado and self.ProductoComprado != "":
            self.sumas=0
        self.sumas+=self.Cantidad
        if int(self.sumas) > stock:
            mensaje = QMessageBox()
            mensaje.setIcon(QMessageBox.Warning)
            mensaje.setWindowTitle("Advertencia")
            mensaje.setText(f"Producto {self.Producto} sin stock")
            mensaje.exec_()
            self.sumas -= self.Cantidad
            self.totales -= self.subtotal
            stock = 0
            
            return
            # AGREGA LOS DATOS EN LAS COLUMNAS
        else:
            self.ProductoComprado = self.Producto
        row_count = self.ui.tableWidget.rowCount()  # Función para el índice de fila
        self.ui.tableWidget.insertRow(row_count)  # Crea fila
        self.ui.tableWidget.setItem(row_count, 0, QTableWidgetItem(str(self.codigo)))
        self.ui.tableWidget.setItem(row_count, 1, QTableWidgetItem(str(self.Producto)))
        self.ui.tableWidget.setItem(row_count, 2, QTableWidgetItem(str(self.Precio)))
        self.ui.tableWidget.setItem(row_count, 3, QTableWidgetItem(str(self.Cantidad)))
        self.ui.tableWidget.setItem(row_count, 4, QTableWidgetItem(str(self.subtotal)))

            # Agrega el TOTAL 
        row_total = self.ui.tableWidget.rowCount()  # Número de fila
        self.alfa = row_total
        self.ui.tableWidget.insertRow(row_total)
        self.ui.tableWidget.setItem(row_total, 0, QTableWidgetItem("Total"))
        self.ui.tableWidget.setItem(row_total, 4, QTableWidgetItem(str(self.totales)))
    def Eliminar(self):
        if self.indice_seleccionado != -1:
            item = self.ui.tableWidget.item(self.indice_seleccionado, 3).text()
            item1 = self.ui.tableWidget.item(self.indice_seleccionado, 0).text()
            del self.RestaCantidad[self.indice_seleccionado]
            del self.RestacodProductos[self.indice_seleccionado]
            # Obtener el texto del subtotal en la celda seleccionada
            subtotal_texto = self.ui.tableWidget.item(self.indice_seleccionado, 4).text()
            valor_entero = float(subtotal_texto)
            # Restar el subtotal eliminado del total
            self.totales -= valor_entero

            del self.BO_Precios[self.indice_seleccionado]
            del self.BO_Productos[self.indice_seleccionado]
            del self.BO_Cantidad[self.indice_seleccionado]
            del self.BO_PREUNI[self.indice_seleccionado]


                # Actualizar la tabla y el total
            self.ui.tableWidget.removeRow(self.indice_seleccionado)
            row_total = self.ui.tableWidget.rowCount()

            self.ui.tableWidget.removeRow(row_total - 1)  # Eliminar la fila del total anterior
            self.ui.tableWidget.insertRow(row_total - 1)  # Insertar una nueva fila para el total
            self.ui.tableWidget.setItem(row_total - 1, 0, QTableWidgetItem("Total"))
            self.ui.tableWidget.setItem(row_total - 1, 4, QTableWidgetItem(str(self.totales)))



            if row_total == 1:
                self.ui.tableWidget.removeRow(0)
    def registrar_seleccion(self, row, column):
        self.indice_seleccionado = row
    def Siguiente(self):
        Total = self.totales
        cursor = self.conn.cursor()
        a = []
        b = []
        # Insertar datos en la tabla Cliente
        cursor.execute("SELECT cantidad_disponible, ID_producto FROM Inventario ")
        lista = cursor.fetchall()
        for i in lista:
            a1,a2 = i
            a.append(a1), b.append(a2)
        b_indices = {id: i for i, id in enumerate(b)}
        modified_values = self.modified_values

        # Iterar sobre los elementos de restaid
        for id, rest in zip(self.RestacodProductos, self.RestaCantidad):
            if id in b_indices:
                indice = b_indices[id]
                a[indice] -= rest
                modified_values.append(a[indice])
        self.modified_values = modified_values
        j=0
        
        for j in range(len(self.RestacodProductos)):
            restarenPTVENTA =("update Inventario set cantidad_disponible = ? where ID_producto = ?")
            cursor.execute(restarenPTVENTA, (str(modified_values[j]),self.RestacodProductos[j]))
            self.conn.commit()
        from Registro import Registro
        self.Main = Registro(Total, self.User, self.BO_Precios, self.BO_Productos, self.BO_Cantidad, self.BO_PREUNI)
        self.Main.show()
        self.close()
    def Datos(self):
        return self.BO_Precios, self.BO_Productos, self.BO_Cantidad, self.BO_PREUNI
    def Barcode(self):
        import cv2
        from pyzbar.pyzbar import decode
        import time
        import winsound

        def detect_and_decode_barcode(image):
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            barcodes = decode(gray)
            barcode_data = ""  # Variable para almacenar el código detectado
            for barcode in barcodes:
                barcode_data = barcode.data.decode("utf-8")
                barcode_type = barcode.type
                (x, y, w, h) = barcode.rect
                cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
                cv2.putText(image, f"{barcode_data} ({barcode_type})",
                            (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
            return image, barcode_data
        cap = cv2.VideoCapture(0)
        detected_code = ""  # Variable para almacenar el último código detectado
        last_detected_time = 0
        detection_delay = 2  # segundos de espera entre detecciones

        while True:
                ret, frame = cap.read()
                if not ret:
                    print("Error al acceder a la cámara")
                    break
                        
                frame_with_barcodes, new_detected_code = detect_and_decode_barcode(frame)      
                current_time = time.time()
                if new_detected_code and (current_time - last_detected_time > detection_delay):
                    detected_code = new_detected_code  # Actualizar el último código detectado
                    winsound.Beep(1000, 500)  # Suena un beep por cada código detectado
                    last_detected_time = current_time
                    ###
                    self.indice = -1
                    row_total = self.ui.tableWidget.rowCount()
                    self.ui.tableWidget.removeRow(row_total - 1) 

                    codeBrcode = detected_code
                    codeBrcode = str(codeBrcode[0:4])
                    print(codeBrcode)

                    if codeBrcode in self.CodigoProductos:
                        self.indice = self.CodigoProductos.index(codeBrcode)

                    # Con el indice carga el precio dentro de precio
                    self.codigo = self.CodigoProductos[self.indice]
                    self.Producto = self.ListaProductos[self.indice]
                    self.Precio = self.PreciosProductos[self.indice]
                    self.Cantidad = 1
                    self.subtotal = float(self.Cantidad * self.Precio)
                    self.totales += self.subtotal

                    #Resta Productos
                    self.RestacodProductos.append(self.codigo)
                    self.RestaCantidad.append(self.Cantidad)



                        # Boleta
                    self.BO_Productos.append(self.Producto)
                    self.BO_Precios.append(self.subtotal)
                    self.BO_Cantidad.append(self.Cantidad)
                    self.BO_PREUNI.append(self.Precio)
                    cursor = self.conn.cursor()
                    a = ("select cantidad_disponible from Inventario where ID_producto = ?")
                    cursor.execute(a,(self.codigo))
                    stock = str(cursor.fetchall())
                    limite = stock.index(",")
                    stock = int(str(stock)[2:limite])
                    
                    if self.Producto != self.ProductoComprado and self.ProductoComprado != "":
                        self.sumas=0
                    self.sumas+=self.Cantidad
                    if int(self.sumas) > stock:
                        mensaje = QMessageBox()
                        mensaje.setIcon(QMessageBox.Warning)
                        mensaje.setWindowTitle("Advertencia")
                        mensaje.setText(f"Producto {self.Producto} sin stock")
                        mensaje.exec_()
                        self.sumas -= self.Cantidad
                        self.totales -= self.subtotal
                        stock = 0
                        
                        return
                        # AGREGA LOS DATOS EN LAS COLUMNAS
                    else:
                        self.ProductoComprado = self.Producto
                    row_count = self.ui.tableWidget.rowCount()  # Función para el índice de fila
                    self.ui.tableWidget.insertRow(row_count)  # Crea fila
                    self.ui.tableWidget.setItem(row_count, 0, QTableWidgetItem(str(self.codigo)))
                    self.ui.tableWidget.setItem(row_count, 1, QTableWidgetItem(str(self.Producto)))
                    self.ui.tableWidget.setItem(row_count, 2, QTableWidgetItem(str(self.Precio)))
                    self.ui.tableWidget.setItem(row_count, 3, QTableWidgetItem(str(self.Cantidad)))
                    self.ui.tableWidget.setItem(row_count, 4, QTableWidgetItem(str(self.subtotal)))

                        # Agrega el TOTAL 
                    row_total = self.ui.tableWidget.rowCount()  # Número de fila
                    self.alfa = row_total
                    self.ui.tableWidget.insertRow(row_total)
                    self.ui.tableWidget.setItem(row_total, 0, QTableWidgetItem("Total"))
                    self.ui.tableWidget.setItem(row_total, 4, QTableWidgetItem(str(self.totales)))
                    ###
                            

                cv2.imshow('Barcode Detection', frame_with_barcodes)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

        cap.release()
        cv2.destroyAllWindows()



        

        

    def mostrar_pagina_registrar(self):
        
        self.ui.stackedWidget.setCurrentWidget(self.ui.pagina_RE)
    
    def Actualizar(self):
        #LIMPIA LA TABLA
        self.ui.tabla_inventario.clearContents()
        self.ui.tabla_inventario.setRowCount(0)


        # Crear un cursor para ejecutar consultas SQL
        cursor = self.conn.cursor()

        cursor.execute("SELECT I.ID_inventario, I.ID_producto, P.nombre, I.cantidad_disponible, P.precio_unitario FROM Inventario I INNER JOIN Producto P ON I.ID_producto = P.ID_producto")

        # Obtener todas las filas
        filas = cursor.fetchall()
        self.Lid_inventario=[]
        self.Lid_Producto=[]
        self.L_Nombre=[]
        self.Lid_cantidad=[]
        self.Lid_PrecioUni=[]
        # Imprimir los datos obtenidos
        for fila in filas:
            id_inventario, id_producto, cantidad_disponible, nombre_producto, precio_unitario = fila
            self.Lid_inventario.append(id_inventario), self.Lid_Producto.append(id_producto)
            self.L_Nombre.append(nombre_producto), self.Lid_cantidad.append(cantidad_disponible)
            self.Lid_PrecioUni.append(float(precio_unitario))

        self.ui.tabla_inventario.setRowCount(0)
        for i in range(len(self.Lid_inventario)):
            row_count = self.ui.tabla_inventario.rowCount() #FUNCION PARA INDICE DE FILA
            self.ui.tabla_inventario.insertRow(row_count) #CREA FILA
            self.ui.tabla_inventario.setItem(row_count,0,QTableWidgetItem(str(self.Lid_inventario[i])))
            self.ui.tabla_inventario.setItem(row_count,1,QTableWidgetItem(str(self.Lid_Producto[i])))
            self.ui.tabla_inventario.setItem(row_count,2,QTableWidgetItem(str(self.Lid_cantidad[i])))
            self.ui.tabla_inventario.setItem(row_count,3,QTableWidgetItem(str(self.L_Nombre[i])))
            self.ui.tabla_inventario.setItem(row_count,4, QTableWidgetItem(str(self.Lid_PrecioUni[i])))

    def mostrar_pagina_actualizar(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.pagina_Actualizar)
    def Actualizar_Buscar(self):
        if self.ui.TXT_NOMBRE_PRODUCTO_2.text() != "":
            # Crear un cursor para ejecutar consultas SQL
            cursor = self.conn.cursor()
            cursor.execute("SELECT I.ID_inventario, I.ID_producto, P.nombre, I.cantidad_disponible, P.precio_unitario FROM Inventario I INNER JOIN Producto P ON I.ID_producto = P.ID_producto")

            filas = cursor.fetchall()
            actid_inventario =[]
            ACTid_Producto=[]
            ACT_Nombre=[]
            ACTid_cantidad=[]
            ACTid_PrecioUni=[]
            for fila in filas:
                id_inventario,id_producto, cantidad_disponible, nombre_producto, precio_unitario = fila
                actid_inventario.append(id_inventario),ACTid_Producto.append(id_producto)
                ACT_Nombre.append(nombre_producto), ACTid_cantidad.append(cantidad_disponible)
                ACTid_PrecioUni.append(float(precio_unitario))

            codeProduct =self.ui.TXT_NOMBRE_PRODUCTO_2.text()

            if codeProduct in actid_inventario:
                Ind=actid_inventario.index(codeProduct)
                self.ui.label_4.setText(ACTid_Producto[Ind])
                self.ui.TXT_NOMBRE_3.setText(str(ACTid_cantidad[Ind]))
                self.ui.TXT_PRECIO_3.setText(str(ACTid_PrecioUni[Ind]))
                self.ui.TXT_CANTIDAD_2.setText(str(ACT_Nombre[Ind]))
                
                self.Verificaion = True
                
            else:
                self.Verificaion = False
                self.ui.label_17.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Producto no Encontrado</span></p></body></html>", None))


    def mostrar_pagina_eliminar(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.pagina_ELIMINAR)

    def actualizar_producto(self):
        if self.Verificaion == True:
            cursor = self.conn.cursor()
            # Crear un cursor para ejecutar consultas SQL
            codeProduct =self.ui.TXT_NOMBRE_PRODUCTO_2.text()
            code = self.ui.label_4.text()
            name = self.ui.TXT_NOMBRE_3.text()
            price = self.ui.TXT_PRECIO_3.text()
            cant = self.ui.TXT_CANTIDAD_2.text()
            try:
                price = float(price)
                cant = int(cant)
            except ValueError:
                mensaje = QMessageBox()
                mensaje.setIcon(QMessageBox.Warning)
                mensaje.setWindowTitle("Advertencia")
                mensaje.setText("Ingresa correctamente el precio y la cantidad")
                mensaje.exec_()
                self.ui.label_17.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Algo anda Mal ＞︿＜</span></p></body></html>", None))
                return
            sql_query = "UPDATE Producto SET nombre = ?, precio_unitario = ? WHERE ID_producto = ?; UPDATE Inventario SET cantidad_disponible = ? WHERE ID_inventario = ?"
            cursor.execute(sql_query, (name, price, code, cant, codeProduct))
            
            self.conn.commit()
            self.ui.label_17.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Producto Actualizado (\u25cf'\u25e1'\u25cf)</span></p></body></html>", None))
            

if __name__ == "__main__":
    
    app = QApplication()
    ventana = Tablucho()
    ventana.show()
    app.exec_()
