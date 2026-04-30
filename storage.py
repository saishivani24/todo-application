import json
import os

DB_FILE = os.path.join(os.path.dirname(__file__), "todos.json")


def load() -> list[dict]:
    if not os.path.exists(DB_FILE):
        return []
    with open(DB_FILE, "r") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            print("Warning: todos.json is corrupted. Starting with an empty list.")
            return []
    if not isinstance(data, list):
        print("Warning: todos.json has unexpected format. Starting with an empty list.")
        return []
    return data


def save(todos: list[dict]) -> None:
    with open(DB_FILE, "w") as f:
        json.dump(todos, f, indent=2)
