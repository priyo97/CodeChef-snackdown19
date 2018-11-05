def main():


	t = int(input())

	years = {2010,2015,2016,2017,2019}

	while t:

		n = int(input())

		if n in years:

			print("HOSTED")
		else:

			print("NOT HOSTED")

		t -= 1


main()
