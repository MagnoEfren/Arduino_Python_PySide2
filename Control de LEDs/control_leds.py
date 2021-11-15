# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'indicadores_ledsQlbAyw.ui'
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
        MainWindow.resize(617, 395)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(108, 108, 108);")
        self.frame.setFrameShape(QFrame.WinPanel)
        self.frame.setFrameShadow(QFrame.Plain)
        self.frame.setLineWidth(10)
        self.frame.setMidLineWidth(7)
        self.layoutWidget = QWidget(self.frame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(392, 32, 151, 46))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label)

        self.puertos = QComboBox(self.layoutWidget)
        self.puertos.setObjectName(u"puertos")
        self.puertos.setStyleSheet(u"QComboBox {\n"
"    border: 2px solid black;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: red;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"\n"
"\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"\n"
"QComboBox:on { \n"
"    padding-top: 5px;\n"
"    padding-left: 5px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 3px;\n"
"    border-left-color:#ff0000;\n"
"    border-left-style: solid; \n"
"    border-top-right-radius: 4px;   \n"
"    border-bottom-right-radius: 4px;\n"
"}\n"
"\n"
"")

        self.verticalLayout_4.addWidget(self.puertos)

        self.layoutWidget1 = QWidget(self.frame)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(392, 117, 151, 46))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.layoutWidget1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.velocidad = QComboBox(self.layoutWidget1)
        self.velocidad.setObjectName(u"velocidad")
        self.velocidad.setStyleSheet(u"QComboBox {\n"
"    border: 2px solid magenta;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: red;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"\n"
"\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"\n"
"QComboBox:on { \n"
"    padding-top: 5px;\n"
"    padding-left: 5px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 3px;\n"
"    border-left-color:#ffffff;\n"
"    border-left-style: solid; \n"
"    border-top-right-radius: 4px;   \n"
"    border-bottom-right-radius: 4px;\n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.velocidad)

        self.layoutWidget2 = QWidget(self.frame)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(390, 220, 151, 131))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.conectar = QPushButton(self.layoutWidget2)
        self.conectar.setObjectName(u"conectar")
        self.conectar.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid #000000;\n"
"    border-radius: 6px;\n"
"	background-color: rgb(0, 255, 127);\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 255, 0);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: red;\n"
"}\n"
"\n"
"\n"
"QPushButton::setCheckable(bool) {\n"
"	\n"
"	background-color: rgb(0, 255, 0);\n"
"\n"
"}")

        self.verticalLayout_3.addWidget(self.conectar)

        self.desconectar = QPushButton(self.layoutWidget2)
        self.desconectar.setObjectName(u"desconectar")
        self.desconectar.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid #000000;\n"
"    border-radius: 6px;\n"
"	\n"
"	background-color: rgb(255, 85, 0);\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 255, 0);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: red;\n"
"}\n"
"\n"
"\n"
"QPushButton::setCheckable(bool) {\n"
"	\n"
"	background-color: rgb(0, 255, 0);\n"
"\n"
"}")

        self.verticalLayout_3.addWidget(self.desconectar)

        self.actualizar = QPushButton(self.layoutWidget2)
        self.actualizar.setObjectName(u"actualizar")
        self.actualizar.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid #000000;\n"
"    border-radius: 6px;\n"
"	\n"
"	\n"
"	background-color: rgb(0, 0, 255);\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 255, 0);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: red;\n"
"}\n"
"\n"
"\n"
"QPushButton::setCheckable(bool) {\n"
"	\n"
"	background-color: rgb(0, 255, 0);\n"
"\n"
"}")

        self.verticalLayout_3.addWidget(self.actualizar)

        self.valor1 = QLabel(self.frame)
        self.valor1.setObjectName(u"valor1")
        self.valor1.setGeometry(QRect(330, 50, 24, 39))
        self.valor1.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 11pt \"Impact\";")
        self.valor2 = QLabel(self.frame)
        self.valor2.setObjectName(u"valor2")
        self.valor2.setGeometry(QRect(330, 120, 24, 39))
        self.valor2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 11pt \"Impact\";")
        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 48, 311, 41))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"\n"
"font: 87 10pt \"Arial Black\";")

        self.horizontalLayout.addWidget(self.label_5)

        self.slider1 = QSlider(self.widget)
        self.slider1.setObjectName(u"slider1")
        self.slider1.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border: 1px solid #00ff00;\n"
"    height: 4px; \n"
"    background: #00ff00;\n"
" \n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background:  #0000ff;\n"
"    \n"
"\n"
"    width: 28px;\n"
"	height:28px;\n"
"\n"
"left: 11px;\n"
"right: 11px;\n"
"\n"
"\n"
"    margin: -12px; \n"
"    border-radius:14px;\n"
"}\n"
"\n"
"\n"
"QSlider::add-page:horizontal{\n"
"background-color:white;\n"
"border: 1px solid white;\n"
"}\n"
"")
        self.slider1.setMaximum(255)
        self.slider1.setSingleStep(0)
        self.slider1.setPageStep(8)
        self.slider1.setValue(20)
        self.slider1.setOrientation(Qt.Horizontal)
        self.slider1.setInvertedAppearance(False)
        self.slider1.setInvertedControls(True)
        self.slider1.setTickPosition(QSlider.TicksAbove)

        self.horizontalLayout.addWidget(self.slider1)

        self.widget1 = QWidget(self.frame)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(10, 118, 311, 41))
        self.horizontalLayout_2 = QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.widget1)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"font: 87 10pt \"Arial Black\";")

        self.horizontalLayout_2.addWidget(self.label_6)

        self.slider2 = QSlider(self.widget1)
        self.slider2.setObjectName(u"slider2")
        self.slider2.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border: 1px solid #00ff00;\n"
"    height: 4px; \n"
"    background: #00ff00;\n"
" \n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background:  #0000ff;\n"
"    \n"
"\n"
"    width: 28px;\n"
"	height:28px;\n"
"\n"
"left: 11px;\n"
"right: 11px;\n"
"\n"
"    margin: -12px; \n"
"    border-radius:14px;\n"
"}\n"
"\n"
"\n"
"QSlider::add-page:horizontal{\n"
"background-color:white;\n"
"border: 1px solid white;\n"
"}")
        self.slider2.setMaximum(255)
        self.slider2.setSingleStep(0)
        self.slider2.setPageStep(8)
        self.slider2.setValue(20)
        self.slider2.setOrientation(Qt.Horizontal)
        self.slider2.setInvertedAppearance(False)
        self.slider2.setInvertedControls(True)
        self.slider2.setTickPosition(QSlider.TicksAbove)

        self.horizontalLayout_2.addWidget(self.slider2)

        self.widget2 = QWidget(self.frame)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(50, 230, 68, 86))
        self.verticalLayout_5 = QVBoxLayout(self.widget2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.widget2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"font: 87 10pt \"Arial Black\";")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_7)

        self.radioButton1 = QRadioButton(self.widget2)
        self.radioButton1.setObjectName(u"radioButton1")
        self.radioButton1.setStyleSheet(u"\n"
"QRadioButton::indicator {\n"
"    width:                  50px;\n"
"    height:                 50px;\n"
"    border-radius:          30px;\n"
"    \n"
"\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:       #00ff00;\n"
"    border:                 5px solid black;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:       red;\n"
"   border:                 5px solid black;\n"
"}")
        self.radioButton1.setCheckable(True)
        self.radioButton1.setAutoExclusive(False)

        self.verticalLayout_5.addWidget(self.radioButton1)

        self.widget3 = QWidget(self.frame)
        self.widget3.setObjectName(u"widget3")
        self.widget3.setGeometry(QRect(210, 230, 68, 86))
        self.verticalLayout_6 = QVBoxLayout(self.widget3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.widget3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"font: 87 10pt \"Arial Black\";")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_8)

        self.radioButton2 = QRadioButton(self.widget3)
        self.radioButton2.setObjectName(u"radioButton2")
        self.radioButton2.setStyleSheet(u"\n"
"QRadioButton::indicator {\n"
"    width:                  50px;\n"
"    height:                 50px;\n"
"    border-radius:          30px;\n"
"    \n"
"\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:       #00ff00;\n"
"    border:                 5px solid black;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:       red;\n"
"   border:                 5px solid black;\n"
"}")
        self.radioButton2.setCheckable(True)
        self.radioButton2.setAutoExclusive(False)

        self.verticalLayout_6.addWidget(self.radioButton2)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Seleccione el Puerto", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Seleccione la Velocidad", None))
        self.conectar.setText(QCoreApplication.translate("MainWindow", u"CONECTAR", None))
        self.desconectar.setText(QCoreApplication.translate("MainWindow", u"DESCONECTAR", None))
        self.actualizar.setText(QCoreApplication.translate("MainWindow", u"ACTUALIZAR", None))
        self.valor1.setText(QCoreApplication.translate("MainWindow", u"255", None))
        self.valor2.setText(QCoreApplication.translate("MainWindow", u"255", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"PWM 1", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"PWM 2", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"LED 1", None))
        self.radioButton1.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"LED 2", None))
        self.radioButton2.setText("")
    # retranslateUi

