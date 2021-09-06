# we can iterate ver collections

l = [5,4,3, True, (1,), 'hi']

for item in l: # colon indicate start of a block of code
    print(type(item))
    print(item) # each line of the code block is indented

# the code block ends when the indentation stops

# we can also use a range object for iteration
r = range(99) # NB stops before 99, i.e 98
print(r, type(r))

# we can use a range to generate values
for i in range(-9, 10, 3): # start, stop-before, step
    print(i)

# we can iterate over collections
s = 'not long until lunch time'
d = {'name':'Ada', 'age':146, 'member':True}

for c in s:
    print(c)

for item in d: # careful - dict is NOT indexed by number
    print(item, d[item])

for key, value in d.items(): # remember items() and values() are available on dictionaries
    print(key, value)

# using range for efficiency - at no point do all the values exist in memory
total = 0
for i in range(1000000): # stop BEFORE 1000000
    total += i

print(total)

# we can generate members as we need them - odd syntax!!
my_gen = ( num**0.5 for num in range(-10*100, 10*100) ) # a tuple generator
print(type(my_gen))
# we can then use our custom generator in an iteration
for r in my_gen:
    print(r)

# mini challenge - please generate all the even numbers 0-100 (without using step)
evens = (num*2 for num in range(0,51))
for e in evens:
    print(e)

# here it is using step!!
evens = range(0, 101, 2)
for e in evens:
    print(e)

# we can combine 'if' logic in custom generators
evens = (num for num in range(0,100) if num%2 == 0)
for e in evens:
    print(e)