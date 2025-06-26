print("-----Todo List-----")
tasks=[]
while True:
    option=input("What would you like to do?\nAdd, Show, Edit, Complete or Exit?").lower()
    match option:
        case 'add':
            todo = input("Enter todo:")
            tasks.append(todo)
            print(tasks)
        case 'show':
            print(tasks)
        case 'complete':
            print(tasks)
            n=input("which task do you want to mark complete? (mention task number)")
            
        case 'exit':
            break
