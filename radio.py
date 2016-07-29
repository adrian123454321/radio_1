class radio():
	def __init__(self,marca):
		self.marca=marca
		self.encendido=False
		self.en_Fm=True
		self.emisora=88.0
		self.volumen=0

	def encender(self):
		self.encendido=True

	def apagar(self):
		self.encendido=False

	def subir_volumen(self):
		if self.volumen>=100:
			self.volumen=100
		else:
			self.volumen+=5

	def bajar_volumen(self):
		if self.vomlumen<=0
			self.volumen=0
		else:
			self.volumen-=5

	def subir_emisora(self):
		if 	self.en_Fm>107.0:
			self.en_Fm=87.0
		else:
			sel.em_Fm+=0.5

	def bajar_emisora



