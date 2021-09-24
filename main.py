import random as rand
number = rand.randint(1000, 10000)
guess = int(input("What's your first guess? "))
# Algorithm checks if number is correct
if guess == number:
    print("That's right! You win!")
else:
    i = 0
    while guess != number:
        i = i + 1
        j = 0
        guess = str(guess)
        number = str(number)
        # Check which numbers are correct and mark incorrect with 'N'
        guessy = ['N']*4
        # Make sure you check each digit, so run loop 4 times
        for q in range(0, 4):
            if guess[q] == number[q]:
                j += 1
                guessy[q] = guess[q]
            else:
                continue
        # If only some digits are correct then run next condition
        if j < 4 and j != 0:
            print("You have " + str(j) + " digit(s) right.")
            print("These numbers were correct")
            for m in guessy:
                print(m, end= " ")
            # Ask for next input
            guess = int(input("What is your next guess? "))
        # No digit(s) correct.
        elif j == 0:
            print("None of these digits are correct.")
            guess = int(input("What is your next guess? "))
    if guess == number:
        print("It took you " + str(i) + " tries to win!")