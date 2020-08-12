class EllipticCurve(object):
	def __init__(self, a, b, p):
		self.a = a
		self.b = b
		self.p = p

	def __eq__(self, C):
		return (self.a,self.b) == (C.a,C.b)

	def has_point(self, x, y):
		return	(y**2) % self.p == (x ** 3 + self.a * x + self.b ) % self.p

	def __str__(self):
		return 'y^2 = x^3 + {}x+ {}'.format(self.a, self.b)
