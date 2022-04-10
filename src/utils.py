def get_super(x: int):
	x = str(x)
	return x.translate(x.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹"))
