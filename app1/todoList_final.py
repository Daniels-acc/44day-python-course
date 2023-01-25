todoList_list = []
todoList_completed = []

def chooseItem():
    return int(input('Enter number of item: '))

def checkTodoLength():
    return len(todoList_list)

def addItem():
        inputNum = int(input('Enter how many items you want to add: '))
        i = 1

        while i <= inputNum :
                stri = str(i)
                item = input('Enter enter no. ' + stri + ': \n')

        # READING AND WRITTING TO .txt FILE #
                todoList_file = open('src/todos.txt', 'r') # open txt todoList_file and start read session
                todoList = todoList_file.readlines() #read lines from .txt to see what's inside txt file
                todoList_file.close() # end read session

                todoList.append(str(item.title())) # after we see what's inside, we can append to file

                todoList_file = open('src/todos.txt', 'w') # open todoList_file and start w - write session ///
                todoList_file.writelines(todoList) # write appended item to todoList
                todoList_file.close() # end write session
                i+=1

def deleteItem():
    showItem()
    num = chooseItem()
    for item in todoList_list:
        print(todoList_list[num - 1] + ' successfully deleted.')
        todoList_list.pop(num - 1)
        break

def showItem():
    todoList_file = open('src/todos.txt', 'r')  # open txt todoList_file and start read session
    todolist = todoList_file.readlines()  # read lines from .txt to see what's inside txt file
    todoList_file.close()  # end read session

    print(todolist)


    # if checkTodoLength() == 0:
    #     print ("")
    # else:
    #     print('Items: ')

    #     for i, item in enumerate(todoList_list):
    #         print(f"{i+1}. {item}")
    # sortList = input("-- To sort the list, type sort or exit: ")
    # try:
    #     match sortList:
    #         case 'sort':
    #             todoList_list.sort()
    #         case 'exit':
    #             print('Exiting')
    # except:
    #     print("")



def editItem():
    showItem()
    num = chooseItem()
    for item in todoList_list:
        newItem = input('Enter new item: ')
        print('New item: ' + newItem.title())
        todoList_list[num - 1] = newItem.title()
        break

def completeItem():
    showItem()
    i=0
    try:
        while i < len(todoList_list):
            num = chooseItem()
            todoList_completed.append(todoList_list[num - 1])
            todoList_list.pop(num - 1)
            showItem()
            for item in todoList_list:
                print(todoList_list[num - 1] + ' completed.')
                break
            break
    except:
        print(f"{'Please enter number less than: '}{len(todoList_list)}.")
        completeItem()

def showCompleted():
    for i, item in enumerate(todoList_completed):
        print(f"{i+1}. {item}")


while True:
    userAction = input('Choose an action: "add", "delete", "show", "edit", "complete", "show completed" or "exit": ').lower()
    match userAction:
        case 'add':
            addItem()
        case 'delete':
            deleteItem()
        case 'show':
            showItem()
        case 'edit':
            editItem()
        case 'complete':
            completeItem()
        case 'showc':
            showCompleted()
        case 'exit':
            break

print('End. Goodbye.')










