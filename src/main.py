from polynomial import Polynomial

def main() -> None:
	p = Polynomial([4, 5, 1])
	p = p.substract(Polynomial([0, 1]))
	print(p)
	print(p.divide(Polynomial([2, 1])))
	print(p.eval(69))
	print(p.root())
	print(p.derivitive())

if __name__ == "__main__":
	main()
