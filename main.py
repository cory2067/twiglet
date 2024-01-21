from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from api_models import GetObjectsResponse, PostCraftRequest, PostCraftResponse, PostArsenalRequest, PostArsenalResponse, GetArsenalResponse, GetRandomArsenalResponse, GetRandomArsenalRequest
from game_object import GameObject, Arsenal
from base_objects import OBJECTS
from db import generate_arsenal_id, insert_arsenal, find_random_arsenal, find_arsenal

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
    return PostCraftResponse(
        crafted_object=objects[0] # temp
    )

@app.post("/api/arsenal")
def post_arsenal(request: PostArsenalRequest) -> PostArsenalResponse:
    arsenal = Arsenal(
        id=generate_arsenal_id(),
        name=request.name,
        objects=request.objects,
    )
    insert_arsenal(arsenal)
    print(arsenal.id)
    return PostArsenalResponse(arsenal_id=arsenal.id)

@app.get("/api/random-arsenal")
def get_random_arsenal(exclude_id: str) -> GetRandomArsenalResponse:
    return GetRandomArsenalResponse(
        arsenal=find_random_arsenal(exclude_id)
    )

@app.get("/api/arsenal/{arsenal_id}")
def get_arsenal(arsenal_id: str) -> GetArsenalResponse:
    return GetArsenalResponse(
        arsenal=find_arsenal(arsenal_id)
    )

app.mount("/", StaticFiles(directory="static", html=True), name="static")

# load with some default arsenal for testing
insert_arsenal(
    Arsenal(
        id='test-arsenal-1',
        name="Test Arsenal",
        objects=OBJECTS[:5],
    )
)
insert_arsenal(
    Arsenal(
        id='test-arsenal-2',
        name="Test Arsenal",
        objects=OBJECTS[-5:],
    )
)