from sqlmodel import Field
from datetime import datetime
from app.schemas.legend_schema import LegendBase


class Legend(LegendBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    image_url: str = Field(max_length=500)
    created_at: datetime = Field(default_factory=datetime.now)
