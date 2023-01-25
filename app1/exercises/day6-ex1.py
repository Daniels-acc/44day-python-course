# Coding Exercise 1
# Please download the essay.txt file from the resources of this article.
# Then, create a program that reads that file and prints out its text.
# The first letter of each word in the output should be uppercase.

file = open('src/essay.txt', 'r')
file_var = file.read()
file.close()

print(file_var.title())
