import argparse
import tasks


def cmd_add(args):
    try:
        task = tasks.add(args.title)
        print(f"Added task [{task['id']}]: {task['title']}")
    except ValueError as e:
        print(f"Error: {e}")


def cmd_list(args):
    todos = tasks.list_all()
    if not todos:
        print("No tasks yet.")
        return
    for t in todos:
        status = "x" if t["done"] else " "
        print(f"  [{status}] {t['id']}. {t['title']}")


def cmd_done(args):
    task = tasks.complete(args.id)
    if task:
        print(f"Marked done: {task['title']}")
    else:
        print(f"No task with id {args.id}.")


def cmd_delete(args):
    if tasks.delete(args.id):
        print(f"Deleted task {args.id}.")
    else:
        print(f"No task with id {args.id}.")


def main():
    parser = argparse.ArgumentParser(description="Simple CLI To-Do app")
    sub = parser.add_subparsers(dest="command", required=True)

    p_add = sub.add_parser("add", help="Add a new task")
    p_add.add_argument("title", help="Task description")
    p_add.set_defaults(func=cmd_add)

    p_list = sub.add_parser("list", help="List all tasks")
    p_list.set_defaults(func=cmd_list)

    p_done = sub.add_parser("done", help="Mark a task as complete")
    p_done.add_argument("id", type=int, help="Task ID")
    p_done.set_defaults(func=cmd_done)

    p_del = sub.add_parser("delete", help="Delete a task")
    p_del.add_argument("id", type=int, help="Task ID")
    p_del.set_defaults(func=cmd_delete)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
