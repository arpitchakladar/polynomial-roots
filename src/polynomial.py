import math
from copy import copy
from typing import Type

def get_super(x):
	normal = "0123456789"
	super_s = "⁰¹²³⁴⁵⁶⁷⁸⁹"
	res = x.maketrans(''.join(normal), ''.join(super_s))
	return x.translate(res)

class Polynomial:
	coefficients: list[float]

	def __init__(self, coefficients: list[float]):
		if len(coefficients) < 1:
			raise Exception("A polynomial must have atleast 1 term.")
		self.coefficients = coefficients

	def __str__(self) -> str:
		res = str(abs(self[0]))
		if self.degree > 0:
			if self[0] < 0:
				res = "- " + res
			else:
				res = "+ " + res
		elif self[0] < 0:
			res = "-" + res

		for i in range(1, len(self.coefficients)):
			if self[i] != 0:
				degree = ""
				if i > 1:
					degree = get_super(str(i))
				abs_coefficient = abs(self[i])
				coefficient = str(abs_coefficient) if abs_coefficient != 1 else ""
				sign = ""
				if i != self.degree:
					sign = "- " if self[i] < 0 else "+ "
				elif self[i] < 0:
					sign = "-"
				res = f"{sign}{coefficient}x{degree} " + res
		return res

	def _get_greator_and_smallor(self, p):
		g = None
		l = None
		if p.degree > self.degree:
			g = p
			l = self
		else:
			l = p
			g = self
		return (g, l)

	def _raise_to(self, degree: int):
		return Polynomial([0 for i in range(0, degree - self.degree)] + self.coefficients)

	@property
	def degree(self):
		return len(self.coefficients) - 1

	def __getitem__(self, x: int):
		return self.coefficients[x]

	def __call__(self, x) -> float:
		res = self[0]
		for i in range(1, len(self.coefficients)):
			res += math.pow(x, i) * self[i]
		return res

	@property
	def derivitive(self):
		coefficients = []
		for i in range(1, len(self.coefficients)):
			coefficients.append(self[i] * i)
		return Polynomial(coefficients)

	@property
	def root(self, accuracy = 10000) -> float:
		d = self.derivitive
		res = self[0]
		for i in range(accuracy):
			v = self(res)
			m = d(res)
			c = v - m * res
			res = - (c / m)
		return math.floor(res * accuracy) / accuracy

# Operations
	def __neg__(self):
		res = copy(self)
		for i in range(len(self.coefficients)):
			res.coefficients[i] = - self[i]
		return res

	def __add__(self, other):
		(g, l) = self._get_greator_and_smallor(other)
		coefficients = []
		for i in range(g.degree + 1):
			if i <= l.degree:
				coefficients.append(g[i] + l[i])
			else:
				coefficients.append(g[i])
		return Polynomial(coefficients)

	def __sub__(self, other):
		return self + (-other)

	def __mul__(self, other):
		res = Polynomial([0])
		for i in range(self.degree + 1):
			for j in range(other.degree + 1):
				res = res + Polynomial([self[i] * other[j]])._raise_to(i + j)
		return res

	def __div__(self, other):
		if self.degree > other.degree:
			coefficients = []
			remainder = copy(self)
			for i in range(self.degree, other.degree - 1, -1):
				coefficient = remainder[i] / other[other.degree]
				remainder = remainder - (other * Polynomial([coefficient])._raise_to(i - other.degree))
				coefficients.append(coefficient)
			coefficients.reverse()
			return Polynomial(coefficients)
		return Polynomial([0])

	def __truediv__(self, other):
		return self.__div__(other)
