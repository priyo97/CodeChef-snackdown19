def main():


	t = int(input())

	while t:

		n = int(input())

		words = {}

		hand = {"d":0,"f":0,"j":1,"k":1}

		total = 0

		while n:

			s = input()

			if not words.get(s,False): 
				
				time = 2

				prev_hand = hand[ s[0] ]


				for i in s[1:]:

					current_hand = hand[i]

					if current_hand == prev_hand:

						time += 4

					else:

						time += 2

					prev_hand = current_hand

				words[s] = time // 2

				total += time

			else:

				total += words[s]

			n -= 1

		print(total)

		t -= 1

main()