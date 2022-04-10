import math
from copy import copy
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
		res = str(abs(self.get_coefficient(0)))
		if self.get_degree() > 0:
			if self.get_coefficient(0) > 0:
				res = "+ " + res
			else:
				res = "- " + res

		for i in range(1, len(self.coefficients)):
			if self.get_coefficient(i) != 0:
				p = ""
				if i > 1:
					p = get_super(str(i))
				c = ""
				if self.get_coefficient(i) != 1:
					c = str(abs(self.get_coefficient(i)))
				s = ""
				if self.get_coefficient(i) < 0:
					s = "- "
				elif i != self.get_degree():
					s = "+ "
				res = f"{s}{c}x{p} " + res
		return res

	def _get_greator_and_smallor(self, p):
		g = None
		l = None
		if p.get_degree() > self.get_degree():
			g = p
			l = self
		else:
			l = p
			g = self
		return (g, l)

	def _raise_to(self, degree: int):
		return Polynomial([0 for i in range(0, degree - self.get_degree())] + self.coefficients)

	def get_degree(self):
		return len(self.coefficients) - 1

	def get_coefficient(self, term: int):
		return self.coefficients[term]

	def negate(self):
		p = copy(self)
		for i in range(len(self.coefficients)):
			p.coefficients[i] = - self.get_coefficient(i)
		return p

	def add(self, p):
		(g, l) = self._get_greator_and_smallor(p)
		coefficients = []
		for i in range(g.get_degree() + 1):
			if i <= l.get_degree():
				coefficients.append(g.get_coefficient(i) + l.get_coefficient(i))
			else:
				coefficients.append(g.get_coefficient(i))
		return Polynomial(coefficients)

	def substract(self, p):
		return self.add(p.negate())

	def multiply(self, p: int): # only monomials
		return Polynomial([p * i for i in self.coefficients])

	def divide(self, p):
		if self.get_degree() > p.get_degree():
			coefficients = []
			remainder = copy(self)
			for i in range(self.get_degree(), p.get_degree() - 1, -1):
				coefficient = remainder.get_coefficient(i) / p.get_coefficient(p.get_degree())
				k = p.multiply(coefficient)._raise_to(i)
				remainder = remainder.substract(k)
				coefficients.append(coefficient)
			coefficients.reverse()
			return Polynomial(coefficients)

	def eval(self, x) -> float:
		res = self.get_coefficient(0)
		for i in range(1, len(self.coefficients)):
			res += math.pow(x, i) * self.get_coefficient(i)
		return res

	def derivitive(self):
		coefficients = []
		for i in range(1, len(self.coefficients)):
			coefficients.append(self.get_coefficient(i) * i)
		return Polynomial(coefficients)

	def root(self, acc = 10000) -> float:
		d = self.derivitive()
		res = self.get_coefficient(0)
		for i in range(acc):
			v = self.eval(res)
			m = d.eval(res)
			c = v - m * res
			res = - (c / m)
		return res
