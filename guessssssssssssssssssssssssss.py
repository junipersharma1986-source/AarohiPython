import random
print("welcome to guess the number")
Secret_number = random.randint(1,80) 

guess=None

while guess != Secret_number:
   guess = int(input("guess a number between 1 and 80"))

   if guess< Secret_number:
      print("too low! try again!!")
   elif guess< Secret_number:
      print("too high! guess again!")
   else: 
      print("correct! you guessed the number!")
      


