# rock paper scissors in python

import random



while True:
	player = int(input('enter your choice (1 for rock, 2 for paper and 3 for scissors): '))

	if player <= 0 or player > 3:
		print("Invalid input bruh!!!!!")
		break

	computer = random.randint(1, 3)

	print(f'player : {player} & computer : {computer}\n')

	if player == computer:
		print("It's a Tie! -><-")

	if computer > player or computer == 0 and player == 2:
		print("You Lose! :'(")

	if player > computer or player == 0 and computer == 2:
		print("You Win!! 8) ")

	loop = input('play again?? (y/n) >> ')
	if (loop.lower() == 'n'):
		print("Exit Game")
		break