def display_menu():
    print("MENU")
    print("1. Add task")
    print("2. View task")
    print("3. Mark as done")
    print("4. Exit")
    
def add_task(tasks):
    task=input("Enter task name: ").strip()
    if task:
        tasks.append(task)
        print("Task added successfully")
    else:
        print("Task name cannot be empty!")
        
def view_task(tasks):
    if tasks:
        print("\nTasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    else:
        print("! No task avlable")
        
def mark_task_done(tasks):
    if not tasks:
        print("! No tasks to mark as done")
        return
    view_task(tasks)
    
    try:
        index= int(input("Enter task index to mark as done: "))-1
        if 0<= index< len(tasks):
            remove_task= tasks.pop(index)
            print(f"Tasks{remove_task} mark as done and removed.")
            
    except ValueError:
        print("! Please enter a valid number")
        
def save_task(tasks):
    with open ("tasks.txt","w") as f:
        for task in tasks:
            f.write(task+"\n")
            
def load_tasks():
    try:
        with open("tasks.txt", "r") as f:
            return f.read().splitlines()
    except FileNotFoundError:
        return []
    
def main():
    tasks= load_tasks()
    while True:
        display_menu()
        choice= input("Enter your choice: ")
        if choice=="1":
            add_task(tasks)
        elif choice=="2":
            view_task(tasks)
        elif choice== "3":
            mark_task_done(tasks)
        elif choice== "4":
            print("Exiting and saving tasks....")
            save_task(tasks)
            break
        else:
            print("Invalid choice, please enter a valid option.")
            
if __name__== "__main__":
    main()