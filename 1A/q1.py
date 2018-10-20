def main():


	t = int(input())

	while t:

		n = int(input())
		a = [int(x) for x in input().split()]

		prev = a[-1]

		count = 0

		for i in a[n-2::-1]:

			if i > prev:

				count += 1

			prev = i 

			if count > 1:

				print("NO")
				break

		else:

			if count == 0:

				print("YES")
			
			else:

				if a[0] >= a[-1]:


					print("YES")

				else:

					print("NO")

		t -= 1

main()