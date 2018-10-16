def main():


	t = int(input())

	while t:

		n, k = [int(x) for x in input().split()]
		a = [int(x) for x in input().split()]

		a.sort(reverse=True)

		c = a[k-1]

		count = 0

		for i in a[k:]:

			if c != i:
				break

			count += 1


		print(k+count)

		t -= 1


main()