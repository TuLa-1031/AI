import random

def play():
    guessing_taken = 0
    number = random.randint(1,10)
    for guessing_taken in range(6):
        print('guess it')
        guess = input()
        guess = int(guess)
        if guess < number:
            print('my number is a bit higher')
        if guess > number:
            print('My number is a bit lower')
        if guess == number:
            break
    guessing_taken = guessing_taken + 1
    if guess == number:
        print("Congratulations! That's right. You had guessed ", + guessing_taken ," time.")
    if guess != number:
        print("Oh no, it's ",+ number)

if __name__ == '__main__':
    play()