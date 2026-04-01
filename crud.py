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

create_task(
    "Josh",
    "Math Homework",
    "Math",
    datetime(2026, 4, 10),
    "Complete exercises 1–10"
)