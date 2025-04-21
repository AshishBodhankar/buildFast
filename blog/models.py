from sqlmodel import Field, SQLModel

class Blogs(SQLModel, table=True):
   id: int = Field(primary_key=True, index=True)
   title: str = Field(index=True)
   body: str = Field(index=True)

