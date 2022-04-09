from polynomial import Polynomial

def main() -> None:
	p = Polynomial([3, 5, 7, 3])
	print(p)
	print(p.eval(69))
	print(p.root())
	print(p.derivitive())

if __name__ == "__main__":
	main()
