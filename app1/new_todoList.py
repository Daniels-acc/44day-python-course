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
            todos = file.readlines() # need to have this variable to store the data
            file.close()

            todos.append(todo_input) # variable to append to list

            file = open('src/todos.txt', 'w') # it will overwrite the existing file and start session of writing,
            # creates the file if it does not exist
            file.writelines(todos)
            file.close()

        case 'read':
            file = open('src/todos.txt', 'r')
            todos = file.readlines() # ovo je kao da smo napisali todos = [lista neka]
            file.close()

            new_todos = []

            for item in todos:
                new_item = item.strip("\n")
                new_todos.append(new_item)

            print(f"Ovo printa listu:  {todos}")
            print("List of todos: ")
            for index, item in enumerate(new_todos): #iterate through that todo list and prints it
                row = f"{index + 1}. {item.title()}"
                print(row)



