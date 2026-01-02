"""
Main CLI interface for the Todo App using InquirerPy.

This module implements the command-line interface with a main menu and all required
functionality to manage tasks using InquirerPy for interactive user input.
"""
import uuid
from InquirerPy import inquirer
from InquirerPy.validator import EmptyInputValidator

try:
    # Try absolute imports first (when run as package)
    from todo_app.data_models.task import Task
    from todo_app.data_models.tasks_list import tasks_list
    from todo_app.features.add_task import add_task
    from todo_app.features.update_task import update_task
    from todo_app.features.delete_task import delete_task
    from todo_app.features.mark_task_as_complete import mark_task_as_complete
except ImportError:
    # Fall back to relative imports (when run directly)
    from .data_models.task import Task
    from .data_models.tasks_list import tasks_list
    from .features.add_task import add_task
    from .features.update_task import update_task
    from .features.delete_task import delete_task
    from .features.mark_task_as_complete import mark_task_as_complete


def display_welcome_message():
    """Display the welcome message for the Todo App CLI."""
    print("\n" + "="*50)
    print("Welcome to the Todo App!")
    print("Manage your tasks efficiently with this CLI interface")
    print("="*50 + "\n")


def show_main_menu():
    """Display the main menu and return the user's choice."""
    choice = inquirer.select(
        message="Select an option:",
        choices=[
            "Add Task",
            "View Tasks",
            "Update Task",
            "Mark Task as Complete",
            "Delete Task",
            "Exit"
        ]
    ).execute()
    return choice


def run_cli():
    """Run the main CLI loop."""
    display_welcome_message()

    while True:
        choice = show_main_menu()

        if choice == "Add Task":
            add_task_cli()
        elif choice == "View Tasks":
            view_tasks_cli()
        elif choice == "Update Task":
            update_task_cli()
        elif choice == "Mark Task as Complete":
            mark_task_complete_cli()
        elif choice == "Delete Task":
            delete_task_cli()
        elif choice == "Exit":
            print("\nThank you for using the Todo App! Goodbye!")
            break

        # Add a pause before showing the menu again
        if choice != "Exit":
            input("\nPress Enter to return to the main menu...")


def add_task_cli():
    """Handle adding a new task via CLI with input validation."""
    print("\n--- Add New Task ---")

    # Get task title with validation
    title = inquirer.text(
        message="Enter task title:",
        validate=EmptyInputValidator("Task title cannot be empty"),
        invalid_message="Task title cannot be empty"
    ).execute()

    # Get task description with validation
    description = inquirer.text(
        message="Enter task description:",
        validate=EmptyInputValidator("Task description cannot be empty"),
        invalid_message="Task description cannot be empty"
    ).execute()

    # Generate unique ID
    task_id = str(uuid.uuid4())

    # Create and add task
    new_task = Task(id=task_id, title=title, description=description, is_complete=False)

    if add_task(new_task):
        print(f"\n✓ Task '{title}' added successfully with ID: {task_id}")
    else:
        print(f"\n✗ Failed to add task. Task with ID {task_id} already exists.")


def view_tasks_cli():
    """Handle viewing tasks via CLI."""
    print("\n--- View Tasks ---")

    if not tasks_list:
        print("No tasks available.")
        return

    # Create choices from tasks
    task_choices = []
    for task in tasks_list:
        status = "✓" if task.is_complete else "○"
        task_choices.append({
            "name": f"{status} [{task.id}] {task.title}",
            "value": task
        })

    # Add option to return to main menu
    task_choices.append({"name": "Back to Main Menu", "value": "back"})

    selected_task = inquirer.select(
        message="Select a task to view details:",
        choices=task_choices
    ).execute()

    if selected_task == "back":
        return

    # Display task details
    print(f"\n--- Task Details ---")
    print(f"ID: {selected_task.id}")
    print(f"Title: {selected_task.title}")
    print(f"Description: {selected_task.description}")
    print(f"Status: {'Complete' if selected_task.is_complete else 'Incomplete'}")

    # Wait for user to press enter to return to main menu
    input("\nPress Enter to return to the main menu...")


def update_task_cli():
    """Handle updating a task via CLI."""
    print("\n--- Update Task ---")

    if not tasks_list:
        print("No tasks available to update.")
        return

    # Create choices from tasks
    task_choices = []
    for task in tasks_list:
        status = "✓" if task.is_complete else "○"
        task_choices.append({
            "name": f"{status} [{task.id}] {task.title}",
            "value": task
        })

    # Add option to return to main menu
    task_choices.append({"name": "Back to Main Menu", "value": "back"})

    selected_task = inquirer.select(
        message="Select a task to update:",
        choices=task_choices
    ).execute()

    if selected_task == "back":
        return

    # Select which field to update (excluding ID)
    field_choices = ["Title", "Description", "Status"]
    selected_field = inquirer.select(
        message="Select field to update:",
        choices=field_choices
    ).execute()

    if selected_field == "Title":
        new_value = inquirer.text(
            message="Enter new title:",
            validate=EmptyInputValidator("Title cannot be empty"),
            invalid_message="Title cannot be empty"
        ).execute()
        updated_task = Task(
            id=selected_task.id,
            title=new_value,
            description=selected_task.description,
            is_complete=selected_task.is_complete
        )
    elif selected_field == "Description":
        new_value = inquirer.text(
            message="Enter new description:",
            validate=EmptyInputValidator("Description cannot be empty"),
            invalid_message="Description cannot be empty"
        ).execute()
        updated_task = Task(
            id=selected_task.id,
            title=selected_task.title,
            description=new_value,
            is_complete=selected_task.is_complete
        )
    elif selected_field == "Status":
        new_status = inquirer.select(
            message="Select new status:",
            choices=["Incomplete", "Complete"]
        ).execute()
        is_complete = True if new_status == "Complete" else False
        updated_task = Task(
            id=selected_task.id,
            title=selected_task.title,
            description=selected_task.description,
            is_complete=is_complete
        )

    # Update the task
    if update_task(updated_task):
        print(f"\n✓ Task '{updated_task.title}' updated successfully.")
    else:
        print(f"\n✗ Failed to update task.")


def mark_task_complete_cli():
    """Handle marking a task as complete via CLI."""
    print("\n--- Mark Task as Complete ---")

    if not tasks_list:
        print("No tasks available.")
        return

    # Create choices from tasks that are not already complete
    incomplete_tasks = [task for task in tasks_list if not task.is_complete]

    if not incomplete_tasks:
        print("No incomplete tasks available to mark as complete.")
        return

    # Create choices from incomplete tasks
    task_choices = []
    for task in incomplete_tasks:
        task_choices.append({
            "name": f"[{task.id}] {task.title}",
            "value": task.id
        })

    # Add option to return to main menu
    task_choices.append({"name": "Back to Main Menu", "value": "back"})

    selected_task_id = inquirer.select(
        message="Select a task to mark as complete:",
        choices=task_choices
    ).execute()

    if selected_task_id == "back":
        return

    # Mark task as complete
    if mark_task_as_complete(selected_task_id):
        # Find the task to display its title
        task = next((t for t in tasks_list if t.id == selected_task_id), None)
        if task:
            print(f"\n✓ Task '{task.title}' marked as complete.")
    else:
        print(f"\n✗ Failed to mark task as complete.")


def delete_task_cli():
    """Handle deleting a task via CLI with confirmation."""
    print("\n--- Delete Task ---")

    if not tasks_list:
        print("No tasks available to delete.")
        return

    # Create choices from tasks
    task_choices = []
    for task in tasks_list:
        status = "✓" if task.is_complete else "○"
        task_choices.append({
            "name": f"{status} [{task.id}] {task.title}",
            "value": task.id
        })

    # Add option to return to main menu
    task_choices.append({"name": "Back to Main Menu", "value": "back"})

    selected_task_id = inquirer.select(
        message="Select a task to delete:",
        choices=task_choices
    ).execute()

    if selected_task_id == "back":
        return

    # Confirm deletion
    confirm = inquirer.confirm(
        message=f"Are you sure you want to delete this task? This action cannot be undone.",
        default=False
    ).execute()

    if confirm:
        # Find the task to display its title
        task = next((t for t in tasks_list if t.id == selected_task_id), None)

        # Delete the task
        if delete_task(selected_task_id):
            task_title = task.title if task else "Unknown Task"
            print(f"\n✓ Task '{task_title}' deleted successfully.")
        else:
            print(f"\n✗ Failed to delete task.")
    else:
        print("\nDeletion cancelled.")


def main():
    """Main entry point for the CLI application."""
    run_cli()
