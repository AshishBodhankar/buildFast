from sqlmodel import create_engine

SQLALCHEMY_DATABASE_URL = 'sqlite+pysqlite:///./blog.db'

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True,
                       connect_args={'check_same_thread':False})



