# a tuple is an indexed immutable collection of any types

t = (5, True, 3, 'oooh')
l = [5, True, 3, 'oooh']
s = 'can we unpack strings?'

# we can use tuple unpacking like this
w, x, y, z = t
# and also list unpacking
m, n, o, p = l

# a, b, c = s # fails = we cannot unpack a string

print(y, z, m, n)