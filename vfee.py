class Vibracion_Forzada_Estado_Estable():
	def __init__(self, v0, t0, x0, caso_int):
		self.caso= caso_int
		self.vel0= v0
		self.time0= t0
		self.pos0= x0
		self.T= 0
		self.A= 0
		self.f= 0
		self.pos= []
		self.vel= []
		self.ace= []