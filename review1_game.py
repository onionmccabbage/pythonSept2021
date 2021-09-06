# Python review exercise: guess the random number between 0-100
from random import randint # we need a way to make random numbers

def game():
    target = randint(0,100) # up to 100 inclusive
    # create collections of odds, evens, squares and primes
    odd_ints  = (number for number in range(0,101) if number % 2 == 1 )# do we really need this???
    even_ints = [number for number in range(0, 101, 2) ] # ooh a list
    squares_list = [ num**2 for num in range(0,11) ] # we need to include 100!!
    primes_t = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97)
    # set some boolean flags regarding the nature of our target number
    is_odd    = target in odd_ints
    is_even   = target in even_ints
    is_square = target in squares_list
    is_prime  = target in primes_t
    guess = 999 # give itan initial value out of range
    # run the game
    while guess != target:
        guess = int(input('guess:')) # make sure it's an int
        # conditionally act on the guess
        if guess == target: # did they get it right
            print('correct it was', target)
            # since guess now equals target, the while loop will end
        elif guess == -2: # do they want a clue
            print ('CLUE: odd:', is_odd, 'even:',is_even, 'square:',is_square, 'prime:', is_prime)
        elif guess == -1: # do they want to quit
            print ('it was', target)
            break # stops the current loop
        elif guess > target: # is the guess too high
            print('too high')
        elif guess < target: # is the guess too low (could be an else clause)
            print('too low')

game()