# Todo App

A simple in-memory todo console application built with Python and InquirerPy for an interactive CLI experience.

## Features

- Interactive CLI menu with InquirerPy
- Add new tasks with validation
- View existing tasks with detailed information
- Update task details (title, description, status)
- Mark tasks as complete
- Delete tasks with confirmation
- In-memory task storage

## Setup

This project uses UV as the package manager. To set up the project:

1. Install UV package manager
2. Clone the repository
3. Navigate to the project directory

## Installation

```bash
uv sync
```

Or to install dependencies:
```bash
uv install
```

## Usage

```bash
todo-app
```

## CLI Interface Documentation

The Todo App provides an interactive command-line interface with the following menu options:

### Main Menu
When you run `todo-app`, you'll see a main menu with these options:
- Add Task
- View Tasks
- Update Task
- Mark Task as Complete
- Delete Task
- Exit

### Add Task
- Prompts for task title with validation (cannot be empty)
- Prompts for task description with validation (cannot be empty)
- Automatically generates a unique ID for the task
- Adds the task to the in-memory task list

### View Tasks
- Shows all existing tasks with their completion status
- Displays task details (ID, title, description, status) when selected
- If no tasks exist, shows an appropriate message

### Update Task
- Shows a list of existing tasks to select from
- Allows selection of which field to update (title, description, or status)
- Provides validation for text fields
- Excludes the ID field from modification (as required)

### Mark Task as Complete
- Shows only incomplete tasks for selection
- Updates the selected task's status to "Complete"
- If no incomplete tasks exist, shows an appropriate message

### Delete Task
- Shows all tasks for selection
- Requests confirmation before deletion to prevent accidental removal
- If cancelled, returns to the main menu without changes

### Navigation
- All operations return to the main menu after completion
- Use Enter to confirm selections
- Use arrow keys to navigate menus
- Press Ctrl+C to exit the application at any time

## Testing

To run tests:
```bash
uv run pytest
```