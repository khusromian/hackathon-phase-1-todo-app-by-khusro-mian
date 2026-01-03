from typing import List, Dict
from .models import Task

class TodoService:
    def __init__(self):
        self.tasks: Dict[int, Task] = {}
        self._next_id: int = 1

    def add_task(self, description: str) -> Task:
        if not description.strip():
            raise ValueError("Description cannot be empty")

        task = Task(id=self._next_id, description=description)
        self.tasks[self._next_id] = task
        self._next_id += 1
        return task

    def list_tasks(self) -> List[Task]:
        return list(self.tasks.values())

    def complete_task(self, task_id: int) -> Task:
        if task_id not in self.tasks:
            raise KeyError(f"Task ID {task_id} not found")

        task = self.tasks[task_id]
        task.is_completed = True
        return task

    def update_task(self, task_id: int, description: str) -> Task:
        if task_id not in self.tasks:
            raise KeyError(f"Task ID {task_id} not found")
        if not description.strip():
            raise ValueError("Description cannot be empty")

        task = self.tasks[task_id]
        task.description = description
        return task

    def delete_task(self, task_id: int) -> None:
        if task_id not in self.tasks:
            raise KeyError(f"Task ID {task_id} not found")
        del self.tasks[task_id]
