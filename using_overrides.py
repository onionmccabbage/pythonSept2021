# we can override ANY of Pythons built-ins (they all start with __)

# in this case, we override the equality operator
class Word():
    '''
    Take a string and make it case-blind when comparing for equality
    '''
    def __init__(self, text):
        self.text = text
    # here we override the built in equality operator
    def __eq__(self, other_word):
        return self.text.lower() == other_word.text.lower()

# __ne__ not equal
# __gt__ greater than
# __lt__ less than
# __ge__ and __le__ greater-or-equal and less-or-equal

# other 'magic methods'
# __add__( self, other ) self + other
# __sub__( self, other ) self - other
# __mul__( self, other ) self * other
# __floordiv__( self, other ) self // other
# __truediv__( self, other ) self / other
# __mod__( self, other ) self % other
# __pow__( self, other ) self ** other
# __len__ is the length of the object

if __name__ == '__main__':
    # normal sring comparison
    lower = 'hello'
    upper = 'HELLO'
    print(lower == upper) # False
    # our new string comparison
    w_lower = Word('hello')
    w_upper = Word('HELLO')
    print(w_lower == w_upper) # True
    # we can access the built-in doc string
    print(w_lower.__doc__)