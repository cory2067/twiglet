from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from api_models import GetObjectsResponse, PostCraftRequest, PostCraftResponse
from game_object import GameObject
from base_objects import OBJECTS
from engine.create_new_items import generate_ai_gameobject

app = FastAPI()

@app.get("/ping")
def root():
    return {"message": "pong!"}

@app.get("/api/objects")
def get_objects() -> GetObjectsResponse:
    return GetObjectsResponse(
        objects=OBJECTS,
    )

@app.post("/api/craft")
def craft(request: PostCraftRequest) -> PostCraftResponse:
    prompt = request.prompt
    objects = request.objects
    print(prompt)
    print(objects)
    crafted_object = generate_ai_gameobject(objects, prompt)
    return PostCraftResponse(
        crafted_object=crafted_object # temp
    )


app.mount("/", StaticFiles(directory="static", html=True), name="static")