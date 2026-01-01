# API Contracts for Todo App Data Models

## Overview
This document defines the data model contracts for the Todo App. These contracts specify the structure and validation rules for data entities used in the application.

## Data Models

### Task Model
```python
class Task(BaseModel):
    id: str
    title: str
    description: str
    is_complete: bool = False
```

#### Field Specifications:
- **id**:
  - Type: str
  - Required: Yes
  - Description: Unique identifier for every task
  - Validation: Must be a non-empty string

- **title**:
  - Type: str
  - Required: Yes
  - Description: Title of Task
  - Validation: Must be a non-empty string

- **description**:
  - Type: str
  - Required: No (optional)
  - Description: Description of Task
  - Default: Empty string
  - Validation: Can be any string including empty

- **is_complete**:
  - Type: bool
  - Required: No (optional)
  - Description: Status to indicate if task is complete or not
  - Default: False
  - Validation: Must be a boolean value

### Tasks List Structure
```python
tasks_list: List[Task]
```

#### Specifications:
- **Type**: List containing Task objects
- **Description**: In-memory storage for all Task instances
- **Operations Supported**:
  - Add Task objects to the list
  - Remove Task objects from the list (deleting of task)
  - Update Task objects in the list (Task Updation)
  - Mark Task as complete or uncomplete