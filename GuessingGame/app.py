import random 


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
       guess = int(input(f"Guess a number between 1 and {x}: "))
       if guess < random_number:
          print('Your guess is too low, try again')
       elif guess > random_number:
          print('The number is too high, try again')
       else:
          print('You got it!!!')


guess(10)



