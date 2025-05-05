"""
todo.py - CLI-Based To-Do List Manager

Description:
Main CLI program for managing tasks using a doubly linked list.
Supports adding, deleting, sorting tasks, and undo/redo actions.

Dependencies:
- linked_list.py (Task storage)
- sorting.py (Sorting algorithms)
- undo_redo.py (Undo/redo actions)
"""

from linked_list import TaskList
from undo_redo import UndoRedo

task_list = TaskList()
undo_redo = UndoRedo()

while True:
    command = input("Enter command (add/delete/show/undo/redo/exit): ").strip().lower()

    if command == "add":
        title = input("Task title: ")
        priority = int(input("Priority (1-3): "))
        deadline = input("Deadline (YYYY-MM-DD or None): ")
        task_list.add_task(title, priority, deadline)
        undo_redo.add_action("add", title)
        print(f"Task '{title}' added.")
    
    elif command == "delete":
        title = input("Task title to delete: ")
        result = task_list.delete_task(title)
        undo_redo.add_action("delete", title)
        print(result)
    
    elif command == "show":
        task_list.display_tasks()
    
    elif command == "undo":
        print(undo_redo.undo())

    elif command == "redo":
        print(undo_redo.redo())

    elif command == "exit":
        print("Goodbye!")
        break

    else:
        print("Invalid command.")


