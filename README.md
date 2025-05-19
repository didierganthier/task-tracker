# Task Tracker CLI

A simple command-line interface to manage tasks, storing them in a JSON file.

# Project URL
https://roadmap.sh/projects/task-tracker

## Requirements
- Python 3.6+
- No external libraries

## Setup
1. Clone the repository: `git clone <repo-url>`
2. Navigate to the project directory: `cd task-tracker`
3. Run the CLI: `python task-cli.py <command> [arguments]`

## Usage
```
task-cli <command> [arguments]
```

### Commands
- `add <description>`: Add a16Add a new task.
  - Example: `task-cli add "Buy groceries"`
- `update <id> <description>`: Update a task's description.
  - Example: `task-cli update 1 "Buy groceries and cook dinner"`
- `delete <id>`: Delete a task.
  - Example: `task-cli delete 1`
- `mark-in-progress <id>`: Mark a task as in-progress.
  - Example: `task-cli mark-in-progress 1`
- `mark-done <id>`: Mark a task as done.
  - Example: `task-cli mark-done 1`
- `list [status]`: List all tasks or tasks by status (todo, in-progress, done).
  - Examples: `task-cli list`, `task-cli list done`

## Task Properties
Each task has:
- `id`: Unique identifier
- `description`: Task description
- `status`: todo, in-progress, or done
- `createdAt`: Creation timestamp
- `updatedAt`: Last update timestamp

## Storage
Tasks are stored in `tasks.json` in the current directory.

## Error Handling
The CLI handles:
- Invalid commands or arguments
- Non-existent task IDs
- Invalid JSON file
- Invalid ID formats
  
## Notes
 - The implementation uses only Python's standard library (json, os, sys, datetime).

 - Tasks are stored in tasks.json with the required properties.

 - Error handling covers invalid inputs, file issues, and non-existent tasks.

 - The CLI is case-insensitive for commands and status.

 - The code is modular, with separate functions for each operation.

 - Comments are included for clarity.

