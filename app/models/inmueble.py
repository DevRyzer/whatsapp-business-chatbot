from sqlalchemy import Column, Integer, String, Float, Boolean
from app.db.session import Base

class Inmueble(Base):
    __tablename__ = "inmuebles"

    id = Column(Integer, primary_key=True)
    direccion = Column(String, nullable=False)
    zona = Column(String, nullable=False)
    precio = Column(Float, nullable=False)
    metros_cuadrados = Column(Integer)
    habitaciones = Column(Integer)
    disponible = Column(Boolean, default=True)
    descripcion = Column(String)