local_path = r'/\src'  # r - prije stringa da može čitati path

def readFile():
    file = open('src/todos.txt', 'r')
    todos = file.readlines()
    file.close()
    for index, item in enumerate(todos):
        row = f"{index + 1}. {item.title()}"
        print(row)


while True:
    user_action = input("Type 'create', 'read', 'update' or 'delete': ")
    user_action = user_action.strip()

    match user_action:

        case 'create':
            todo_input = str(input("Create todo item: ")) + "\n"

            file = open('src/todos.txt', 'r') # open todos.txt file - pens a file for reading, error if the file does not exist
            todos = file.readlines() # reads opened file - list file type
            file.close()

            todos.append(todo_input) # append items to that opened file and keeps existing in todos variable
            file = open('src/todos.txt', 'w') # it will overwrite the existing file and start session of writing,
            # creates the file if it does not exist
            file.writelines(todos)
            file.close()

        case 'read':
            readFile()

        case 'update':
            print('Choose an item to edit: ')
            file = readFile()


        case 'exit':
            print('Exiting')
            break