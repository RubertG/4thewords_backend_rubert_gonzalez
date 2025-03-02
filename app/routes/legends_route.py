from fastapi import APIRouter, HTTPException, status
from app.core.db import SessionDep
from app.services.legend_services import get_all_legends
from app.models.legend_model import Legend
from app.schemas.legend_schema import LegendCreate

router = APIRouter(
    prefix="/leyendas",
    tags=["leyendas"],
)


@router.get("", response_model=list[Legend])
async def get_legends(session: SessionDep):
    legends = get_all_legends(session)

    if legends is None:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Error al obtener las leyendas",
        )

    return legends
