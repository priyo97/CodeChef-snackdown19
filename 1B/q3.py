def main():

	t = int(input())

	while t:

		n, m, k, l = [int(x) for x in input().split()]

		a = [int(x) for x in input().split()]

		a.sort()

		tt = (m + 1) * l

		if a[0] < k:

			min = tt - a[0]

			# print("hi")

			for i in a[1:]:

				tt = tt + l

				if i < k:

					m = tt - i 

					if m < min:

						min = m
				else:

					m = tt - k

					if m < min:

						min = m

					break

			else:

				tt = tt + l

				m = tt - k

				if m < min:

					min = m


			if len(a) == 1:

				tt = tt + l
				m = tt - k

				if m < min:

					min = m

		else:

			min = tt - k


		print(min)

		t -= 1


main()