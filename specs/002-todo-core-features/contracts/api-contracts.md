# API Contracts: Todo App Core Features

## Contract: add_task

### Function Signature
```python
def add_task(task: Task) -> bool:
```

### Parameters
- **task** (Task): A Task object containing id, title, description, and is_complete status
  - Type: `Task` (from src.todo_app.data_models.task)
  - Required: Yes
  - Validation: Must conform to Task model validation rules

### Return Value
- **Type**: `bool`
- **Description**: True if task was successfully added, False otherwise
- **Success**: Task is added to the global tasks_list
- **Failure**: Task is not added due to validation error or duplicate ID

### Requirements
- Meets FR-001: System MUST provide an `add_task` function that accepts a Task object and adds it to the existing Task list
- Uses proper type hinting per FR-006
- Uses Task class from data models per FR-007

---

## Contract: delete_task

### Function Signature
```python
def delete_task(task_id: str) -> bool:
```

### Parameters
- **task_id** (str): The unique identifier of the task to delete
  - Type: `str`
  - Required: Yes
  - Validation: Must match an existing task ID in the tasks_list

### Return Value
- **Type**: `bool`
- **Description**: True if task was successfully deleted, False otherwise
- **Success**: Task is removed from the global tasks_list
- **Failure**: Task not found or deletion failed

### Requirements
- Meets FR-002: System MUST provide a `delete_task` function that accepts a task identifier and removes the corresponding task from the Task list
- Uses proper type hinting per FR-006

---

## Contract: update_task

### Function Signature
```python
def update_task(task: Task) -> bool:
```

### Parameters
- **task** (Task): A Task object containing updated information
  - Type: `Task` (from src.todo_app.data_models.task)
  - Required: Yes
  - Validation: Must conform to Task model validation rules and ID must match existing task

### Return Value
- **Type**: `bool`
- **Description**: True if task was successfully updated, False otherwise
- **Success**: Task in global tasks_list is updated with new values
- **Failure**: Task not found or update failed

### Requirements
- Meets FR-003: System MUST provide an `update_task` function that accepts a Task object and updates the corresponding task in the Task list
- Uses proper type hinting per FR-006
- Uses Task class from data models per FR-007

---

## Contract: mark_task_as_complete

### Function Signature
```python
def mark_task_as_complete(task_id: str) -> bool:
```

### Parameters
- **task_id** (str): The unique identifier of the task to mark as complete
  - Type: `str`
  - Required: Yes
  - Validation: Must match an existing task ID in the tasks_list

### Return Value
- **Type**: `bool`
- **Description**: True if task was successfully marked as complete, False otherwise
- **Success**: Task's is_complete field is set to True in the global tasks_list
- **Failure**: Task not found or update failed

### Requirements
- Meets FR-004: System MUST provide a `mark_task_complete` function that accepts a task identifier and marks the corresponding task as complete
- Uses proper type hinting per FR-006