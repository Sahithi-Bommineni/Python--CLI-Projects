print("-----Todo List-----")
#tasks=[]
while True:
    option=input("What would you like to do?\nAdd, Show, Edit, Complete or Exit? ").lower()
    match option:
        case 'add':
            todo = input("Enter todo: ") + "\n"
            file = open('todolist.txt','r') #open or create file
            tasks = file.readlines() #read the file
            file.close()
            tasks.append(todo)
            file = open('todolist.txt','w') 
            file.writelines(tasks) #write into file
            file.close()
            #print(tasks)
        case 'show':
            file = open('todolist.txt','r')
            tasks = file.readlines()
            for i,task in enumerate(tasks):
                print(i+1,"",task.title())
            file.close()
        case 'edit':
            file = open('todolist.txt','r')
            tasks = file.readlines()
            file.close()
            for i,task in enumerate(tasks):
                print(i+1,"",task.title())
            n=int(input("mention task number to edit: "))
            n=n-1
            newtask = input("Enter new task: ")
            file = open('todolist.txt','w') 
            file.writelines(tasks) #write into file
            file.close()
            tasks[n]= newtask
        case 'complete':
            for i,task in enumerate(tasks):
                print(i+1,"",task.title())
            n=int(input("mention task number to edit: "))
            n=n-1
            tasks.pop(n)
        case 'exit':
            break
        case unknown:
            print("Hey! You entered invalid option")
