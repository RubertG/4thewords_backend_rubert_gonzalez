from fastapi import APIRouter, HTTPException, status
from app.core.db import SessionDep
from app.services.legend_services import (
    get_all_legends,
    get_legend_by_id,
    create_legend,
    update_legend,
    delete_legend,
)
from app.models.legend_model import Legend
from app.schemas.legend_schema import LegendCreate, LegendUpdate
from pydantic import ValidationError

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
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error al obtener las leyendas",
        )

    return legends


@router.post("", response_model=Legend, status_code=status.HTTP_201_CREATED)
async def add_legend(legend_data: LegendCreate, session: SessionDep):
    """
    Crea una leyenda.

    Args:
        legend_data (LegendCreate): Datos de la leyenda.
        session (SessionDep): Sesión de la base de datos.

    Returns:
        Legend | HTTPException: Leyenda creada o un error
    """
    try:
        legend = create_legend(legend_data, session)
    except ValidationError as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Error de validación de datos",
        )
    if legend is None:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error al crear la leyenda",
        )

    return legend


@router.get("/{legend_id}", response_model=Legend)
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
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Leyenda no encontrada",
        )

    return legend


@router.patch("/{legend_id}", response_model=Legend, status_code=status.HTTP_200_OK)
async def edit_legend(legend_id: int, legend_data: LegendUpdate, session: SessionDep):
    """
    Actualiza una leyenda por su ID.

    Args:
        legend_id (int): ID de la leyenda.
        session (SessionDep): Sesión de la base de datos.

    Returns:
        Legend | HTTPException: Leyenda actualizada o un error 404 si no se encuentra.
    """
    try:
        legend = update_legend(legend_id, legend_data, session)
    except ValidationError as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Error de validación de datos",
        )
        
    if legend is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Error al actualizar la leyenda, no se encontró la leyenda",
        )

    return legend


@router.delete("/{legend_id}", status_code=status.HTTP_200_OK)
async def remove_legend(legend_id: int, session: SessionDep):
    """
    Elimina una leyenda por su ID.

    Args:
        legend_id (int): ID de la leyenda.
        session (SessionDep): Sesión de la base de datos.

    Returns:
        dict: Mensaje de éxito.
    """
    is_deleted = delete_legend(legend_id, session)

    if not is_deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Error al eliminar la leyenda, no se encontró la leyenda",
        )

    return {"detail": "Leyenda eliminada con éxito"}
