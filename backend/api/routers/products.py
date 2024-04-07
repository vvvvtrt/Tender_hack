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
    if len(product.name) > 0:
        generate_product = processing(product.name)
        generate_product["units"] = " ".join(generate_product["units"])
        generate_product["update_name"] = product.name
        generate_product["model"] = "--- <model> ---"
        # print(generate_product)
        return generate_product
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
            "units": "product",
            "country": "country"
        }
        return test_product
    else:
        raise HTTPException(status_code=400, detail="Bad Request!")
