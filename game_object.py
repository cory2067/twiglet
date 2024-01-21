from pydantic import BaseModel
from typing import Literal

class Modifier(BaseModel):
    stat_affected: Literal["accuracy", "speed", "strength"]
    value: float
    duration: int
    reason: str


class GameObject(BaseModel):
    name: str
    object_description: str
    attack_description: str
    durability: int
    accuracy: int
    speed: int
    strength: int
    debuff: Modifier | None
    buff: Modifier |  None
    sprites: list[str] = []

class Arsenal(BaseModel):
    id: str
    name: str
    objects: list[GameObject]