import json
import os
import sys
from datetime import datetime

# File to store tasks
TASKS_FILE = "tasks.json"

def load_tasks():
    """Load tasks from the JSON file, create it if it doesn't exist."""
    if not os.path.exists(TASKS_FILE):
        return []
    try:
        with open(TASKS_FILE, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("Error: Invalid JSON in tasks file. Starting with empty tasks list.")
        return []

def save_tasks(tasks):
    """Save tasks to the JSON file."""
    try:
        with open(TASKS_FILE, 'w') as f:
            json.dump(tasks, f, indent=2)
    except Exception as e:
        print(f"Error saving tasks: {e}")
        sys.exit(1)

def generate_id(tasks):
    """Generate a unique ID for a new task."""
    return max([task['id'] for task in tasks], default=0) + 1

def add_task(description):
    """Add a new task with the given description."""
    tasks = load_tasks()
    task = {
        "id": generate_id(tasks),
        "description": description,
        "status": "todo",
        "createdAt": datetime.now().isoformat(),
        "updatedAt": datetime.now().isoformat()
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {task['id']})")

def update_task(task_id, description):
    """Update the description of a task with the given ID."""
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['description'] = description
            task['updatedAt'] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task {task_id} updated successfully")
            return
    print(f"Error: Task with ID {task_id} not found")

def delete_task(task_id):
    """Delete a task with the given ID."""
    tasks = load_tasks()
    initial_len = len(tasks)
    tasks = [task for task in tasks if task['id'] != task_id]
    if len(tasks) < initial_len:
        save_tasks(tasks)
        print(f"Task {task_id} deleted successfully")
    else:
        print(f"Error: Task with ID {task_id} not found")

def mark_task(task_id, status):
    """Mark a task with the given ID as in-progress or done."""
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = status
            task['updatedAt'] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task {task_id} marked as {status}")
            return
    print(f"Error: Task with ID {task_id} not found")

def list_tasks(status=None):
    """List tasks, optionally filtered by status."""
    tasks = load_tasks()
    if not tasks:
        print("No tasks found")
        return

    filtered_tasks = tasks
    if status:
        filtered_tasks = [task for task in tasks if task['status'] == status]
        if not filtered_tasks:
            print(f"No tasks found with status: {status}")
            return

    for task in filtered_tasks:
        print(f"ID: {task['id']}, Description: {task['description']}, "
              f"Status: {task['status']}, Created: {task['createdAt']}, "
              f"Updated: {task['updatedAt']}")

def print_usage():
    """Print usage instructions."""
    print("""
Usage: task-cli <command> [arguments]

Commands:
  add <description>          Add a new task
  update <id> <description> Update a task's description
  delete <id>               Delete a task
  mark-in-progress <id>     Mark a task as in-progress
  mark-done <id>            Mark a task as done
  list [status]             List tasks (optionally by status: todo, in-progress, done)
""")

def main():
    if len(sys.argv) < 2:
        print_usage()
        sys.exit(1)

    command = sys.argv[1].lower()

    try:
        if command == "add":
            if len(sys.argv) < 3:
                print("Error: Description is required")
                sys.exit(1)
            description = " ".join(sys.argv[2:])
            add_task(description)

        elif command == "update":
            if len(sys.argv) < 4:
                print("Error: ID and description are required")
                sys.exit(1)
            task_id = int(sys.argv[2])
            description = " ".join(sys.argv[3:])
            update_task(task_id, description)

        elif command == "delete":
            if len(sys.argv) != 3:
                print("Error: ID is required")
                sys.exit(1)
            task_id = int(sys.argv[2])
            delete_task(task_id)

        elif command == "mark-in-progress":
            if len(sys.argv) != 3:
                print("Error: ID is required")
                sys.exit(1)
            task_id = int(sys.argv[2])
            mark_task(task_id, "in-progress")

        elif command == "mark-done":
            if len(sys.argv) != 3:
                print("Error: ID is required")
                sys.exit(1)
            task_id = int(sys.argv[2])
            mark_task(task_id, "done")

        elif command == "list":
            status = sys.argv[2].lower() if len(sys.argv) > 2 else None
            if status and status not in ["todo", "in-progress", "done"]:
                print("Error: Invalid status. Use todo, in-progress, or done")
                sys.exit(1)
            list_tasks(status)

        else:
            print(f"Error: Unknown command '{command}'")
            print_usage()
            sys.exit(1)

    except ValueError:
        print("Error: Invalid ID format. ID must be a number")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()