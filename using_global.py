# the module itself is called the 'global' scope
g = 'in the global namespace' # NB in Python we aim to avoid over-use of the global scope

def someFn(): # every block of code has it's own scope
    global g # now we have a reference to the 'g' in the global scope
    g = 'in the function code block namespace'
    print(g)

if __name__ == '__main__':
    print(g)
    someFn()
    print(g)