def read_file(filename,filearg='r'):
    with open(filename+'.txt',filearg) as file:
        tasks = file.readlines()
    return tasks

def write_file(filename,tasks,filearg='w'):
    with open(filename+'.txt',filearg) as file:
        file.writelines(tasks)


print("-----Todo List-----")
#tasks=[]
while True:
    option=input("What would you like to do?\nAdd, Show, Edit, Complete or Exit? ").lower()
    match option:
        case 'add':
            todo = input("Enter todo: ") + "\n"
            tasks = read_file("todolist","r")
            # with open('todolist.txt','r') as file: #open or create file
            #     tasks = file.readlines() #read the file
            #file.close() --> when using with open, we dont need to close explicitly
            tasks.append(todo)
            write_file("todolist",tasks,"w")
            # file = open('todolist.txt','w') 
            # file.writelines(tasks) #write into file
            # file.close()
            #print(tasks)
        case 'show':
            tasks = read_file("todolist","r")
            # with open('todolist.txt','r') as file:
            #      tasks = file.readlines()
            #read_file('todolist','r')
            for i,task in enumerate(tasks):
                print(i+1,"",task.title())
        case 'edit':
            try:
                tasks = read_file("todolist","r")
                # with open('todolist.txt','r') as file:
                #     tasks = file.readlines()
                for i,task in enumerate(tasks):
                    print(i+1,"",task.title())
                n=int(input("mention task number to edit: "))
                n=n-1
                if n<len(tasks):
                    newtask = input("enter task: ")
                    tasks[n]=newtask + "\n"
                    write_file("todolist",tasks,"w")
                else:
                    print("Invalid task input. Please try again.\n")
                    continue
            except ValueError:
                print("Invalid input, please try again.")
                continue
        case 'complete':
            # with open('todolist.txt','r') as file:
            #     tasks = file.readlines()
            # for i,task in enumerate(tasks):
            #     print(i+1,"",task.title())
            try:
                n=int(input("mention task number to edit: "))
                tasks = read_file("todolist","r")
                # with open('todolist.txt','r') as file:
                #     tasks = file.readlines()
                index=n-1
                if index<len(tasks):
                    task_to_remove = tasks[index].strip("\n")
                    tasks.pop(index)
                    write_file("todolist",tasks,"w")
                else:
                    print("Invalid task. Please try again.\n")
                    continue
            except ValueError:
                print("Invalid input, please try again.")
                continue
        case 'exit':
            break
        case unknown:
            print("Sorry! You entered invalid option. Please try again.\n")
