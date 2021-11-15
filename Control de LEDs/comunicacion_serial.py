# Control de Leds con Arduino  desde una GUI en Python con PySide2 
# @autor: Magno Efren
# Youtube: https://www.youtube.com/c/MagnoEfren


from PySide2.QtCore import  QObject  # pyqtSignal para pyqt5
import serial, serial.tools.list_ports

class Comunicacion(QObject):                                                  
	def __init__(self):
		super().__init__()
		self.arduino  = serial.Serial()
		self.arduino.timeout = 0.5		
		
		self.baudrates = ['1200', '2400', '4800', '9600', '19200', '38400', '115200']
		self.puertos = []


	def puertos_disponibles(self):
		self.puertos = [port.device for port in serial.tools.list_ports.comports()]


	def conexion_serial(self):
		try:	
			self.arduino.open()
		except:
			print('error al conectar')

	def enviar_datos(self, data):
		if (self.arduino.is_open): 
			self.datos = str(data) + "\n"
			self.arduino.write(self.datos.encode())
	
		else:
			print('error')

		
	def desconectar(self):
		self.arduino.close()





