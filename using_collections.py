# lists
l = [7,6,5,4,3] # or list()
l.append(99)
l.insert(1, 'new')
w = l.pop()
x = l.remove('new')
print(l, w, x)

# tuple
t = tuple(l)
print(t[0:4], type(t))
# careful - a one-member tuple
t = (3,) #  a tuple
print(type(t))

# Dictionary - a non-indexed collection of values as name:value
d = {'first':'Timnit', 'last':'Gebru', 'age':42, 'member':True} # or d = dict()
print(d['member'])
d['status'] = l
print(d.keys(), d.values(), type(d))