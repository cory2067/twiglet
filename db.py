from game_object import Arsenal
import uuid
import random

# TODO: use a real database
db = {}

def generate_arsenal_id() -> str:
    return uuid.uuid4().hex

def insert_arsenal(arsenal: Arsenal) -> str:
    db[arsenal.id] = arsenal

def find_arsenal(arsenal_id: str) -> Arsenal:
    return db[arsenal_id]

def find_random_arsenal(exclude_id: str) -> str:
    key = random.choice(list(set(db.keys()) - {exclude_id}))
    return db[key]