from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange

app = FastAPI()

#we will give a scheme like a rules to follow
class Post(BaseModel):
    title: str 
    content: str
    published: bool = True
    rating: Optional[int] = None

mypost = [{"title": "title of post 1", "content": "content of post 1", "id": 1}, {"title": "favorite foods", "content": "I like pizza", "id": 2}]

@app.get("/")
async def read_root():
    return {"message": "World"}

@app.get("/posts")
async def read_posts():
    return {"data": mypost} 

@app.post("/createposts")
async def create_posts(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 1000000)
    mypost.append(post_dict)
    return {"data": post_dict}

