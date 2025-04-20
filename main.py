from fastapi import FastAPI

myapp = FastAPI()

@myapp.get('/')
#the below fuction wrapped by the above decorator is called "path operation function" 
def index():
    return {'data':'blog list'}

@myapp.get('/blog/unpublished')
def unpublished():
    return {'data':'all unpublished blogs'}

@myapp.get('/blog/{id}')
def show(id: int):
    # fetch blog with id = id
    return {'data': id}

@myapp.get('/blog/{id}/comments')
def comments(id: int):
    return {'data': {id * 3, id * 7 + 9}}

