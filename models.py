import json
import os

DATA_FILE = 'todos.json'

def load_data():
    if not os.path.exists(DATA_FILE):
        return {"lists": []}
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except Exception:
        return {"lists": []}

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)

class TaskManager:
    @staticmethod
    def get_all_lists():
        data = load_data()
        return data.get("lists", [])

    @staticmethod
    def create_list(name):
        data = load_data()
        new_list = {
            "id": str(len(data["lists"]) + 1),
            "name": name,
            "tasks": []
        }
        data["lists"].append(new_list)
        save_data(data)
        return new_list

    @staticmethod
    def get_list(list_id):
        data = load_data()
        for lst in data["lists"]:
            if lst["id"] == str(list_id):
                return lst
        return None

    @staticmethod
    def add_task(list_id, description):
        data = load_data()
        for lst in data["lists"]:
            if lst["id"] == str(list_id):
                new_task = {
                    "id": str(len(lst["tasks"]) + 1),
                    "description": description,
                    "completed": False
                }
                lst["tasks"].append(new_task)
                save_data(data)
                return new_task
        return None

    @staticmethod
    def toggle_task(list_id, task_id):
        data = load_data()
        for lst in data["lists"]:
            if lst["id"] == str(list_id):
                for task in lst["tasks"]:
                    if task["id"] == str(task_id):
                        task["completed"] = not task["completed"]
                        save_data(data)
                        return task
        return None

    @staticmethod
    def delete_task(list_id, task_id):
        data = load_data()
        for lst in data["lists"]:
            if lst["id"] == str(list_id):
                lst["tasks"] = [t for t in lst["tasks"] if t["id"] != str(task_id)]
                save_data(data)
                return True
        return False

    @staticmethod
    def delete_list(list_id):
        data = load_data()
        initial_len = len(data["lists"])
        data["lists"] = [l for l in data["lists"] if l["id"] != str(list_id)]
        if len(data["lists"]) < initial_len:
            save_data(data)
            return True
        return False
