from fastapi import APIRouter, HTTPException, status
from app.core.db import SessionDep
from app.services.legend_services import get_all_legends, get_legend_by_id
from app.models.legend_model import Legend
from app.schemas.legend_schema import LegendCreate

router = APIRouter(
    prefix="/leyendas",
    tags=["leyendas"],
)


@router.get("", response_model=list[Legend])
async def get_legends(session: SessionDep):
    """
    Obtiene todas las leyendas.

    Args:
        session (SessionDep): Sesión de la base de datos.

    Returns:
        list[Legend] | HTTPException: Lista de leyendas o un error 404.
    """
    legends = get_all_legends(session)

    if legends is None:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Error al obtener las leyendas",
        )

    return legends


@router.get("/{legend_id}")
async def get_legend(legend_id: int, session: SessionDep):
    """
    Obtiene una leyenda por su ID.

    Args:
        legend_id (int): ID de la leyenda.
        session (SessionDep): Sesión de la base de datos.

    Returns:
        Legend | HTTPException: Leyenda o un error 404.
    """
    legend = get_legend_by_id(legend_id, session)

    if legend is None:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Leyenda no encontrada",
        )

    return legend
