# Python can read and write ANY file type, since all files are ultimately binary files
# NB encoding as binary is ALWAYS more efficient than encoding as text

def main():
    # we need some binary data
    b = bytes( range(0,256) ) # all the binary values from 0 to 255
    # print(b)
    # here we make a file access object
    fout = open('binfile', 'wb') # 'w' for over(w)rite and 'b' for binary
    # ... and use it to write our binary to the output file
    fout.write(b)
    fout.close()
    # we can read our data back...
    fin = open('binfile', 'rb') # 'r' for read, 'b' for binary
    retrieved_b = fin.read()
    print(retrieved_b)
    fin.close() # always tidy up!!

if __name__ == '__main__':
    main()