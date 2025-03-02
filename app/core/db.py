from typing import Annotated
from fastapi import Depends, FastAPI
from sqlmodel import SQLModel, Session, create_engine
from decouple import config

URL_DB = config("DATABASE_URL")

if not URL_DB:
    raise ValueError("DATABASE_URL no está definido en el archivo .env")

# Crear el motor de la base de datos usando directamente la cadena de conexión
engine = create_engine(URL_DB)


def create_all_tables(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    print("Base de datos creada correctamente")
    yield
    print("Cerrando aplicación")


# Crear una dependencia para obtener una sesión de base de datos
def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
