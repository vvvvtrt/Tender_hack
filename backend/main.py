from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.api.routers.products import (product_router)

app = FastAPI(
    title="API for Tender Hack",
    description="Was created 05-07.04.2024 by RTFM_MISIS",
    version="1.0",
)

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST", "GET"],
    allow_headers=["*"],
)

app.include_router(product_router)
