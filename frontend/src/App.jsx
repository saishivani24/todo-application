import { useEffect, useState } from "react";
import { getTodos, addTodo, completeTodo, deleteTodo } from "./api";
import "./App.css";

export default function App() {
  const [todos, setTodos] = useState([]);
  const [input, setInput] = useState("");
  const [error, setError] = useState("");

  useEffect(() => {
    getTodos().then(setTodos);
  }, []);

  async function handleAdd(e) {
    e.preventDefault();
    setError("");
    if (!input.trim()) return;
    try {
      const task = await addTodo(input.trim());
      setTodos(prev => [...prev, task]);
      setInput("");
    } catch {
      setError("Failed to add task.");
    }
  }

  async function handleDone(id) {
    const updated = await completeTodo(id);
    setTodos(prev => prev.map(t => t.id === id ? updated : t));
  }

  async function handleDelete(id) {
    await deleteTodo(id);
    setTodos(prev => prev.filter(t => t.id !== id));
  }

  return (
    <div className="container">
      <h1>Todo App</h1>

      <form onSubmit={handleAdd} className="add-form">
        <input
          value={input}
          onChange={e => setInput(e.target.value)}
          placeholder="New task..."
        />
        <button type="submit">Add</button>
      </form>
      {error && <p className="error">{error}</p>}

      <ul className="todo-list">
        {todos.length === 0 && <li className="empty">No tasks yet.</li>}
        {todos.map(t => (
          <li key={t.id} className={t.done ? "done" : ""}>
            <span className="title">{t.title}</span>
            <div className="actions">
              {!t.done && (
                <button onClick={() => handleDone(t.id)} className="btn-done">Done</button>
              )}
              <button onClick={() => handleDelete(t.id)} className="btn-delete">Delete</button>
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
}
