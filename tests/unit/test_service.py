import pytest

def test_add_task(todo_service):
    task = todo_service.add_task("Buy milk")
    assert task.id == 1
    assert task.description == "Buy milk"
    assert task.is_completed is False
    assert len(todo_service.list_tasks()) == 1

def test_add_empty_task(todo_service):
    with pytest.raises(ValueError, match="Description cannot be empty"):
        todo_service.add_task("")

def test_list_tasks(todo_service):
    assert len(todo_service.list_tasks()) == 0
    todo_service.add_task("T1")
    todo_service.add_task("T2")
    assert len(todo_service.list_tasks()) == 2

def test_complete_task(todo_service):
    task = todo_service.add_task("T1")
    completed_task = todo_service.complete_task(task.id)
    assert completed_task.is_completed is True

def test_complete_invalid_task(todo_service):
    with pytest.raises(KeyError, match="Task ID 999 not found"):
        todo_service.complete_task(999)

def test_update_task(todo_service):
    task = todo_service.add_task("T1")
    updated = todo_service.update_task(task.id, "Updated T1")
    assert updated.description == "Updated T1"

def test_update_invalid_task(todo_service):
    with pytest.raises(KeyError, match="Task ID 999 not found"):
        todo_service.update_task(999, "New")

def test_delete_task(todo_service):
    task = todo_service.add_task("T1")
    todo_service.delete_task(task.id)
    assert len(todo_service.list_tasks()) == 0

def test_delete_invalid_task(todo_service):
    with pytest.raises(KeyError, match="Task ID 999 not found"):
        todo_service.delete_task(999)
