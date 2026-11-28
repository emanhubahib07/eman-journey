import random
number = random.randint(1,10)

print("====== Guessing number game ======")
while True:
    Guess = int(input("Guess a number 1 to 10: "))
    if Guess == number:
        print("You're Correct!")
        print("Thank youu for playing!")
        break
    else:
        print("Try again")
        if Guess > number:
            print("Too high!")
        elif Guess < number:
            print("Too low!")
