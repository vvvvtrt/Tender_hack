from fastapi import APIRouter, HTTPException

from backend.api.schemas.products import (ProductInput, ProductOutputGenerated,
                                          ProductOutputNew)
from backend.core.controllers.products import processing


product_router = APIRouter(
    prefix="/api",
    tags=["product"]
)


@product_router.post("/generate_product", response_model=ProductOutputGenerated)
async def get_user(product: ProductInput):
    print(product)
    if len(product.name) > 0:
        test_product = processing(product.name)
        test_product["update_name"] = product.name
        test_product["model"] = "model"
        return test_product
    else:
        raise HTTPException(status_code=400, detail="Bad Request!")


@product_router.post("/create_product", status_code=201)
async def get_user(product: ProductOutputNew):
    if len(product.name) > 0:
        test_product = {
            "name": "product",
            "type": "product",
            "model": "product",
            "producer": "product",
            "units": "product"
        }
        return test_product
    else:
        raise HTTPException(status_code=400, detail="Bad Request!")
