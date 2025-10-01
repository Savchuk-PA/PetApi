from pydantic import BaseModel

# {
#     "id": 0,
#     "category": {"id": 0, "name": "string"},
#     "name": "doggie",
#     "photoUrls": ["string"],
#     "tags": [{"id": 0, "name": "string"}],
#     "status": "available",
# }


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
