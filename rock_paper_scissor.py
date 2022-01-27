import random

def play():
    user=input(" Whats Your Choice? 'r' for ROCK, 'p' for PAPER,and 's' for SCISSORS ")
    computer=random.choice(['r','p','c'])

    if user==computer:
        return 'Its a TIE'
    if is_win(user,computer):
        return 'You WON'

    return 'You LOSS'

def is_win(user,computer):
    #returns true if user wins
    #r>s,s>p,p>r
    if (user=='r' and computer=='s') or (user=='s' and computer=='p') or (user=='p' and computer=='r'):
        return True

print(play())