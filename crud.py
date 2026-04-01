from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb://localhost:27017/")
db = client["school"]
tasks = db["tasks"]

def create_task(name, title, subject, due_date, description):
    task = {
        "name": name,
        "title": title,
        "subject": subject,
        "due_date": due_date,
        "description": description
    }
    
    result = tasks.insert_one(task)
    return str(result.inserted_id)


def get_all_tasks():
    return list(tasks.find({}, {"_id": 0}))

def get_tasks_by_name(name):
    return list(tasks.find({"name": name}, {"_id": 0}))

def get_task(title):
    return tasks.find_one({"title": title}, {"_id": 0})

def update_task(title, updated_data):
    result = tasks.update_one(
        {"title": title},
        {"$set": updated_data}
    )
    
    return result.modified_count

def delete_task(title):
    result = tasks.delete_one({"title": title})
    return result.deleted_count


# Create
create_task("Bob", "Science Project", "Science", datetime(2026, 4, 15), "Build a volcano")

# Read
print(get_all_tasks())

# Update
update_task("Science Project", {"subject": "Physics"})

# Delete
delete_task("Science Project")
