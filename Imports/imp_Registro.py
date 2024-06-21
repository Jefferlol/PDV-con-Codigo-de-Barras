# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'RegistroAMHYsj.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(377, 267)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 20, 171, 31))
        self.label_3.setStyleSheet(u"Background: rgb(112, 87, 139);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"")
        self.label_3.setMargin(10)
        self.Line_DNI = QLineEdit(self.centralwidget)
        self.Line_DNI.setObjectName(u"Line_DNI")
        self.Line_DNI.setGeometry(QRect(190, 20, 171, 31))
        self.Line_DNI.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"")
        self.Line_DNI.setMaxLength(8)
        self.Line_Tel = QLineEdit(self.centralwidget)
        self.Line_Tel.setObjectName(u"Line_Tel")
        self.Line_Tel.setGeometry(QRect(190, 70, 171, 31))
        self.Line_Tel.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"")
        self.Line_Tel.setMaxLength(9)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 70, 171, 31))
        self.label_5.setStyleSheet(u"Background: rgb(112, 87, 139);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"")
        self.label_5.setMargin(10)
        self.Btn_Atras = QPushButton(self.centralwidget)
        self.Btn_Atras.setObjectName(u"Btn_Atras")
        self.Btn_Atras.setGeometry(QRect(20, 200, 101, 41))
        self.Btn_Atras.setStyleSheet(u"Background: rgb(112, 87, 139);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.Btn_Salir = QPushButton(self.centralwidget)
        self.Btn_Salir.setObjectName(u"Btn_Salir")
        self.Btn_Salir.setGeometry(QRect(260, 200, 101, 41))
        self.Btn_Salir.setStyleSheet(u"Background: rgb(112, 87, 139);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.Line_Cupon = QLineEdit(self.centralwidget)
        self.Line_Cupon.setObjectName(u"Line_Cupon")
        self.Line_Cupon.setGeometry(QRect(190, 120, 171, 31))
        self.Line_Cupon.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"")
        self.Line_Cupon.setMaxLength(10)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 120, 171, 31))
        self.label_6.setStyleSheet(u"Background: rgb(112, 87, 139);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"")
        self.label_6.setMargin(10)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 160, 171, 21))
        self.label_7.setStyleSheet(u"Background: rgb(112, 87, 139);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"")
        self.label_7.setMargin(1)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(180, 160, 181, 31))
        self.label_2.setStyleSheet(u"border-color: rgb(85, 85, 127);\n"
"font: 87 14pt \"Arial Black\";")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.Btn_Calcular = QPushButton(self.centralwidget)
        self.Btn_Calcular.setObjectName(u"Btn_Calcular")
        self.Btn_Calcular.setGeometry(QRect(140, 200, 101, 41))
        self.Btn_Calcular.setStyleSheet(u"Background: rgb(112, 87, 139);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"   DNI", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"   Telefono", None))
        self.Btn_Atras.setText(QCoreApplication.translate("MainWindow", u"Atras", None))
        self.Btn_Salir.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"   Cupon", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"     Total", None))
        self.label_2.setText("")
        self.Btn_Calcular.setText(QCoreApplication.translate("MainWindow", u"Calcular", None))
    # retranslateUi

