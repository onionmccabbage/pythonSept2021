# here is a Python comment
a = 3 # an integer
b = 7

# NB in Python 2 division is INTEGER division
c = a/b # this is a floating point value
c = b/a
c = b**a
c = b//a # this returns the integer part of division
c = b%a # returns the remainder
c = 'hello' # a string of characters
print(c) 

# python is restricted ONLY by resources
# g = 10**100000
# print(g)

# collections are zero-based, accessed with square brackets
s = 'here is a string of characters'
print( s[13:18:2] ) # [start:stop-before:step]
# reverse
print(s[::-1])

# Lists and Tuples
l = [6, False, 5, (8,8,8), 'char', 3.21, [4,3,2]] # this is a list, which is MUTABLE
t = (6, False, 5, [], 'hello') # this is a tuple, which is IMMUTABLE

l[4] = 'Char' # NB strings are immutable
l[6][1] = True
# t[1] = 99 # fails

print(l)

print( type(c), type(l), type(t) )

# we can get user input like this
u = input('Is it coffee time yet?') # input is ALWAYS a string
print(type(u))
# we should check before attempting a cast
w = float(u) # we can try to type cast
x = int(u)
print(type(w), w, type(x), x)