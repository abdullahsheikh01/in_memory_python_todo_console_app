"""
Module for marking tasks as complete in the todo list.
This file will contain functionality for marking tasks as complete.
"""
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..data_models.task import Task
    from ..data_models.tasks_list import tasks_list

from ..data_models.task import Task
from ..data_models.tasks_list import tasks_list


def mark_task_as_complete(task_id: str) -> bool:
    """
    Mark a task as complete by setting its is_complete field to True.

    Args:
        task_id: The unique identifier of the task to mark as complete

    Returns:
        bool: True if task was successfully marked as complete, False if task not found
    """
    # Find the task by ID
    for i, existing_task in enumerate(tasks_list):
        if existing_task.id == task_id:
            # Update the task's is_complete field to True
            tasks_list[i] = existing_task.copy(update={"is_complete": True})
            return True

    # Task not found
    return False