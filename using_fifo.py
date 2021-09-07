# we can read and write external files
def writeToFile():
    # we can simple print to a file via a file access object
    # 'a' means append to the file (create if needed)
    # 't' means treat it as a text file (the default)
    fout = open('my_file.txt', 'at') # 'w' means over(w)rite the file (create if needed)
    print('this ends up in a file also', file=fout) # we direct he print to a file access object
    fout.close() # tidy up

# we can write to a file in bits - not all at once
def elegant(data):
    try:
        fout = open('other.txt', 'xt') # 'x' means exclusive access
        size = len(data) # we now know how many characters we have
        offset = 0
        chunk = 24 # here we choose to write 24 characters at a time
        while True: # NB while will automatically close the file when done
            if offset > size:
                break
            else:
                fout.write(data[offset:offset+chunk]) # start:stop-before
                offset += chunk
    except Exception as e:
        print(e)
    finally:
        print('all done')

# reading data back from a file
def readText():
    # this is a file access object (not the actual file itself)
    fin = open('other.txt', 'r') # 'r' means read (t is the default for text)
    read = fin.read() # read the whole thing
    # read = fin.readline()+'----'+fin.readline() # read two lines
    print(read)

if __name__ == '__main__':
    writeToFile()
    s = '''
    we can use a while loop to automatically close a file access object
    This is useful when there is lots to write
    Also handy if we might get exceptions'''
    elegant(s)
    readText() # attempt to read the data from the file
