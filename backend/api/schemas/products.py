from pydantic import BaseModel


class ProductInput(BaseModel):
    name: str


class ProductOutputBase(BaseModel):
    type: str
    country: str
    producer: str
    units: str
    model: str


class ProductOutputGenerated(ProductOutputBase):
    update_name: str


class ProductOutputNew(ProductOutputBase):
    name: str
