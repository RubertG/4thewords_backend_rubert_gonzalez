from pydantic import HttpUrl
from datetime import date
from sqlmodel import SQLModel, Field


class LegendBase(SQLModel):
    name: str = Field(max_length=255)
    category: str = Field(max_length=100)
    description: str
    legend_date: date
    province: str = Field(max_length=100)
    canton: str = Field(max_length=100)
    district: str = Field(max_length=100)
    image_url: HttpUrl = Field(max_length=500)


class LegendCreate(LegendBase):
    pass


class LegendUpdate(LegendBase):
    pass
