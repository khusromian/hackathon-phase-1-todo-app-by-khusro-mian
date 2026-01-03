# Service Interface: TodoService

The `TodoService` is the primary interface for managing tasks.

## Methods

### add_task(description: str) -> Task
- **Input**: text description (non-empty).
- **Return**: The created `Task` object.
- **Errors**: `ValueError` if description is empty.

### list_tasks() -> List[Task]
- **Return**: A list of all tasks.
- **Note**: Should return an empty list if no tasks exist.

### get_task(task_id: int) -> Task
- **Input**: Integer ID.
- **Return**: The `Task` object.
- **Errors**: `KeyError` if task_id does not exist.

### update_task(task_id: int, description: str) -> Task
- **Input**: Integer ID, new description.
- **Return**: The updated `Task` object.
- **Errors**: `KeyError` if ID missing, `ValueError` if description empty.

### complete_task(task_id: int) -> Task
- **Input**: Integer ID.
- **Return**: The updated `Task` object (`is_completed=True`).
- **Errors**: `KeyError` if ID missing.

### delete_task(task_id: int) -> None
- **Input**: Integer ID.
- **Errors**: `KeyError` if ID missing.
