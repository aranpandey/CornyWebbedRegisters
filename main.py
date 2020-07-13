print("Guess a number")
guess = input()
guess = int(guess)

if guess < 10:
  print("The number is less than ten")
if guess == 10:
  print("The number is equal to  ten")
if guess > 10:
  print("The number is greater than  ten")