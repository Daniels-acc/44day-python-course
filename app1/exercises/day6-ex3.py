# Coding Exercise 3
# Please download the members.txt file from the resources of this article.
# Then, create a program that, whenever executed, asks the user to enter a new member in the command line:
#  Add a new member: Solomon Kane
# Then, the member is added to members.txt. In this case, the text file content would be:

member_input = str(input("Enter a new member: ")) +'\n'

file = open('src/members.txt', 'r')
temporary = file.readlines()
file.close()

temporary.append(member_input)
file = open('src/members.txt', 'w')
file.writelines(temporary)
file.close()

