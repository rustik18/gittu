import random

lowest_num = 1
highest_num = 100
random_number = random.randint(lowest_num, highest_num)
guesses = 0

is_working = True
print(f"Guess a number between {lowest_num} and {highest_num}.")
while is_working:
	guess = (input("Enter your guess:"))
	if guess.isdigit():
		guess = int(guess)
		guesses += 1
		
		if guess < lowest_num or guess > highest_num:
			print("That number is out of range.")
			print(f"Please select a number between {lowest_num} and {highest_num}.")
			
		elif guess > random_number:
			print("Too high.Try again!")
			
		elif guess < random_number:
			print("Too low. Try again!")
				
		else:
			print("!!!CORRECT!!!")
			is_working = False
				
	else:
		print("Invalid answer")
		print(f"We need number between {lowest_num} and {highest_num}. KALLA!")
				
print(f"The number of guesses: {guesses}.")