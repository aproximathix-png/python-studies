restart = True
tasklist = []
while restart:

    print("#### Welcome to the To-Do List Manager ####")
    print   ("1. Add a task")
    print   ("2. View tasks")  
    print   ("3. Remove a task")
    print   ("4. Exit")
    answer = int(input("You chose: "))
    if answer == 1:
        print('what task do you want to add?')
        task = input()
        x = task.strip()
        if x == "":
            print("task can't be empty")
        else:
            tasklist.append(task)
        



    if answer == 2: 
        if (len(tasklist) == 0):
             print("you dont have task yet")
        for index, value in enumerate(tasklist):
             print(f'{index}: {value}')
            

    if answer == 3:
        delete = input("Which task do you want to remove? ")
        if delete in tasklist:
            tasklist.remove(delete)
        elif delete.isdigit() and int(delete) < len(tasklist):
            tasklist.pop(int(delete))
            print("Task removed successfully")
        else:
            print("Task not found")

    if answer == 4:
        print("Thank you for using our To-Do List Manager")
        break
    if answer > 4 or answer < 1:
        print("error you put the wrong number")