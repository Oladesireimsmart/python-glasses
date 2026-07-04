import random
playing = True
number = str(random.randint(0, 9))   

print("I will generate a numberfrom 0 to 9 and you have to guess the number , one digit at a time.")
print("thegame ends once you get one hero")

while playing:
    guess = input("Enter your guess: ")
    if guess == number:
        print("Congratulations! You guessed the number.")
        playing = False
    else:
        print("Wrong guess. Try again.")