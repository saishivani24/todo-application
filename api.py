from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import tasks

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class TaskIn(BaseModel):
    title: str


@app.get("/todos")
def list_todos():
    return tasks.list_all()


@app.post("/todos", status_code=201)
def add_todo(body: TaskIn):
    try:
        return tasks.add(body.title)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.patch("/todos/{task_id}/done")
def complete_todo(task_id: int):
    task = tasks.complete(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@app.delete("/todos/{task_id}", status_code=204)
def delete_todo(task_id: int):
    if not tasks.delete(task_id):
        raise HTTPException(status_code=404, detail="Task not found")
