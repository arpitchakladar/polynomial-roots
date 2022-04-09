import math
import typing

def get_super(x):
    normal = "0123456789"
    super_s = "⁰¹²³⁴⁵⁶⁷⁸⁹"
    res = x.maketrans(''.join(normal), ''.join(super_s))
    return x.translate(res)

class Polynomial:
	coefficients: list[float]

	def __init__(self, coefficients: list[float]):
		self.coefficients = coefficients

	def __str__(self):
		res = str(self.coefficients[0])
		for i in range(1, len(self.coefficients)):
			p = ""
			if i > 1:
				p = get_super(str(i))
			res = f"{self.coefficients[i]}x{p} + " + res
		return res

	def eval(self, x) -> float:
		res = self.coefficients[0]
		for i in range(1, len(self.coefficients)):
			res += math.pow(x, i) * self.coefficients[i]
		return res

	def derivitive(self):
		coefficients = []
		for i in range(1, len(self.coefficients)):
			coefficients.append(self.coefficients[i] * i)
		return Polynomial(coefficients)

	def root(self, acc = 10000) -> float:
		d = self.derivitive()
		res = self.coefficients[0]
		for i in range(acc):
			v = self.eval(res)
			m = d.eval(res)
			c = v - m * res
			res = - (c / m)
		return res
