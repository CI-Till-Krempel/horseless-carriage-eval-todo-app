from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List, Dict

app = FastAPI(title="To-Do List Web App")

class TodoListCreate(BaseModel):
    name: str

class TodoList(BaseModel):
    id: str
    name: str

lists_db: Dict[str, dict] = {}

@app.post("/lists", response_model=TodoList)
def create_list(item: TodoListCreate):
    import uuid
    list_id = str(uuid.uuid4())[:8]
    new_list = {"id": list_id, "name": item.name, "tasks": []}
    lists_db[list_id] = new_list
    return TodoList(id=list_id, name=item.name)

@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <html>
        <head><title>To-Do List App</title></head>
        <body>
            <h1>To-Do List App</h1>
            <div id="app">
                <form id="create-list-form">
                    <input type="text" id="list-name" placeholder="List Name" required />
                    <button type="submit">Create List</button>
                </form>
                <div id="lists-container"></div>
            </div>
            <script>
                document.getElementById('create-list-form').addEventListener('submit', async (e) => {
                    e.preventDefault();
                    const name = document.getElementById('list-name').value;
                    const res = await fetch('/lists', {
                        method: 'POST',
                        headers: {'Content-Type': 'application/json'},
                        body: JSON.stringify({name})
                    });
                    if (res.ok) {
                        window.location.reload();
                    }
                });
            </script>
        </body>
    </html>
    """
