from polynomial import Polynomial

def main() -> None:
	p = Polynomial([-16, -30, 3, 2, 12, 1])
	p2 = p / Polynomial([2, 1, 1])
	print(p2 * Polynomial([2, 1, 1]))
	print(p * Polynomial([2, 1]))

if __name__ == "__main__":
	main()
