import os
import sys

# Add src to sys.path so 'todo' can be imported in tests
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

import pytest
from todo.service import TodoService

@pytest.fixture
def todo_service():
    return TodoService()
