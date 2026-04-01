from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb://localhost:27017/")
db = client["asrjc"]
tasks = db["hw"]

def create_task(name, title, subject, due_date, description):
    hw = {
        "name": name,
        "title": title,
        "subject": subject,
        "due_date": due_date,
        "description": description
    }
    
    result = tasks.insert_one(hw)
    return str(result.inserted_id)

def get_all_hw():
    return list(tasks.find({}, {"_id": 0}))

def get_hw_by_name(name):
    return list(tasks.find({"name": name}, {"_id": 0}))

def get_hw(title):
    return tasks.find_one({"title": title}, {"_id": 0})

def update_hw(title, updated_data):
    result = tasks.update_one(
        {"title": title},
        {"$set": updated_data}
    )
    
    return result.modified_count

def delete_hw(title):
    result = tasks.delete_one({"title": title})
    return result.deleted_count



# Create
# create_task("Josh", "Hackathon", "STEM", datetime(2026, 4, 15), "Build RedPin.")

# Read
# print(get_all_hw())

# Update
# update_hw("Hackathon", {"subject": "STEM"})

# Delete
# delete_hw("Hackathon")
