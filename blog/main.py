from typing import Annotated
from fastapi import FastAPI, Depends, Query
from .database import engine
from .models import SQLModel, Blogs
from sqlmodel import Session, select
from contextlib import asynccontextmanager


def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]

@asynccontextmanager
async def lifespan(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    yield

app = FastAPI(lifespan=lifespan)

@app.post('/blogs')
def create(request: Blogs, session:SessionDep):
    session.add(request)
    session.commit()
    session.refresh(request)
    return {'title':request.title,'body':request.body}

@app.get('/blogs')
def read(session:SessionDep,
         offset: int = 0,
         limit: Annotated[int, Query(le=100)] = 100,
         ) -> list[Blogs]:
    blogs = session.exec(select(Blogs).offset(offset).limit(limit)).all()
    return blogs

