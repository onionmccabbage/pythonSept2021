# recently Python has adopted class-based coding
# NB ALL things in Python are objects, even classes

# Python classes can be very simple (to the point of being useless)
class Thing():
    pass

# a Person class
class Person():
    '''
    Explain the class in the docstring
    This Person class delcares the properties of a person
    Name (string), Age (+ve int), Email (string)
    Classes also encaplulate functions (called methods)
    e.g. print out the person details nicely
    '''
    # the __init__ method is OPTIONAL!!!! but if present it MUST take self as an argument
    def __init__(self, name, email, age): # this runs automatically when we make an instance
        self.name = name
        self.email = email
        self.age = age
    # if we need to, we can add functions to our class (known as methods - things the class can do)
    def showDetailsNicely(self): # all class methods MUST take self as an argument
        # we can nicely format the properties of this class
        return 'Name {0} Email {1} Age {2} years'.format(self.name, self.email, self.age)
    # we have the option of providing accessor and mutator methods (getter and setter)
    def getAge(self):
        return self.age
    def setAge(self, new_age): # we need to provide a new value for the age
        # we can check the provided value is within bounds (positive integer)
        if isinstance(new_age, int) and new_age > 0: # or if type(new_age) == int
            # all good
            self.age = new_age
        else:
            pass # make no changes!
    # mini challenge - declare getter and setter for the name - must ne a non-emoty string
    # also write a couple of lines ot exercise your code
    def getName(self):
        return self.name
    def setName(self, new_name):
        # check the provided value is a non-empty string
        if isinstance(new_name, str) and new_name != '':
            self.name = new_name
        else:
            pass

if __name__ == '__main__':
    # we can make instances of our classes
    t = Thing()
    p = Person('Timnit', 't@g.ie', 42) # this will automatically run the __init__ method
    p.age = 24 # we can directly access members of the class
    print(p.name, p.email, p.age)
    print(p.showDetailsNicely())
    # exercise the name get/set methods
    p.setName('Ethel')
    p.setName('')
    p.setName(True)
    print(p.getName()) # expect 'Ethel'

    # try to mutate the age using the setter method
    p.setAge(999)
    p.setAge('32')
    p.setAge(-64)
    print(p.getAge()) # expect 999
    









    # unpacking
    # t = (p, 'hello', False)
    # print(t, *t)