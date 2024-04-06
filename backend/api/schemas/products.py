from pydantic import BaseModel


class ProductInput(BaseModel):
    name: str


class ProductOutputBase(BaseModel):
    type: str
    model: str
    producer: str
    units: str


class ProductOutputGenerated(ProductOutputBase):
    update_name: str


class ProductOutputNew(ProductOutputBase):
    name: str
