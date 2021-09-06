# determine if a number is larger or smaller than another number
a = int(float(input('first number? ')))
b = int(float(input('second number? ')))

if a<b: # == tests equality, <=, >=, != all work as expected
    print('first is less than second')
elif b<a: # elif means 'else if'
    print('second is less than first')
else:
    print('probably the same number')

