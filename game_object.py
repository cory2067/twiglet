from pydantic import BaseModel


class Modifier(BaseModel):
    stat_affected: str
    value: int
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
    file: str | None