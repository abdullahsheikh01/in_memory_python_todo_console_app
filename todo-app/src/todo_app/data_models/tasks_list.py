"""
Tasks list module for the Todo App.
This module provides a data structure for managing multiple Task instances.

Supported operations:
- Add new Task instances to the collection
- Remove Task instances from the collection
- Update Task instances within the collection
- Retrieve Task instances from the collection
- Search for specific Task instances based on criteria
"""
from typing import List
from .task import Task


# List to manage Task instances
tasks_list: List[Task] = []