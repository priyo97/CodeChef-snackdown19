def main():

	t = int(input())


	while t:

		n = int(input())

		a = [int(x) for x in input().split()]
		b = [int(x) for x in input().split()]


		for i in range(n-2):

			c = b[i] - a[i]

			if c > 0:

				a[i] = a[i] + c
				a[i + 1] = a[i + 1] + 2 * c
				a[i + 2] = a[i + 2] + 3 * c

			elif c < 0:

				print("NIE")
				break

		else:

			if a[n-2] == b[n-2] and a[n-1] == b[n-1]:

				print("TAK")
			
			else:

				print("NIE")

		t -= 1



main()