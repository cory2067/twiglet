from pydantic import BaseModel
from game_object import GameObject

class GetObjectsResponse(BaseModel):
    objects: list[GameObject]

class PostCraftRequest(BaseModel):
    objects: list[GameObject]
    prompt: str

class PostCraftResponse(BaseModel):
    crafted_object: GameObject