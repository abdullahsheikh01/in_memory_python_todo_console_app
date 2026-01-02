"""
Module for deleting tasks from the todo list.
This file will contain functionality for deleting tasks.
"""
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..data_models.task import Task
    from ..data_models.tasks_list import tasks_list

from ..data_models.task import Task
from ..data_models.tasks_list import tasks_list


def delete_task(task_id: str) -> bool:
    """
    Delete a task from the tasks list by ID.

    Args:
        task_id: The unique identifier of the task to delete

    Returns:
        bool: True if task was successfully deleted, False if task not found
    """
    # Find the task by ID
    for i, existing_task in enumerate(tasks_list):
        if existing_task.id == task_id:
            # Remove the task from the tasks_list
            tasks_list.pop(i)
            return True

    # Task not found
    return False