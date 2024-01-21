from pydantic import BaseModel
from game_object import GameObject, Arsenal

class GetObjectsResponse(BaseModel):
    objects: list[GameObject]

class PostCraftRequest(BaseModel):
    objects: list[GameObject]
    prompt: str

class PostCraftResponse(BaseModel):
    crafted_object: GameObject

class PostArsenalRequest(BaseModel):
    objects: list[GameObject]
    name: str

class PostArsenalResponse(BaseModel):
    arsenal_id: str

class GetRandomArsenalRequest(BaseModel):
    exclude: list[str]

class GetRandomArsenalResponse(BaseModel):
    arsenal: Arsenal

class GetArsenalResponse(BaseModel):
    arsenal: Arsenal