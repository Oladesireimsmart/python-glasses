Secret=534
for i in range(1, 5):
    guess=int(input("Guess the secret number: "))
    if guess == Secret:
        print("Congratulations! You guessed the secret number.")
        break
    else:
        print("Wrong guess. Try again.")