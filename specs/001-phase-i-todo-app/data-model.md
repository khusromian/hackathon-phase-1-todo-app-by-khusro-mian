# Data Model: Phase I Todo App

## Entities

### Task
Represents a single todo item in the system.

| Field | Type | Description |
|-------|------|-------------|
| id | int | Unique identifier (auto-increment) |
| description | str | The content of the todo item |
| is_completed | bool | Status of the task (default: False) |

## State Transitions

- **Created**: Status is `is_completed=False`.
- **Completed**: Transition `is_completed` from `False` to `True`.
- **Reopened**: (Optional/Future) Transition from `True` back to `False`.
- **Deleted**: Removed from the in-memory dictionary.
