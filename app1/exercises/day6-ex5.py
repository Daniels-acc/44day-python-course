# Coding Exercise 5
# Please download the three text files a.txt, b.txt, and c.txt from the resources.
# Then, create a program that reads each text file and prints out the content of each in the command line.

files = ['src/a.txt','src/b.txt', 'src/c.txt']

for item in files:
    file = open(item, 'r')
    x = file.read()
    print(x)
    file.close()