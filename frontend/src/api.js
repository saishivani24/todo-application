const BASE = "http://localhost:8000";

export const getTodos = () => fetch(`${BASE}/todos`).then(r => r.json());

export const addTodo = (title) =>
  fetch(`${BASE}/todos`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ title }),
  }).then(r => r.json());

export const completeTodo = (id) =>
  fetch(`${BASE}/todos/${id}/done`, { method: "PATCH" }).then(r => r.json());

export const deleteTodo = (id) =>
  fetch(`${BASE}/todos/${id}`, { method: "DELETE" });
