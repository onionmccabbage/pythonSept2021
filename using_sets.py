# a set is like a dictionary but with no keys (just unique values)

s = {4,4,4,3,2,'lunch', True, 1,3.2} # s = set()
s.add(8)

print(s)

# there are NO ordinal positions, so iterate with care
for item in s:
    print(item in s) # NOT a predictable order

q = input('guess a value in the set: ') # every input is always a string
if q in s:
    print('correct, the string {} exists in the set'.format(q))
elif q.isnumeric() and float(q) in s: # also isalpha etc.
    print('correct, the number {} exists in the set'.format(q))
elif q=='True' and True in s:
    print('correct, the boolean {} exist in the set'.format(q))
elif q=='False' and False in s: # CAREFUL - lots of things evaluate to False
    print('correct, the boolean {} exist in the set'.format(q))
else:
    print('no, the value {} does not exist in the set'.format(q))

