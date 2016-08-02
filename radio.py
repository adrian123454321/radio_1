class Radio():
	def __init__(self,marca):
		self.marca=marca
		self.encendido=False
		self.en_Fm=True
		self.en_am=False
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
		if self.vomlumen<=0:
			self.volumen=0
		else:
			self.volumen-=5

	def subir_emisora(self):
		if not en_fm:
		 self.en_am=True
		 if self.en_am>=1300:
		 	self.en_am=300
		 else:
		 	self.en_am+=40

	def bajar_emisora(self):
		if not en_fm:
			self.en_am=True
			if self.en_am<=300:
				self.en_am=1300
			else:
				self.en_am-=40

	def subir_emisora(self):
		if not en_am:
			self.en_fm=True
			if self.en_fm<=107.0:
				self.en_fm=88.0
			else:
				self.en_fm+=0.5

	def bajar_emisora(self):
		if not en_am:
			self.en_fm=True
			if sefl.en_fm<=88.0:
				self.en_fm=107.0
			else:






			 	



