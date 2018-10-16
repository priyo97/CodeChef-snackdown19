import math

def isPrime(num):

	for i in range(2,num):

		if not num % i:

			return False

	return True


def isSemiPrime(num):

	for i in range(2,num):

		if isPrime(i):

			n = num // i 

			if num / i - n == 0 and n != i and n != 1:

				if isPrime(n):

					return True

	return False



def main():


	t = int(input())


	while t:

		n = int(input())

		for s1 in range(1,n):

			if isSemiPrime(s1):

				s2 = n - s1

				if isSemiPrime(s2):

					print("YES")
					break
		else:
			print("NO")





		t -= 1


main()