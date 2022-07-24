# Control de Leds con Arduino  desde una GUI en Python con PySide2 
# @autor: Magno Efren
# Youtube: https://www.youtube.com/c/MagnoEfren

import sys
from control_leds import *
from comunicacion_serial import Comunicacion
from PySide2.QtCore import QTimer  

class MiApp(QMainWindow):
	def __init__(self,*args, **kwargs):
		super().__init__()
		self.ui = Ui_MainWindow() 
		self.ui.setupUi(self)

		self.serial = Comunicacion()
		self.puertos_disponible()		

		self.nivelpwm1 = 0
		self.nivelpwm2 = 0
		self.led1 = 'b'
		self.led2 = 'd'
	
		self.ui.velocidad.addItems(self.serial.baudrates)
		self.ui.velocidad.setCurrentText("9600")

		self.ui.conectar.clicked.connect(self.conectar)
		self.ui.actualizar.clicked.connect(self.puertos_disponible)
		self.ui.desconectar.clicked.connect(self.desconectar)

		# obtener el valor de los sliders
		self.ui.slider1.valueChanged.connect(self.slider1_pwm)
		self.ui.slider2.valueChanged.connect(self.slider2_pwm)

		self.ui.radioButton1.toggled.connect(self.control_led1)
		self.ui.radioButton2.toggled.connect(self.control_led2)


	def  slider1_pwm(self, event):
		self.ui.slider1.setValue(event)
		self.ui.valor1.setText(str(event))
		self.nivelpwm1 = event
		dato = (self.nivelpwm1 , self.nivelpwm2, ')))))')
		self.serial.enviar_datos(dato)

	def slider2_pwm(self, event):			
		self.ui.slider2.setValue(event)
		self.ui.valor2.setText(str(event))
		self.nivelpwm2 = event
		dato = (self.nivelpwm1 , self.nivelpwm2, ')))))')
		self.serial.enviar_datos(dato)

	def control_led1(self):
		if self.ui.radioButton1.isChecked()==True:
			self.led1 = 'a'	
			dato = (self.led1)
			self.serial.enviar_datos(dato)	
		else:
			self.led1 = 'b'
			dato = (self.led1)
			self.serial.enviar_datos(dato)			

	def control_led2(self):
		if self.ui.radioButton2.isChecked()==True:
			self.led2 = 'c'	
			dato = (self.led2)
			self.serial.enviar_datos(dato)			
		else:
			self.led2 = 'd'
			dato = (self.led2)
			self.serial.enviar_datos(dato)	
			
	def conectar(self):		
		port = self.ui.puertos.currentText()   
		baud = self.ui.velocidad.currentText()   
		self.serial.arduino.port = port      
		self.serial.arduino.baudrate = baud  
		self.serial.conexion_serial()    

	def desconectar(self):
		self.serial.desconectar()		

	def puertos_disponible(self):
		self.serial.puertos_disponibles()
		self.ui.puertos.clear()
		self.ui.puertos.addItems(self.serial.puertos)		

if __name__ == "__main__":
     app = QApplication(sys.argv)
     mi_app = MiApp()
     mi_app.show()
     sys.exit(app.exec_())		
