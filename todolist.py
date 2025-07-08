print("-----Todo List-----")
#tasks=[]
while True:
    option=input("What would you like to do?\nAdd, Show, Edit, Complete or Exit? ").lower()
    match option:
        case 'add':
            todo = input("Enter todo: ") + "\n"
            with open('todolist.txt','r') as file: #open or create file
                tasks = file.readlines() #read the file
            #file.close() --> when using with open, we dont need to close explicitly
            tasks.append(todo)
            file = open('todolist.txt','w') 
            file.writelines(tasks) #write into file
            file.close()
            #print(tasks)
        case 'show':
            with open('todolist.txt','r') as file:
                tasks = file.readlines()
            for i,task in enumerate(tasks):
                print(i+1,"",task.title())
        case 'edit':
            with open('todolist.txt','r') as file:
                tasks = file.readlines()
            for i,task in enumerate(tasks):
                print(i+1,"",task.title())
            n=int(input("mention task number to edit: "))
            n=n-1
            newtask = input("enter task: ")
            newtasks = []
            for task in tasks:
                if task[n] in task:
                    newtasks.append(task.replace(task,newtask))
                else:
                    newtasks.append(task[n])
            with open('todolist.txt','w') as file:
                file.writelines(newtasks) #write into file
        case 'complete':
            with open('todolist.txt','r') as file:
                tasks = file.readlines()
            for i,task in enumerate(tasks):
                print(i+1,"",task.title())
            n=int(input("mention task number to edit: "))
            n=n-1
            file = open('todolist.txt','w') 
            file.writelines(tasks) #write into file
            tasks.remove(n)
            file.close()
        case 'exit':
            break
        case unknown:
            print("Sorry! You entered invalid option. Please try again.")
