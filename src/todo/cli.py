import sys
from .service import TodoService

class TodoCLI:
    def __init__(self, service: TodoService):
        self.service = service

    def run(self):
        print("Welcome to Phase I Todo App!")
        while True:
            self.display_menu()
            choice = input("\nChoose an option: ").strip()

            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.list_tasks()
            elif choice == "3":
                self.mark_complete()
            elif choice == "4":
                self.update_task()
            elif choice == "5":
                self.delete_task()
            elif choice == "6":
                print("Goodbye!")
                sys.exit(0)
            else:
                print("Invalid choice. Please try again.")

    def display_menu(self):
        print("\n--- TODO MENU ---")
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. Mark Task Complete")
        print("4. Update Task Description")
        print("5. Delete Task")
        print("6. Exit")

    def add_task(self):
        description = input("Enter task description: ").strip()
        try:
            task = self.service.add_task(description)
            print(f"Task added with ID: {task.id}")
        except ValueError as e:
            print(f"Error: {e}")

    def list_tasks(self):
        tasks = self.service.list_tasks()
        if not tasks:
            print("No tasks found.")
            return

        print("\n--- YOUR TASKS ---")
        for task in tasks:
            status = "✓" if task.is_completed else " "
            print(f"[{status}] {task.id}: {task.description}")

    def mark_complete(self):
        task_id_str = input("Enter Task ID to complete: ").strip()
        try:
            task_id = int(task_id_str)
            self.service.complete_task(task_id)
            print("Task marked as complete.")
        except ValueError:
            print("Error: Invalid ID format.")
        except KeyError as e:
            print(f"Error: {e}")

    def update_task(self):
        task_id_str = input("Enter Task ID to update: ").strip()
        description = input("Enter new description: ").strip()
        try:
            task_id = int(task_id_str)
            self.service.update_task(task_id, description)
            print("Task updated.")
        except ValueError as e:
            print(f"Error: {e}")
        except KeyError as e:
            print(f"Error: {e}")

    def delete_task(self):
        task_id_str = input("Enter Task ID to delete: ").strip()
        try:
            task_id = int(task_id_str)
            self.service.delete_task(task_id)
            print("Task deleted.")
        except ValueError:
            print("Error: Invalid ID format.")
        except KeyError as e:
            print(f"Error: {e}")
