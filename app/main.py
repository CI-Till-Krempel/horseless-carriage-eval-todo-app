from fastapi import FastAPI, Depends, Request, Form, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app.database import SessionLocal, init_db, TodoList, Task

app = FastAPI(title="To-Do List Web App", version="1.0.0")

templates = Jinja2Templates(directory="app/templates")

@app.on_event("startup")
def startup_event():
    init_db()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_dashboard(request: Request, db: Session = Depends(get_db)):
    lists = db.query(TodoList).all()
    return templates.TemplateResponse("index.html", {"request": request, "lists": lists})

@app.post("/lists")
def create_list(name: str = Form(...), db: Session = Depends(get_db)):
    if not name.strip():
        raise HTTPException(status_code=400, detail="List name cannot be empty")
    new_list = TodoList(name=name)
    db.add(new_list)
    db.commit()
    return RedirectResponse(url="/", status_code=303)

@app.post("/lists/{list_id}/tasks")
def create_task(list_id: int, description: str = Form(...), db: Session = Depends(get_db)):
    todo_list = db.query(TodoList).filter(TodoList.id == list_id).first()
    if not todo_list:
        raise HTTPException(status_code=404, detail="List not found")
    if not description.strip():
        raise HTTPException(status_code=400, detail="Task description cannot be empty")
    new_task = Task(description=description, completed=False, list_id=list_id)
    db.add(new_task)
    db.commit()
    return RedirectResponse(url="/", status_code=303)

@app.post("/tasks/{task_id}/toggle")
def toggle_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    task.completed = not task.completed
    db.commit()
    return RedirectResponse(url="/", status_code=303)

@app.post("/tasks/{task_id}/delete")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(task)
    db.commit()
    return RedirectResponse(url="/", status_code=303)

@app.post("/lists/{list_id}/delete")
def delete_list(list_id: int, db: Session = Depends(get_db)):
    todo_list = db.query(TodoList).filter(TodoList.id == list_id).first()
    if not todo_list:
        raise HTTPException(status_code=404, detail="List not found")
    db.delete(todo_list)
    db.commit()
    return RedirectResponse(url="/", status_code=303)
