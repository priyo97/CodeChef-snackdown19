def totalWays(n):

	total = 1

	n -= 1

	while n > 0:

		total *= n 

		n -= 2

	return total



def main():

	t = int(input())

	while t:

		n = int(input())

		a = [int(x) for x in input().split()]

		a.sort(reverse=True)

		tmp = a[0]

		count = []

		c = 1

		l = 0

		for i in a[1:]:

			if tmp == i:

				c += 1

			else:

				count.append(c)

				l += 1

				tmp = i 

				c = 1

		else:

			count.append(c)

			l += 1


		total = 1

		for i in range(l):

			if not count[i] % 2:

				c = totalWays(count[i])

			else:

				c = count[i] * totalWays(count[i] - 1) * count[i+1]

				count[i+1] -= 1

			# print(c)
			total *= c 


		print(total % 1000000007)




		t -= 1

main()