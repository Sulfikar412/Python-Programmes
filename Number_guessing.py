import random
computer_guess=random.randint(1,10)
user_guess=int(input("Enter your Guess :"))
if user_guess==computer_guess:
    print("You win !")
else:
    print("you loss")
print("computer Guess :",computer_guess)
print("User_Guess :",user_guess)
