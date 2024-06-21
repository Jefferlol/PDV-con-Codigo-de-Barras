
from PySide2.QtWidgets import QWidget,QApplication
from PySide2.QtCore import Qt

from Imports.imp_Login import Ui_MainWindow  

from TABLERO2 import Tablucho

class MainWindow(QWidget,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self) 

        self.ui.Btn_Login.clicked.connect(self.Login)
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)   #Vuleve tranparente la parte de arriba
        self.setAttribute(Qt.WA_TranslucentBackground)

        #Color transparente = background-color: rgba(255, 0,0, 2);
        self.ui.Btn_Salir.clicked.connect(self.Salir)
        self.ui.Btn_Contrasea.clicked.connect(self.Perdida)
        self.ui.checkBox.clicked.connect(self.Boton)

        self.ui.lineEdit.mousePressEvent = self.clear_text
        #           Fn para cuando le das click al LineEdit ;)
        self.ui.lineEdit_2.mousePressEvent=self.clear_text1
    def Boton(self):
        if self.ui.checkBox.isChecked() == False and self.ui.lineEdit_2.text() != "Contraseña":
            self.ui.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255); font: 8pt Wingdings 2;")
        else:
            a = self.ui.lineEdit_2.text()
            self.ui.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);\nfont: 25 8pt Yu Gothic UI;")
            self.ui.lineEdit_2.setText(a)

    def Login(self):
        User = self.ui.lineEdit.text()
        Password = self.ui.lineEdit_2.text()
        if User == "Jefferson" and Password == "12345":
            self.ui.Mensaje.setStyleSheet("color: black; background-color: rgba(255, 0,0, 2);")
            self.ui.Mensaje.setText("Session Iniciada :D ")
            self.close()
            self.Main = Tablucho()
            self.Main.show()
        else:
            # SetStyleSheet es igual a HojaDeEstilos :D
            self.ui.Mensaje.setStyleSheet("color: red; background-color: rgba(255, 0,0, 2);")
            self.ui.Mensaje.setText("Usuario o contraseña incorrecta")
            self.ui.lineEdit.setText("Usuario")
            self.ui.lineEdit_2.setText("Contraseña")

    def Perdida(self):
        self.ui.Mensaje.setText("Contacte con el servicio al cliente:\n +51 987 654 321")
        self.ui.lineEdit.setText("")
        self.ui.lineEdit_2.setText("")

    def Salir(self):
        self.close()

    def clear_text(self, event):
        if self.ui.lineEdit.text() == "Usuario":
            self.ui.lineEdit.setText("")
            self.ui.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);font: 8pt Yu Gothic UI;")
        if self.ui.lineEdit_2.text() == "":
            self.ui.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);\nfont: 25 8pt Yu Gothic UI;")
            self.ui.lineEdit_2.setText("Contraseña")

    def clear_text1(self, event):
        if self.ui.lineEdit_2.text() == "Contraseña" and self.ui.checkBox.isChecked() == False:
            self.ui.lineEdit_2.setText("")
            self.ui.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255); font: 8pt Wingdings 2;")

        if self.ui.lineEdit.text() == "":
            self.ui.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\nfont: 25 8pt Yu Gothic UI;")
            self.ui.lineEdit.setText("Usuario")
            

if __name__ == "__main__":
    
    app = QApplication()
    ventana = MainWindow()
    ventana.show()
    app.exec_()