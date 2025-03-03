from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.db import create_all_tables
from app.routes import legends_route

app = FastAPI(lifespan=create_all_tables)

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Servidor en línea"}


app.include_router(legends_route.router)
