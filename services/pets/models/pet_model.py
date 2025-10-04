from pydantic import BaseModel


class Tags(BaseModel):
    id: int
    name: str


class Category(BaseModel):
    id: int
    name: str


class PetModelResponse(BaseModel):
    id: int
    category: Category
    name: str
    photoUrls: list[str]
    tags: list[Tags]
    status: str
