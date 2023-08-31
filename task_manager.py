class Task:
    def __init__(self, description):
        self.description = description

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)

    def view_tasks(self):
        for idx, task in enumerate(self.tasks):
            print(f"{idx + 1}. {task.description}")

def main():
    manager = TaskManager()

    while True:
        print("\nTask Management System")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            description = input("Enter task description: ")
            manager.add_task(description)
        elif choice == '2':
            index = int(input("Enter task index to remove: ")) - 1
            manager.remove_task(index)
        elif choice == '3':
            manager.view_tasks()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
