from app.core.db import SessionDep
from sqlmodel import select
from app.models.legend_model import Legend
from app.schemas.legend_schema import LegendCreate, LegendUpdate


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


def create_legend(legend_data: LegendCreate, session: SessionDep) -> Legend | None:
    """
    Crea una leyenda en la base de datos. Primero valida los datos de la leyenda y luego si guarda en la base de datos.

    Args:
        legend (Legend): Leyenda a crear.
        session (SessionDep): Sesión de la base de datos.

    Returns:
        Legend | None: Leyenda creada o None si ocurre un error.
    """
    try:
        legend = Legend.model_validate(legend_data.model_dump())
        session.add(legend)
        session.commit()
        session.refresh(legend)

        return legend
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


def update_legend(
    legend_id: int, legend_data: LegendUpdate, session: SessionDep
) -> Legend | None:
    """
    Actualiza una leyenda en la base de datos despues de verificar que exista.

    Args:
        legend_id (int): ID de la leyenda a actualizar.
        legend_data (Legend): Datos de la leyenda.
        session (SessionDep): Sesión de la base de datos.

    Returns:
        Legend | None: Leyenda actualizada o None si ocurre un error.
    """
    try:
        legend_db = get_legend_by_id(legend_id, session)

        if legend_db is None:
            return None

        legend_data_dict = legend_data.model_dump(exclude_unset=True)
        legend_db.sqlmodel_update(legend_data_dict)
        session.add(legend_db)
        session.commit()
        session.refresh(legend_db)

        return legend_db
    except Exception as e:
        return None
