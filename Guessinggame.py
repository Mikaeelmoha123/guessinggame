from operator import truediv


secret_word = "ducati"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word:
    if guess_count < guess_limit:
        guess = input("enter your guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("out of guesses, enda kwa babako! ")
else:
    print("you win ")
