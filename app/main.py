from fastapi import FastAPI
from app.core.db import create_all_tables
from app.routes import legends_route

app = FastAPI(lifespan=create_all_tables)


@app.get("/")
async def root():
    return {"message": "Servidor en línea"}


app.include_router(legends_route.router)
