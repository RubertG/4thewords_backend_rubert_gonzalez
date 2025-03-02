from pydantic import field_validator
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
    image_url: str = Field(max_length=500)
    
    @field_validator("image_url")
    @classmethod
    def validar_url(cls, value):
        if not value.startswith("http"):
            raise ValueError("La URL de la imagen debe comenzar con 'http'.")
        return value


class LegendCreate(LegendBase):
    pass


class LegendUpdate(LegendBase):
    pass
