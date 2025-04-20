from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()

@app.get('/')
#the below fuction wrapped by the above decorator is called "path operation function" 
def index():
    return {'data':'blog list'}

@app.get('/blog/unpublished')
def unpublished():
    return {'data':'all unpublished blogs'}


@app.get('/blog')
def show(limit:int = 10, published:bool = False, sort: Optional[str] = None):
    # fetch blog with id = id
    if published == True:
        return {'data': f'{limit} published blogs from the database'}
    else:
        return {'data': f'{limit} blogs from the database'}

@app.get('/blog/{id}/comments')
def comments(id: int, limit:int = 10 ):
    return {'data': {id * 3, id * 7 + 9}}


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool] = False

@app.post('/blog')
def create_blog(request:Blog):
    return {'data':f'Blog is created with {request.title}'}

if __name__ == "__main__":
    uvicorn.run(app,host="127.0.0.1",port=9000)