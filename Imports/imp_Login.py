from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.resize(362, 453)
        MainWindow.setStyleSheet(u"background-color: rgba(255, 0,0, 2);\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"border-radius: 10px;")
        self.FondoClaro = QLabel(self.centralwidget)
        self.FondoClaro.setObjectName(u"FondoClaro")
        self.FondoClaro.setGeometry(QRect(20, 20, 321, 381))
        self.FondoClaro.setStyleSheet(u"background: rgb(50, 130, 181);\n"
"border-radius: 10px;")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(100, 70, 161, 41))
        font = QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet(u"background: rgb(50, 130, 181);\n"
"color: rgb(171, 233, 255);")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(60, 140, 241, 41))
        font1 = QFont()
        font1.setFamily(u"Yu Gothic UI Light")
        font1.setPointSize(8)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(3)
        self.lineEdit.setFont(font1)
        self.lineEdit.setCursor(QCursor(Qt.IBeamCursor))
        self.lineEdit.setLayoutDirection(Qt.LeftToRight)
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"font: 25 8pt \"Yu Gothic UI Light\";")
        self.lineEdit.setMaxLength(20)
        self.lineEdit.setCursorPosition(7)
        self.lineEdit.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(60, 190, 241, 41))
        font2 = QFont()
        font2.setFamily(u"Yu Gothic UI")
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(3)
        self.lineEdit_2.setFont(font2)
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"font: 25 8pt \"Yu Gothic UI\";")
        self.lineEdit_2.setMaxLength(20)
        self.Btn_Login = QPushButton(self.centralwidget)
        self.Btn_Login.setObjectName(u"Btn_Login")
        self.Btn_Login.setGeometry(QRect(60, 260, 241, 41))
        font3 = QFont()
        font3.setFamily(u"Trebuchet MS")
        font3.setPointSize(14)
        self.Btn_Login.setFont(font3)
        self.Btn_Login.setLayoutDirection(Qt.LeftToRight)
        self.Btn_Login.setStyleSheet(u"background: rgb(187, 225, 248);\n"
"border-color: rgb(187, 225, 248);\n"
"border-radius: 10px;\n"
"color:rgb(43, 68, 85);")
        self.Btn_Salir = QPushButton(self.centralwidget)
        self.Btn_Salir.setObjectName(u"Btn_Salir")
        self.Btn_Salir.setGeometry(QRect(110, 410, 141, 23))
        font4 = QFont()
        font4.setFamily(u"Arial Rounded MT Bold")
        font4.setPointSize(10)
        self.Btn_Salir.setFont(font4)
        self.Btn_Salir.setStyleSheet(u"background-color: rgba(255, 0,0, 2);\n"
"color: rgb(171, 233, 255);")
        self.Btn_Contrasea = QToolButton(self.centralwidget)
        self.Btn_Contrasea.setObjectName(u"Btn_Contrasea")
        self.Btn_Contrasea.setGeometry(QRect(90, 310, 181, 20))
        self.Btn_Contrasea.setFont(font4)
        self.Btn_Contrasea.setStyleSheet(u"background-color: rgba(255, 0,0, 2);\n"
"border-color: rgb(50, 130, 181);\n"
"color:  rgb(171, 233, 255);")
        self.Mensaje = QLabel(self.centralwidget)
        self.Mensaje.setObjectName(u"Mensaje")
        self.Mensaje.setGeometry(QRect(60, 340, 241, 41))
        font5 = QFont()
        font5.setPointSize(10)
        font5.setBold(True)
        font5.setWeight(75)
        self.Mensaje.setFont(font5)
        self.Mensaje.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.Mensaje.setLayoutDirection(Qt.LeftToRight)
        self.Mensaje.setStyleSheet(u"background-color: rgba(255, 0,0, 2);\n"
"")
        self.Mensaje.setFrameShadow(QFrame.Plain)
        self.Mensaje.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.Mensaje.setOpenExternalLinks(False)
        self.checkBox = QCheckBox(self.centralwidget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(200, 236, 101, 21))
        self.checkBox.setStyleSheet(u"background-color: rgba(255, 0,0, 2);\n"
"border-color: rgb(50, 130, 181);\n"
"color:  rgb(171, 233, 255);")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 361, 451))
        self.frame.setStyleSheet(u"background-color: rgb(14, 76, 117);\n"
"border-radius: 20px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.raise_()
        self.FondoClaro.raise_()
        self.label.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.Btn_Login.raise_()
        self.Btn_Salir.raise_()
        self.Btn_Contrasea.raise_()
        self.Mensaje.raise_()
        self.checkBox.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.FondoClaro.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:24pt;\">Bienvenido</span></p></body></html>", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"Usuario", None))
        self.lineEdit_2.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a", None))
        self.Btn_Login.setText(QCoreApplication.translate("MainWindow", u"Ingresar", None))
        self.Btn_Salir.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
        self.Btn_Contrasea.setText(QCoreApplication.translate("MainWindow", u"\u00bfPerdiste tu contrase\u00f1a?", None))
        self.Mensaje.setText("")
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Ver Contrase\u00f1a", None))
    # retranslateUi
