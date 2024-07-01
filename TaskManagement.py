import datetime

class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False
        self.due_date = datetime.datetime.now()
        self.deadline = self.due_date.replace(hour=8, minute=0, second=0)

    def is_past_due(self):
        return datetime.datetime.now() > self.deadline

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)
        print('Task added successfully.')

    def view_task(self, description):
        for task in self.tasks:
            if task.description == description:
                status = '[ ✓ ]' if task.completed else '[X]' if task.is_past_due() else ''
                print("Description:", task.description, ", Completed:", task.completed, ", Due Date:", task.due_date, status)
                return
        print("Task " + description + " not found.")

    def view_tasks(self):
        if not self.tasks:
            print('No tasks available.')
        else:
            print('Current tasks:')
            for task in self.tasks:
                status = '[ ✓ ]' if task.completed else '[X]' if task.is_past_due() else ''
                print("Description:", task.description, ", Completed:", task.completed, ", Due Date:", task.due_date, status)

    def complete_task(self, description):
        for task in self.tasks:
            if task.description == description:
                task.completed = True
                print('Task ' + description + " marked as completed")
                return
        print("Task " + description + " not found.")

    def delete_task(self, description):
        for task in self.tasks:
            if task.description == description:
                self.tasks.remove(task)
                print("Task " + description + " deleted.")
                return
        print("Task " + description + " not found.")

def main():
    task_manager = TaskManager()
    while True:
        command = input('Enter a command (add, view, complete, delete) or "exit" to quit: ')
        
        if command == 'exit':
            break

        elif command == 'add':
            description = input('Enter the Task Description: ')
            task_manager.add_task(description)

        elif command == 'view':
            description = input('Enter the Task Description to view or press Enter to view all tasks: ')
            if description:
                task_manager.view_task(description)
            else:
                task_manager.view_tasks()

        elif command == 'complete':
            description = input('Enter the Task Description to mark as completed: ')
            task_manager.complete_task(description)

        elif command == 'delete':
            description = input('Enter the Task Description to delete: ')
            task_manager.delete_task(description)

        else:
            print('Invalid command. Please try again.')

if __name__ == "__main__":
    main()
