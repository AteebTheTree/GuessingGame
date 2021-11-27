import random

number = random.randint(1,9)
chances = 5

while chances > 0:
    guess = int(input("Enter a number! "))
    
    if guess == number:
        print("You won!")
        break
    else:
        if guess < number:
            print("Your guess was too low, guess a number higher than", guess)
        elif guess > number:
            print("Your guess was too high, guess a number lower than", guess)

        chances -= 1
else:
    print("You lose :(")
