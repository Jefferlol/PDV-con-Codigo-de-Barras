# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'posibletablerolIHTdC.ui'
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
        MainWindow.resize(860, 506)
        MainWindow.setStyleSheet(u"background-color: rgb(170, 170, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(150, 0))
        self.frame.setMaximumSize(QSize(100, 16777215))
        self.frame.setStyleSheet(u"\n"
"background-color: rgb(170, 170, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.BOTON_TABLA = QPushButton(self.frame)
        self.BOTON_TABLA.setObjectName(u"BOTON_TABLA")
        self.BOTON_TABLA.setStyleSheet(u"border-radius: 10px; background: rgb(240, 209, 234);")
        icon = QIcon()
        icon.addFile(u"Fotos/principal/ximi (6).png", QSize(), QIcon.Normal, QIcon.Off)
        self.BOTON_TABLA.setIcon(icon)
        self.BOTON_TABLA.setIconSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.BOTON_TABLA)

        self.BOTON_rEGISTRAR = QPushButton(self.frame)
        self.BOTON_rEGISTRAR.setObjectName(u"BOTON_rEGISTRAR")
        self.BOTON_rEGISTRAR.setStyleSheet(u"border-radius: 10px; background: rgb(240, 209, 234)")
        icon1 = QIcon()
        icon1.addFile(u"Fotos/principal/registro.png", QSize(), QIcon.Normal, QIcon.Off)
        self.BOTON_rEGISTRAR.setIcon(icon1)
        self.BOTON_rEGISTRAR.setIconSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.BOTON_rEGISTRAR)

        self.BOTON_ACTUALIZAR = QPushButton(self.frame)
        self.BOTON_ACTUALIZAR.setObjectName(u"BOTON_ACTUALIZAR")
        self.BOTON_ACTUALIZAR.setStyleSheet(u"border-radius: 10px; background: rgb(240, 209, 234)")
        icon2 = QIcon()
        icon2.addFile(u"Fotos/principal/ximi (13).png", QSize(), QIcon.Normal, QIcon.Off)
        self.BOTON_ACTUALIZAR.setIcon(icon2)
        self.BOTON_ACTUALIZAR.setIconSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.BOTON_ACTUALIZAR)

        self.BOTON_eLIMINAR = QPushButton(self.frame)
        self.BOTON_eLIMINAR.setObjectName(u"BOTON_eLIMINAR")
        self.BOTON_eLIMINAR.setStyleSheet(u"border-radius: 10px; background: rgb(240, 209, 234)")
        icon3 = QIcon()
        icon3.addFile(u"Fotos/principal/ximi (12).png", QSize(), QIcon.Normal, QIcon.Off)
        self.BOTON_eLIMINAR.setIcon(icon3)
        self.BOTON_eLIMINAR.setIconSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.BOTON_eLIMINAR)


        self.horizontalLayout.addWidget(self.frame)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setEnabled(True)
        self.frame_3.setStyleSheet(u"background-color: rgb(170, 170, 255);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_3)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgb(170, 170, 255);\n"
"")
        self.pagina1 = QWidget()
        self.pagina1.setObjectName(u"pagina1")
        self.pagina1.setStyleSheet(u"background-color: rgb(170, 170, 255);")
        self.Btn_Barcode = QPushButton(self.pagina1)
        self.Btn_Barcode.setObjectName(u"Btn_Barcode")
        self.Btn_Barcode.setGeometry(QRect(470, 350, 221, 30))
        self.Btn_Barcode.setMinimumSize(QSize(120, 30))
        font = QFont()
        font.setFamily(u"Fixedsys")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Btn_Barcode.setFont(font)
        self.Btn_Barcode.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.Btn_3 = QRadioButton(self.pagina1)
        self.Btn_3.setObjectName(u"Btn_3")
        self.Btn_3.setGeometry(QRect(620, 40, 51, 51))
        self.Btn_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon4 = QIcon()
        icon4.addFile(u"Fotos/pngtree-perfume-vector-illustration-in-hand-drawn-style-png-image_2897181.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_3.setIcon(icon4)
        self.Btn_3.setIconSize(QSize(48, 48))
        self.Btn_7 = QRadioButton(self.pagina1)
        self.Btn_7.setObjectName(u"Btn_7")
        self.Btn_7.setGeometry(QRect(480, 140, 51, 51))
        self.Btn_7.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon5 = QIcon()
        icon5.addFile(u"Fotos/gratis-png-frasco-gotero-mapa-material-acuario.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_7.setIcon(icon5)
        self.Btn_7.setIconSize(QSize(48, 48))
        self.Btn_7.setAutoRepeatDelay(100)
        self.label = QLabel(self.pagina1)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(480, 240, 91, 21))
        font1 = QFont()
        font1.setPointSize(14)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.Btn_Siguiente = QPushButton(self.pagina1)
        self.Btn_Siguiente.setObjectName(u"Btn_Siguiente")
        self.Btn_Siguiente.setGeometry(QRect(470, 390, 221, 31))
        self.Btn_Siguiente.setFont(font)
        self.Btn_Siguiente.setStyleSheet(u"background-color: rgb(150, 130, 255)\n"
"")
        self.Btn_12 = QRadioButton(self.pagina1)
        self.Btn_12.setObjectName(u"Btn_12")
        self.Btn_12.setGeometry(QRect(620, 190, 61, 51))
        self.Btn_12.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon6 = QIcon()
        icon6.addFile(u"Fotos/mascarilla-negra-pilaten.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_12.setIcon(icon6)
        self.Btn_12.setIconSize(QSize(32, 48))
        self.Btn_5 = QRadioButton(self.pagina1)
        self.Btn_5.setObjectName(u"Btn_5")
        self.Btn_5.setGeometry(QRect(550, 90, 51, 51))
        self.Btn_5.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon7 = QIcon()
        icon7.addFile(u"Fotos/istockphoto-1404980792-612x612.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_5.setIcon(icon7)
        self.Btn_5.setIconSize(QSize(48, 48))
        self.Btn_9 = QRadioButton(self.pagina1)
        self.Btn_9.setObjectName(u"Btn_9")
        self.Btn_9.setGeometry(QRect(620, 140, 51, 51))
        self.Btn_9.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon8 = QIcon()
        icon8.addFile(u"Fotos/96048633-dibujo-de-botellas-de-jab\u00f3n-l\u00edquido-dispensador-de-jab\u00f3n.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_9.setIcon(icon8)
        self.Btn_9.setIconSize(QSize(32, 48))
        self.push = QPushButton(self.pagina1)
        self.push.setObjectName(u"push")
        self.push.setGeometry(QRect(470, 270, 221, 31))
        self.push.setFont(font)
        self.push.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.Btn_Eliminar = QPushButton(self.pagina1)
        self.Btn_Eliminar.setObjectName(u"Btn_Eliminar")
        self.Btn_Eliminar.setGeometry(QRect(470, 310, 221, 31))
        self.Btn_Eliminar.setFont(font)
        self.Btn_Eliminar.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.Btn_11 = QRadioButton(self.pagina1)
        self.Btn_11.setObjectName(u"Btn_11")
        self.Btn_11.setGeometry(QRect(550, 190, 51, 51))
        self.Btn_11.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon9 = QIcon()
        icon9.addFile(u"Fotos/medicine-dropper-bottle-free-vector.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_11.setIcon(icon9)
        self.Btn_11.setIconSize(QSize(32, 48))
        self.Btn_2 = QRadioButton(self.pagina1)
        self.Btn_2.setObjectName(u"Btn_2")
        self.Btn_2.setGeometry(QRect(550, 40, 51, 51))
        self.Btn_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon10 = QIcon()
        icon10.addFile(u"Fotos/suerito.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_2.setIcon(icon10)
        self.Btn_2.setIconSize(QSize(48, 48))
        self.label_13 = QLabel(self.pagina1)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(210, -10, 271, 41))
        font2 = QFont()
        font2.setFamily(u"Segoe UI Black")
        font2.setPointSize(26)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_13.setFont(font2)
        self.label_13.setStyleSheet(u"color: rgb(0, 170, 127);")
        self.Btn_1 = QRadioButton(self.pagina1)
        self.Btn_1.setObjectName(u"Btn_1")
        self.Btn_1.setGeometry(QRect(480, 40, 51, 51))
        self.Btn_1.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon11 = QIcon()
        icon11.addFile(u"Fotos/medicine-dropper-bottle-free-vector.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_1.setIcon(icon11)
        self.Btn_1.setIconSize(QSize(32, 48))
        self.Btn_6 = QRadioButton(self.pagina1)
        self.Btn_6.setObjectName(u"Btn_6")
        self.Btn_6.setGeometry(QRect(620, 90, 51, 51))
        self.Btn_6.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon12 = QIcon()
        icon12.addFile(u"Fotos/istockphoto-1352019756-612x612.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_6.setIcon(icon12)
        self.Btn_6.setIconSize(QSize(32, 48))
        self.Btn_8 = QRadioButton(self.pagina1)
        self.Btn_8.setObjectName(u"Btn_8")
        self.Btn_8.setGeometry(QRect(550, 140, 51, 51))
        self.Btn_8.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon13 = QIcon()
        icon13.addFile(u"Fotos/gettyimages-1303772648-612x612.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_8.setIcon(icon13)
        self.Btn_8.setIconSize(QSize(32, 48))
        self.Btn_10 = QRadioButton(self.pagina1)
        self.Btn_10.setObjectName(u"Btn_10")
        self.Btn_10.setGeometry(QRect(480, 190, 51, 51))
        self.Btn_10.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon14 = QIcon()
        icon14.addFile(u"Fotos/3228f4903d1701037fa30c2ead90cd95.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_10.setIcon(icon14)
        self.Btn_10.setIconSize(QSize(32, 48))
        self.tableWidget = QTableWidget(self.pagina1)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(0, 40, 461, 381))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(23)
        sizePolicy.setVerticalStretch(32)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QSize(421, 0))
        self.tableWidget.setMaximumSize(QSize(461, 16777215))
        self.tableWidget.setAcceptDrops(False)
        self.tableWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.tableWidget.setWordWrap(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(39)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(80)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.verticalHeader().setMinimumSectionSize(10)
        self.Btn_4 = QRadioButton(self.pagina1)
        self.Btn_4.setObjectName(u"Btn_4")
        self.Btn_4.setGeometry(QRect(480, 90, 51, 51))
        self.Btn_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.Btn_4.setIcon(icon6)
        self.Btn_4.setIconSize(QSize(48, 38))
        self.spinBox = QSpinBox(self.pagina1)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(570, 240, 71, 22))
        self.spinBox.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_5 = QLabel(self.pagina1)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(470, 40, 221, 221))
        self.label_5.setStyleSheet(u"background:rgb(255, 255, 255)")
        self.stackedWidget.addWidget(self.pagina1)
        self.label_5.raise_()
        self.Btn_Barcode.raise_()
        self.Btn_3.raise_()
        self.Btn_7.raise_()
        self.label.raise_()
        self.Btn_Siguiente.raise_()
        self.Btn_12.raise_()
        self.Btn_5.raise_()
        self.Btn_9.raise_()
        self.push.raise_()
        self.Btn_Eliminar.raise_()
        self.Btn_11.raise_()
        self.Btn_2.raise_()
        self.label_13.raise_()
        self.Btn_1.raise_()
        self.Btn_6.raise_()
        self.Btn_8.raise_()
        self.Btn_10.raise_()
        self.tableWidget.raise_()
        self.Btn_4.raise_()
        self.spinBox.raise_()
        self.pagina_RE = QWidget()
        self.pagina_RE.setObjectName(u"pagina_RE")
        self.pagina_RE.setStyleSheet(u"background-color: rgb(170, 170, 255);")
        self.label_2 = QLabel(self.pagina_RE)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(230, 0, 251, 61))
        font3 = QFont()
        font3.setFamily(u"MS Shell Dlg 2")
        font3.setPointSize(72)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setWeight(9)
        self.label_2.setFont(font3)
        self.label_2.setStyleSheet(u"")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.btn_Actualizar = QPushButton(self.pagina_RE)
        self.btn_Actualizar.setObjectName(u"btn_Actualizar")
        self.btn_Actualizar.setGeometry(QRect(260, 380, 191, 30))
        self.btn_Actualizar.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(91, 91, 91);")
        self.tabla_inventario = QTableWidget(self.pagina_RE)
        if (self.tabla_inventario.columnCount() < 5):
            self.tabla_inventario.setColumnCount(5)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tabla_inventario.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tabla_inventario.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tabla_inventario.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tabla_inventario.setHorizontalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tabla_inventario.setHorizontalHeaderItem(4, __qtablewidgetitem9)
        self.tabla_inventario.setObjectName(u"tabla_inventario")
        self.tabla_inventario.setGeometry(QRect(70, 60, 561, 311))
        self.tabla_inventario.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.stackedWidget.addWidget(self.pagina_RE)
        self.pagina_Actualizar = QWidget()
        self.pagina_Actualizar.setObjectName(u"pagina_Actualizar")
        self.label_3 = QLabel(self.pagina_Actualizar)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(150, 40, 281, 41))
        self.label_17 = QLabel(self.pagina_Actualizar)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(40, 300, 351, 101))
        self.label_17.setStyleSheet(u"font: 75 27pt \"MS Sans Serif\";")
        self.label_14 = QLabel(self.pagina_Actualizar)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(40, 160, 47, 13))
        self.label_19 = QLabel(self.pagina_Actualizar)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(40, 220, 71, 16))
        self.BOTON_BUSCAR_3 = QPushButton(self.pagina_Actualizar)
        self.BOTON_BUSCAR_3.setObjectName(u"BOTON_BUSCAR_3")
        self.BOTON_BUSCAR_3.setGeometry(QRect(380, 100, 75, 23))
        self.TXT_NOMBRE_PRODUCTO_2 = QLineEdit(self.pagina_Actualizar)
        self.TXT_NOMBRE_PRODUCTO_2.setObjectName(u"TXT_NOMBRE_PRODUCTO_2")
        self.TXT_NOMBRE_PRODUCTO_2.setGeometry(QRect(220, 100, 151, 20))
        self.TXT_NOMBRE_PRODUCTO_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_15 = QLabel(self.pagina_Actualizar)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(40, 100, 181, 16))
        self.label_15.setStyleSheet(u"font: 75 11pt \"MS Shell Dlg 2\";")
        self.TXT_NOMBRE_3 = QLineEdit(self.pagina_Actualizar)
        self.TXT_NOMBRE_3.setObjectName(u"TXT_NOMBRE_3")
        self.TXT_NOMBRE_3.setGeometry(QRect(100, 160, 151, 20))
        self.TXT_NOMBRE_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_16 = QLabel(self.pagina_Actualizar)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(40, 190, 47, 20))
        self.TXT_PRECIO_3 = QLineEdit(self.pagina_Actualizar)
        self.TXT_PRECIO_3.setObjectName(u"TXT_PRECIO_3")
        self.TXT_PRECIO_3.setGeometry(QRect(100, 190, 151, 20))
        self.TXT_PRECIO_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_18 = QLabel(self.pagina_Actualizar)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(40, 130, 51, 21))
        self.TXT_CANTIDAD_2 = QLineEdit(self.pagina_Actualizar)
        self.TXT_CANTIDAD_2.setObjectName(u"TXT_CANTIDAD_2")
        self.TXT_CANTIDAD_2.setGeometry(QRect(100, 220, 151, 20))
        self.TXT_CANTIDAD_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.BOTON_ACTUALIZAR_3 = QPushButton(self.pagina_Actualizar)
        self.BOTON_ACTUALIZAR_3.setObjectName(u"BOTON_ACTUALIZAR_3")
        self.BOTON_ACTUALIZAR_3.setGeometry(QRect(80, 260, 121, 23))
        self.label_4 = QLabel(self.pagina_Actualizar)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(100, 130, 151, 21))
        self.label_4.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"")
        self.stackedWidget.addWidget(self.pagina_Actualizar)
        self.pagina_ELIMINAR = QWidget()
        self.pagina_ELIMINAR.setObjectName(u"pagina_ELIMINAR")
        self.stackedWidget.addWidget(self.pagina_ELIMINAR)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.frame_3)


        self.gridLayout.addWidget(self.frame_2, 1, 0, 1, 1)

        self.frame_superior = QFrame(self.centralwidget)
        self.frame_superior.setObjectName(u"frame_superior")
        self.frame_superior.setEnabled(True)
        self.frame_superior.setMinimumSize(QSize(0, 2))
        self.frame_superior.setStyleSheet(u"background-color: rgb(170, 170, 255);")
        self.frame_superior.setFrameShape(QFrame.StyledPanel)
        self.frame_superior.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_superior)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.BOTON_LOGO = QPushButton(self.frame_superior)
        self.BOTON_LOGO.setObjectName(u"BOTON_LOGO")
        self.BOTON_LOGO.setMaximumSize(QSize(16777215, 30))
        font4 = QFont()
        font4.setFamily(u"Franklin Gothic Demi")
        font4.setPointSize(14)
        self.BOTON_LOGO.setFont(font4)
        self.BOTON_LOGO.setStyleSheet(u"background-color: rgba(255, 0,0, 2);")
        icon15 = QIcon()
        icon15.addFile(u"Fotos/ICONO.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.BOTON_LOGO.setIcon(icon15)
        self.BOTON_LOGO.setIconSize(QSize(100, 30))

        self.gridLayout_2.addWidget(self.BOTON_LOGO, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame_superior, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.BOTON_TABLA.setText(QCoreApplication.translate("MainWindow", u"TABLA", None))
        self.BOTON_rEGISTRAR.setText(QCoreApplication.translate("MainWindow", u"  REGISTRAR", None))
        self.BOTON_ACTUALIZAR.setText(QCoreApplication.translate("MainWindow", u"ACTUALIZAR", None))
        self.BOTON_eLIMINAR.setText(QCoreApplication.translate("MainWindow", u" ELIMINAR", None))
        self.Btn_Barcode.setText(QCoreApplication.translate("MainWindow", u"Codigo Barras", None))
        self.Btn_3.setText("")
        self.Btn_7.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Cantidad:", None))
        self.Btn_Siguiente.setText(QCoreApplication.translate("MainWindow", u"Siguiente", None))
        self.Btn_12.setText("")
        self.Btn_5.setText("")
        self.Btn_9.setText("")
        self.push.setText(QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.Btn_Eliminar.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        self.Btn_11.setText("")
        self.Btn_2.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Punto de Venta", None))
        self.Btn_1.setText("")
        self.Btn_6.setText("")
        self.Btn_8.setText("")
        self.Btn_10.setText("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Codigo", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Producto", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Precio", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Cantidad", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Subtotal", None));
#if QT_CONFIG(tooltip)
        self.tableWidget.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.Btn_4.setText("")
        self.label_5.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:26pt; font-weight:600; font-style:italic;\">Inventario</span></p></body></html>", None))
        self.btn_Actualizar.setText(QCoreApplication.translate("MainWindow", u"ACTUALIZAR", None))
        ___qtablewidgetitem5 = self.tabla_inventario.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Codigo", None));
        ___qtablewidgetitem6 = self.tabla_inventario.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Cod_Prod", None));
        ___qtablewidgetitem7 = self.tabla_inventario.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Nom_Prod", None));
        ___qtablewidgetitem8 = self.tabla_inventario.horizontalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Stock", None));
        ___qtablewidgetitem9 = self.tabla_inventario.horizontalHeaderItem(4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Precio_Unidad", None));
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; font-style:italic;\">ACTUALIZAR PRODUCTO</span></p><p align=\"center\"><br/></p></body></html>", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Pedido Actualizado (\u25cf'\u25e1'\u25cf)</span></p></body></html>", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"NOMBRE:", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"CANTIDAD:", None))
        self.BOTON_BUSCAR_3.setText(QCoreApplication.translate("MainWindow", u"BUSCAR", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"NOMBRE DEL PRODUCTO:", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"PRECIO:", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"CODIGO:", None))
        self.BOTON_ACTUALIZAR_3.setText(QCoreApplication.translate("MainWindow", u"ACTUALIZAR", None))
        self.label_4.setText("")
        self.BOTON_LOGO.setText(QCoreApplication.translate("MainWindow", u"SUMAQ RUNAKAY", None))
    # retranslateUi
