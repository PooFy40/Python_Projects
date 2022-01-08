import random

def guess(x):
    random_number=random.randint(1,x)
    guess=0

    while guess!=random_number:
        guess=int(input(f"Guess a number between 1 and {x}:-"))

        if guess<random_number:
            print('Try Again , Its to LOW.')
        elif guess>random_number:
            print('Try Again , Its to HIGH.')

    # print(f'Congratulation you WON , You guessed the number {random_number} correctly.')
# guess(10)

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while  feedback!='c':

        if high!=low:
            guess=random.randint(low,high)
        else:
            guess=low
        feedback=input(f'Is {guess} is too high(h),too low(l),or correct(c)').lower()

        if feedback == 'h':
            high=guess-1
        elif feedback == 'l':
            low=guess+1

    print(f'YEY,the computer guessed you secrate number {guess}')

computer_guess(1000)

