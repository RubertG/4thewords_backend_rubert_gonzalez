from app.core.db import SessionDep
from sqlmodel import select
from app.models.legend_model import Legend


def get_all_legends(session: SessionDep) -> list[Legend] | None:
    """
    Obtiene todas las leyendas de la base de datos.

    Args:
        session (SessionDep): Sesión de la base de datos.

    Returns:
        list[Legend] | None: Lista de leyendas o None si ocurre un error.
    """
    try:
        legends = session.exec(select(Legend)).all()

        return legends
    except Exception as e:
        return None


def get_legend_by_id(legend_id: int, session: SessionDep) -> Legend | None:
    """
    Obtiene una leyenda por su ID.

    Args:
        legend_id (int): ID de la leyenda.
        session (SessionDep): Sesión de la base de datos.

    Returns:
        Legend | None: Leyenda o None si ocurre un error.
    """
    try:
        legend = session.get(Legend, legend_id)

        return legend
    except Exception as e:
        return None
