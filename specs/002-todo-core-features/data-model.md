# Data Model: Todo App

## Task Entity

### Fields
- `id: str` - Unique identifier for the task
- `title: str` - Title/description of the task (required)
- `description: str` - Detailed description of the task (required)
- `is_complete: bool` - Completion status, defaults to False

### Relationships
- Task entities are stored in a global `tasks_list: List[Task]`

### Validation Rules
- All fields except `is_complete` are required
- `id` should be unique within the tasks_list
- `title` should not be empty
- `description` can be empty but should be a valid string

### State Transitions
- `is_complete` transitions from False to True when task is marked complete
- Task can be updated to modify title or description
- Task can be deleted from the tasks_list

## Task List Entity

### Fields
- `tasks_list: List[Task]` - Collection of Task objects

### Operations
- Add Task to list
- Remove Task from list
- Update Task in list
- Find Task by ID
- Mark Task as complete