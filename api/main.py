from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.models.model_loader import index
from api.routers.index import load_routes

app = FastAPI()

# Create tables
index()

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load routes
load_routes(app)