# we use range, generator and comprehension to efficiently work with large collections

# comprehensions iterate through a generator

# a list generator (comprehensively iterate over the values and store in a list)
num_l = [num for num in range(0,100, 5)]
print(num_l) # we have a list
# a generator (comprehensively iterate over the calues without persisting in memory)
num_g = (num for num in range(0,100, 5))
print(num_g) # we have a generator
# we can use a generator to generate the values we need without persisting them in memory
for i in num_g:
    print(i, end = ', ') # default is new line but we can terminate print with anything we like


# we can comprehensively iterate over every member of a dictionary
phrase = 'are we there yet?'
# we can use a dictionary comprehension
counts = {letter: phrase.count(letter) for letter in phrase}
print(counts, type(counts))

# comprehesions always have this form (the 'if' is optional):
# (expression or item in iterable if condition)
# [expression or item in iterable if condition] # list comprehension
# {expression or item in iterable if condition} # dict comprehension

# set comprehension
my_set = {number for number in range(1,12) if number % 3 == 1} # persists in memory
print(my_set)