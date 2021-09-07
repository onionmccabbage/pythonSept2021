# data can be passed around by reference or by value
# simple data types always pass by value

a = 1 # a has a value
b = a # b now has the value it got from a
a += 2 # we mutate the value of a
print(a,b) # does the valeu of b change?

# by ref - complex structures pass by reference
m = [8,7,6]
p = m
m[1] = 77
print(m, p)