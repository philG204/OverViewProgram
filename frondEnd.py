import sys
import subprocess as sub
from threading import Thread
from PyQt5 import QtWidgets, QtCore, uic
import time
import socket

class Dialog(QtWidgets.QDialog):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.ui = uic.loadUi("/home/philipp/Dokumente/qt/dialog.ui", self)
		self.ui.scrollArea.setWidget(self.ui.label_6)
		#self.ui.scrollArea_2.setWidget(self.ui.label_3)
		#self.ui.scrollArea_3.setWidget(self.ui.label_2)
		#self.ui.scrollArea_4.setWidget(self.ui.label_9)
		#self.ui.scrollArea_5.setWidget(self.ui.label_10)
		#self.ui.scrollArea_6.setWidget(self.ui.label_11)
		#self.ui.scrollArea_7.setWidget(self.ui.label_14)
		#self.ui.scrollArea_8.setWidget(self.ui.label_16)
		#self.ui.scrollArea_9.setWidget(self.ui.label_17)
		#self.ui.scrollArea_10.setWidget(self.ui.label_19)
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.built_up_connection("192.168.1.100", 420)
		self.t = thread(self.ui, self.s)
		self.t.start()


	def built_up_connection(self, ip, port):
		try: 
			self.s.connect((ip, port))
			

		except socket.error as e:
				self.ui.label_3.setText("Es konnte keine Verbindung aufgebaut werden")
				print(e)


class thread(QtCore.QThread):
	def __init__(self, UI, conn):
		QtCore.QThread.__init__(self)
		self.UI = UI
		self.conn = conn

	def run(self):
		
		while True:
			self.manage_input(self.UI.label_14)
			
      

	def manage_input(self, L):
    #Recive the size of command and prints it out 
		size = self.conn.recv(1024).decode('utf-8')
		print(type(size), sys.getsizeof(size), size)
		time.sleep(0.05)
    #Recive the actually command  
		text = self.conn.recv(int(size))
		print(text)
		L.setText(text.decode('utf-8'))
		time.sleep(0.05)



app = QtWidgets.QApplication(sys.argv)
dialog = Dialog()
dialog.show()
sys.exit(app.exec_())
