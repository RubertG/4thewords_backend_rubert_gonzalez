from app.core.db import SessionDep
from sqlmodel import select
from app.models.legend_model import Legend

def get_all_legends(session: SessionDep) -> list[Legend] | None: 
    try:
        legends = session.exec(select(Legend)).all()
        
        return legends
    except Exception as e:
        return None