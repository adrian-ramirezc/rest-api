from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Todo:
    todo_id: int
    description: str


@dataclass
class Todos:
    elements: List[Todo] = None

    def __post_init__(self):
        if self.elements is None:
            self.elements = []

    def get_by_id(self, _todo_id: int) -> Optional[Todo]:
        for todo in self.elements:
            if todo.todo_id == _todo_id:
                return todo
        return self.create_empty_todo()

    def add(self, todo: Todo):
        self.elements.append(todo)

    def __str__(self):
        all_todos = ",\n".join([str(element) for element in self.elements])
        return f"Todos: {all_todos}"

    @classmethod
    def create_empty_todo(cls):
        return Todo(None, None)
