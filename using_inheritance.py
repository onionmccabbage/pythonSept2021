# classes can iherit from other classes
# so they get ALL the stuff from the parent class

# we can import a class from another module
from using_classes import Person

# imagine a 'Code' class, which is a Person, plus 'language' skills
class Coder(Person):
    def __init__(self, name, email, age, date_joined, access_level, language):
        super().__init__(name, email, age, date_joined, access_level) # call the parent class initializer
        self.language = language

if __name__ == '__main__':
    c = Coder('Ada', 'a@b.ie', 103,  1, 'user', 'python')
    print(c, c.language)
