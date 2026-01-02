# Implementation Plan: Todo App CLI Interface

**Branch**: `003-todo-cli-interface` | **Date**: 2026-01-02 | **Spec**: [specs/003-todo-cli-interface/spec.md](/specs/003-todo-cli-interface/spec.md)
**Input**: Feature specification from `/specs/003-todo-cli-interface/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Implement a CLI interface using InquirerPy for interactive user input that provides a main menu with options to add, view, update, mark complete, and delete tasks. The interface will integrate with existing task management functions and provide proper input validation, navigation, and error handling.

## Technical Context

**Language/Version**: Python 3.12
**Primary Dependencies**: InquirerPy, Pydantic, uuid
**Storage**: In-memory list (tasks_list: List[Task]) stored in data models
**Testing**: pytest (as per previous feature)
**Target Platform**: Cross-platform console application
**Project Type**: Single console application
**Performance Goals**: <100ms response time for all operations
**Constraints**: Console-based interface, no external dependencies beyond those already in project
**Scale/Scope**: Single-user console application with up to 1000 tasks in memory

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

No constitution violations detected. Implementation follows established patterns and uses approved technologies.

## Project Structure

### Documentation (this feature)

```text
todo_app
├── .gitignore
├── .python-version
├── pyproject.toml
├── README.md
└── src
    └── todo_app
        ├── __init__.py # Main File which show Welcome Message and use features
        ├── data_models
        │   ├── task.py
        │   └── tasks_list.py
        └── features # Function of each feature
            ├── add_task.py
            ├── delete_task.py
            ├── update_task.py
            └── mark_task_as_complete.py
```

**Structure Decision**: Follow existing project structure with CLI interface in main __init__.py file that orchestrates the feature functions.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| [e.g., 4th project] | [current need] | [why 3 projects insufficient] |
| [e.g., Repository pattern] | [specific problem] | [why direct DB access insufficient] |

## Phase 0: Research & Analysis

Research completed on InquirerPy for building interactive CLI interfaces. Key findings:
- InquirerPy provides multiple syntax options (classic and alternate)
- Supports various prompt types: text, select, confirm, etc.
- Has built-in validation capabilities
- Can handle dynamic choices based on data

## Phase 1: Design & Implementation Plan

### Phase 1.1: CLI Interface Structure
- Create main menu with welcome message and options
- Implement navigation logic to return to main menu after operations
- Integrate with existing feature functions

### Phase 1.2: Add Task Functionality (FR-004, FR-005, FR-006)
- Collect task title and description with validation
- Generate unique ID using uuid
- Call existing add_task function
- Validate input using InquirerPy validators

### Phase 1.3: View Tasks Functionality (FR-007, FR-013)
- Check for existing tasks
- Display selection list if tasks exist
- Show detailed task information
- Provide option to return to main menu

### Phase 1.4: Update Task Functionality (FR-008, FR-009, FR-010, FR-013)
- Check for existing tasks
- Display selection list if tasks exist
- Allow selection of editable fields (excluding ID)
- Collect new values with validation
- Call existing update_task function

### Phase 1.5: Mark Task Complete Functionality (FR-011, FR-013)
- Check for existing tasks
- Display selection list if tasks exist
- Call existing mark_task_as_complete function

### Phase 1.6: Delete Task Functionality (FR-012, FR-013)
- Check for existing tasks
- Display selection list if tasks exist
- Request confirmation before deletion
- Call existing delete_task function

### Phase 1.7: Documentation (FR-015)
- Update README.md with CLI interface documentation
- Document all menu options and usage

## Implementation Approach

### Phase 1: CLI Interface with Main Menu (FR-001, FR-002)
- Implement main entry point function using InquirerPy for interactive input
- Create welcome message display function
- Create main menu selection using `inquirer.select()` with options: "Add Task", "View Tasks", "Update Task", "Mark Task as Complete", "Delete Task", "Exit"
- Implement main loop that continuously displays menu until user selects "Exit"

### Phase 2: Navigation Logic (FR-003)
- Implement functions for each menu option that return to main menu after completion
- Add pause/input prompts to allow users to read results before returning to menu
- Ensure each operation flow returns to main menu unless user exits

### Phase 3: Add Task Functionality (FR-004, FR-005, FR-006)
- Create `add_task_cli()` function that:
  - Uses `inquirer.text()` with `EmptyInputValidator` for title and description
  - Generates unique ID using `uuid.uuid4()`
  - Creates new Task instance and calls existing `add_task()` function
  - Displays success/error messages
- Validate that task is stored in existing `tasks_list` structure

### Phase 4: View Tasks Functionality (FR-007, FR-013)
- Create `view_tasks_cli()` function that:
  - Checks if `tasks_list` is empty and displays appropriate message
  - Creates dynamic choices from existing tasks using `inquirer.select()`
  - Displays detailed information for selected task
  - Provides option to return to main menu

### Phase 5: Update Task Functionality (FR-008, FR-009, FR-010, FR-013)
- Create `update_task_cli()` function that:
  - Checks if `tasks_list` is empty and displays appropriate message
  - Allows selection of existing task from list
  - Provides selection of editable fields (title, description, status) excluding ID
  - Uses `inquirer.text()` with validation for text fields
  - Uses `inquirer.select()` for status selection
  - Calls existing `update_task()` function
  - Validates that ID field cannot be modified

### Phase 6: Mark Task Complete Functionality (FR-011, FR-013)
- Create `mark_task_complete_cli()` function that:
  - Checks if `tasks_list` is empty and displays appropriate message
  - Shows only incomplete tasks for selection
  - Calls existing `mark_task_as_complete()` function with task ID
  - Displays appropriate message if no incomplete tasks exist

### Phase 7: Delete Task Functionality (FR-012, FR-013)
- Create `delete_task_cli()` function that:
  - Checks if `tasks_list` is empty and displays appropriate message
  - Allows selection of task from list
  - Uses `inquirer.confirm()` to request confirmation before deletion
  - Calls existing `delete_task()` function if confirmed
  - Returns to main menu if cancelled

### Phase 8: Documentation (FR-015)
- Update README.md with comprehensive documentation
- Document all CLI menu options and usage instructions
- Include examples of how to navigate and use each feature

## Detailed Implementation Steps

### Main CLI Structure
1. Create main entry point in `todo-app/src/todo_app/__init__.py`
2. Implement `display_welcome_message()` function
3. Implement `show_main_menu()` function using InquirerPy
4. Implement main loop with menu navigation

### Menu Options Implementation
1. Add Task: Collect title/description with validation, generate UUID, call add_task()
2. View Tasks: Check for empty list, display choices, show details, return to menu
3. Update Task: Check for empty list, select task, select field (not ID), validate input, call update_task()
4. Mark Complete: Check for empty/incomplete lists, select task, call mark_task_as_complete()
5. Delete Task: Check for empty list, select task, confirm deletion, call delete_task()

### Validation and Error Handling
1. Use InquirerPy validators for all text inputs
2. Implement empty state checks for all operations that require existing tasks
3. Ensure proper error messages are displayed
4. Implement graceful navigation between operations

## Risk Analysis

- Input validation: Using InquirerPy's built-in validation to ensure data quality
- Empty task list handling: Proper error messages when no tasks exist for operations
- Navigation: Ensuring users can always return to the main menu
- Error handling: Graceful handling of edge cases and unexpected inputs
- ID protection: Ensuring task ID field cannot be modified during update operations
