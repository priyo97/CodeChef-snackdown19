def main():


	t = int(input())

	while t:

		n = int(input())
		
		a = [int(x) for x in input().split()]

		s = n

		days = 0

		i = 1

		c = a[0]

		while i < n:

			temp = sum(a[i:i+c])
			
			i += c

			c += temp

			days += 1

		print(days)


		t -= 1

main()