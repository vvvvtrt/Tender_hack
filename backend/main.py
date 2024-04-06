from fastapi import FastAPI

from backend.api.routers.products import (product_router)

app = FastAPI(
    title="API for Tender Hack",
    description="Was created 05-07.04.2024 by RTFM_MISIS",
    version="1.0",
)

app.include_router(product_router)
