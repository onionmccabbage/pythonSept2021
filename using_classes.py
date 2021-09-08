# recently Python has adopted class-based coding
# NB ALL things in Python are objects, even classes

# Python classes can be very simple (to the point of being useless)
class Thing():
    pass

# a Person class
class Person(): # implicitly inherits from 'object'
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
        self.__email = email # not directly accessible
        self.__age = age # using __age is called 'name mangling' and prevents direct access to the property
    # if we need to, we can add functions to our class (known as methods - things the class can do)
    def showDetailsNicely(self): # all class methods MUST take self as an argument
        # we can nicely format the properties of this class
        return 'Name {0} Email {1} Age {2} years'.format(self.name, self.__email, self.__age)
    # we have the option of providing accessor and mutator methods (getter and setter)
    def getAge(self):
        return self.__age
    def setAge(self, new_age): # we need to provide a new value for the age
        # we can check the provided value is within bounds (positive integer)
        if isinstance(new_age, int) and new_age > 0: # or if type(new_age) == int
            # all good
            self.__age = new_age
        else:
            pass # make no changes!
    # mini challenge - declare getter and setter for the name - must ne a non-emoty string
    # also write a couple of lines to exercise your code
    def getName(self):
        return self.name
    def setName(self, new_name):
        # check the provided value is a non-empty string
        if isinstance(new_name, str) and new_name != '':
            self.name = new_name
        else:
            pass
    @property # decorator syntax - built in to python
    def email(self): # the method name must match the property
        return self.__email # return the __email property as if it was a property called 'email'
    @email.setter # behaves as if 'email' is a directly mutable property, but actually calls this method
    def email(self, new_email):
        if isinstance(new_email, str) and new_email !='':
            self.__email = new_email
        else:
            pass

if __name__ == '__main__':
    # we can make instances of our classes
    t = Thing()
    p = Person('Timnit', 't@g.ie', 42) # this will automatically run the __init__ method
    p.age = 24 # we cannot directly access this member of the class - instead makes an arbtrary property!!!
    p.__age = 24 # nope - cannot mutate __age directly
    # p.email actually invokes the email property setter method
    print(p.name, p.email, p.age) # careful - age is NOT the internal __age it is an arbitrary property of this object
    print(p.showDetailsNicely())
    # exercise the email get/set methods
    p.email = 'changed@g.ie'
    p.email = 2 # fails silently
    p.email = ''
    print(p.email) # this uses the @property method

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