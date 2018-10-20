def main():

	t = int(input())

	while t:

		n, m = [int(x) for x in input().split()]

		a = []

		d = {}

		i = 1

		while i <= n:

			s = input()

			j = 1

			while j <= m:

				if s[j-1] == '1':

					for e in a:

						dist = i - e[0] + abs(j - e[1])


						d[dist] = d.get(dist,0) + 1

					a.append((i,j))

				j += 1

			i += 1
		
		for i in range(1,n+m-1):

			print(d.get(i,0),end=" ")




		t -= 1

main()