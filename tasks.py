from storage import load, save


def add(title: str) -> dict:
    title = title.strip()
    if not title:
        raise ValueError("Task title cannot be empty.")
    todos = load()
    task = {
        "id": (todos[-1]["id"] + 1) if todos else 1,
        "title": title,
        "done": False,
    }
    todos.append(task)
    save(todos)
    return task


def list_all() -> list[dict]:
    return load()


def complete(task_id: int) -> dict | None:
    todos = load()
    for task in todos:
        if task["id"] == task_id:
            task["done"] = True
            save(todos)
            return task
    return None


def delete(task_id: int) -> bool:
    todos = load()
    updated = [t for t in todos if t["id"] != task_id]
    if len(updated) == len(todos):
        return False
    save(updated)
    return True
