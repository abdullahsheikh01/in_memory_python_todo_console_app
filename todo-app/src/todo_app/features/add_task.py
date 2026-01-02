"""
Module for adding tasks to the todo list.
This file will contain functionality for adding new tasks.
"""
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..data_models.task import Task
    from ..data_models.tasks_list import tasks_list

from ..data_models.task import Task
from ..data_models.tasks_list import tasks_list


def add_task(task: Task) -> bool:
    """
    Add a new task to the tasks list.

    Args:
        task: A Task object containing id, title, description, and is_complete status

    Returns:
        bool: True if task was successfully added, False if duplicate ID exists
    """
    # Check if task with same ID already exists in tasks_list
    for existing_task in tasks_list:
        if existing_task.id == task.id:
            return False  # Task with this ID already exists

    # Add the new task to the tasks_list
    tasks_list.append(task)

    # Return True to indicate successful addition
    return True