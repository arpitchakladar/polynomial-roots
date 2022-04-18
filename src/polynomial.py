import math
from copy import copy
from typing import Type
import utils

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
			elif self[0] == 0:
				res = ""
			else:
				res = "+ " + res
		elif self[0] < 0:
			res = "-" + res

		for i in range(1, len(self.coefficients)):
			if self[i] != 0:
				degree = ""

				if i > 1:
					degree = utils.get_super(i)

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
		return Polynomial(list(range(degree - self.degree)) + self.coefficients)

	def _div(self, other):
		if self.degree > other.degree:
			coefficients = []
			remainder = copy(self)
			for i in range(self.degree, other.degree - 1, -1):
				coefficient = remainder[i] / other[other.degree]
				remainder = remainder - (other * Polynomial([coefficient]))._raise_to(i)
				coefficients.append(coefficient)
			coefficients.reverse()
			return (Polynomial(coefficients), remainder)
		raise Exception("The left operand must be greater than the right operand.")

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
	def roots(self, accuracy = 10000) -> list[float]:
		p = copy(self)
		roots = []
		while p.degree > 0:
			d = p.derivitive
			res = p[0]
			for i in range(accuracy):
				v = p(res)
				m = d(res)
				c = v - m * res
				res = - (c / m)
			if (-0.1 < self(res) < 0.1):
				roots.append(round(res * accuracy) / accuracy)

			try:
				p /= Polynomial([-res, 1])
			except:
				break

		return list(dict.fromkeys(roots))

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
		(quotient, _) = self._div(other)
		return quotient

	def __mod__(self, other):
		(_, remainder) = self._div(other)
		return remainder

	def __truediv__(self, other):
		return self.__div__(other)
