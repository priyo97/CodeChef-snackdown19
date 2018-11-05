def main():


	t = int(input())

	while t:


		n, k = [int(x) for x in input().split()]

		a = [int(x) for x in input().split()]

		a.sort(reverse=True)
		
		a[:k] = [1]*k

		sum1 = k

		s = sum(a)

		for i in a[k:]:

			sum1 += i ** 2


		if sum1 <= s:

			print("YES")
		else:
			print("NO") 


		t -= 1

main()