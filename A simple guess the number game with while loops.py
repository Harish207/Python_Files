from random import randrange

random_number = randrange(1, 10)

count = 0
# Start your game!
while (count<3):
    guess = int(raw_input("Enter Guess:"))
    count += 1
    if (guess == random_number):
        print "You win!"
        break
else:
    print "You lose"
