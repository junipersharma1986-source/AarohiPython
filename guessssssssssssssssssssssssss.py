import random
print("welcome to guess the number")
Secret_number = random.randint(1,100) 

guess=None

while guess != Secret_number:
   guess = int(input("guess a number between 1 and 20"))

   if guess< Secret_number:
      print("too low! try again!!")
   elif guess< Secret_number:
      print("too high! guess again!")
   else:
      print("correct! you guessed the number!")
      


