import os
from pathlib import Path
from pymongo import MongoClient
from pymongo.database import Database
from pymongo.errors import PyMongoError
from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parents[1] / ".env")

def _get_required_env(name: str) -> str:
    value = os.getenv(name, "").strip()
    if not value:
        raise ValueError(f"Missing required env: {name}")
    return value

def init_mongo_client() -> MongoClient:
    mongo_uri = _get_required_env("MONGODB_URI")
    return MongoClient(mongo_uri, serverSelectionTimeoutMS=5000)

def connect_mongo() -> tuple[MongoClient, Database]:
    client = init_mongo_client()
    database_name = _get_required_env("MONGODB_DB")

    try:
        client.admin.command("ping")
    except PyMongoError as exc:
        client.close()
        raise ConnectionError("Failed to connect") from exc

    return client, client[database_name]