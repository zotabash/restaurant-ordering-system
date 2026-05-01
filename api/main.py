from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.models.model_loader import index
from api.routers.index import load_routes

app = FastAPI()

# Create tables
index()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

load_routes(app)