print("-----Todo List-----")
tasks=[]
while True:
    option=input("What would you like to do?\nAdd, Show, Edit, Complete or Exit? ").lower()
    match option:
        case 'add':
            todo = input("Enter todo: ")
            tasks.append(todo)
            #print(tasks)
        case 'show':
            for i,task in enumerate(tasks):
                print(i+1,"",task.title())
        case 'edit':
            for i,task in enumerate(tasks):
                print(i+1,"",task.title())
            n=int(input("mention task number to edit: "))
            n=n-1
            newtask = input("Enter new task: ")
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
