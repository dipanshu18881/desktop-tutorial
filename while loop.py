#i = 1
#while condition:       while i <= 5:
#    ...                       print(i)
#                              i = i + 1

secret_number = 7
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("Guess the number :"))
    guess_count += 1
    if guess == secret_number:
        print("You guessed it!")
        break
else:
    print("Sorry ! Wrong guess.")