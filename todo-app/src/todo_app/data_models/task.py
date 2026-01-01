"""
Task model for the Todo App using Pydantic Base Model.
This module defines the Task data model with structured fields that will be validated by Pydantic.
"""
from pydantic import BaseModel


class Task(BaseModel):
    """
    Task model representing an individual todo item with structured fields.
    """
    id: str
    title: str
    description: str
    is_complete: bool = False