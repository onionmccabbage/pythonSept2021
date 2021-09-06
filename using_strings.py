# we can have 'placeholder' code 
def not_complete_yet():
    pass # pass is a handy way to place-hold until you get round to finishing it

# we can use break, continue and quit
def doStuff():
    for i in range(0,10):
        quit() # quit is a function to quit the current loop
        print('all done {}'.format(i))
        continue # continue is a keyword statement

# doStuff()
# we can manipulate strings
# remember - strings are immutable
s = '   all done   '
print(s.upper().strip()) # this has NOT altered the original string
print(s)
altered = s.strip().upper()
print(altered)