from typing import NoReturn
from polynomial import Polynomial
import utils

def main() -> NoReturn:
	coefficients = [int(input("Enter constant term : "))]
	count = 1

	while True:
		_input = input(f"Enter coefficient for x{utils.get_super(count)} (type \"end\" to stop) : ")
		if (_input.lower().strip() == "end"):
			break

		try:
			coefficients.append(int(_input))
		except:
			break

		count += 1

	p = Polynomial(coefficients)
	print("\r\nPolynomial :-\r\n\r\n" + str(p) + "\r\n")
	print("Roots = " + str(p.roots))

if __name__ == "__main__":
	main()
