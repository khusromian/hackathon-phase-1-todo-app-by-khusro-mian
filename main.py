import sys
import os

# Ensure src is in the python path
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from todo.service import TodoService
from todo.cli import TodoCLI

def main():
    service = TodoService()
    cli = TodoCLI(service)
    cli.run()

if __name__ == "__main__":
    main()
