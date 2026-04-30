import pytest
from unittest.mock import patch


def make_todos(*titles):
    return [{"id": i + 1, "title": t, "done": False} for i, t in enumerate(titles)]


@patch("tasks.save")
@patch("tasks.load", return_value=[])
def test_add_first_task(mock_load, mock_save):
    import tasks
    task = tasks.add("Buy milk")
    assert task["id"] == 1
    assert task["title"] == "Buy milk"
    assert task["done"] is False


@patch("tasks.save")
@patch("tasks.load")
def test_add_increments_id(mock_load, mock_save):
    import tasks
    mock_load.return_value = make_todos("First")
    task = tasks.add("Second")
    assert task["id"] == 2


@patch("tasks.save")
@patch("tasks.load", return_value=[])
def test_add_strips_whitespace(mock_load, mock_save):
    import tasks
    task = tasks.add("  Trimmed  ")
    assert task["title"] == "Trimmed"


@patch("tasks.load", return_value=[])
def test_add_empty_title_raises(mock_load):
    import tasks
    with pytest.raises(ValueError, match="empty"):
        tasks.add("   ")


@patch("tasks.load")
def test_list_all_returns_tasks(mock_load):
    import tasks
    todos = make_todos("A", "B")
    mock_load.return_value = todos
    assert tasks.list_all() == todos


@patch("tasks.save")
@patch("tasks.load")
def test_complete_marks_done(mock_load, mock_save):
    import tasks
    todos = make_todos("Do something")
    mock_load.return_value = todos
    result = tasks.complete(1)
    assert result["done"] is True
    mock_save.assert_called_once()


@patch("tasks.load")
def test_complete_missing_id_returns_none(mock_load):
    import tasks
    mock_load.return_value = make_todos("Task")
    assert tasks.complete(99) is None


@patch("tasks.save")
@patch("tasks.load")
def test_delete_existing_task(mock_load, mock_save):
    import tasks
    mock_load.return_value = make_todos("Keep", "Remove")
    assert tasks.delete(2) is True
    saved = mock_save.call_args[0][0]
    assert all(t["id"] != 2 for t in saved)


@patch("tasks.load")
def test_delete_missing_task_returns_false(mock_load):
    import tasks
    mock_load.return_value = make_todos("Only task")
    assert tasks.delete(99) is False
