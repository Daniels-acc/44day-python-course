# Coding Exercise 2
# Write a program that reads the essay.txt file
# and returns the number of characters contained in the file.

file = open('src/essay.txt', 'r')
temporary = file.read()
file.close()

print(len(temporary))