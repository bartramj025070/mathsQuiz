fileName = input("File name >>  ")
with open(fileName, 'w') as f:
    f.write("hi!")
    f.close()