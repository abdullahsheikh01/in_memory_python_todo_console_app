"""
Module for updating tasks in the todo list.
This file will contain functionality for updating tasks.
"""
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..data_models.task import Task
    from ..data_models.tasks_list import tasks_list

from ..data_models.task import Task
from ..data_models.tasks_list import tasks_list


def update_task(task: Task) -> bool:
    """
    Update an existing task in the tasks list.

    Args:
        task: A Task object containing updated information (id must match existing task)

    Returns:
        bool: True if task was successfully updated, False if task not found
    """
    # Find the existing task by ID
    for i, existing_task in enumerate(tasks_list):
        if existing_task.id == task.id:
            # Update the task at that index with the new task data
            tasks_list[i] = task
            return True

    # Task not found
    return False