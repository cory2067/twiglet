from pydantic import BaseModel


class Player(BaseModel):
    hp: int=100
    accuracy: int=0