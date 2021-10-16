def bruteforcedivision(decimal):
	for x in range(0, 100):
		for y in range(1, 100):
			if (1.0 * x/y) - .001 < decimal and (1.0 * x/y) + .001 > decimal:
			#if (1.0 * x/ 1.0 * y) == decimal:
				print x
				print y
				return " "
