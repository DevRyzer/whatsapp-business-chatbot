from sqlalchemy.orm import Session
from app.models.inmueble import Inmueble

def search_properties(
        db: Session, 
        zone: str | None = None,
        max_price: float | None = None,
        habitaciones_min: int | None = None
    ):
    query = db.query(Inmueble).filter(Inmueble.disponible == True)

    if zone is not None:
        query = query.filter(Inmueble.zona.ilike(f"%{zone}%"))
    if max_price is not None:
        query = query.filter(Inmueble.precio <= max_price)
    if habitaciones_min is not None:
        query = query.filter(Inmueble.habitaciones >= habitaciones_min)

    return [
        {
            "direccion": i.direccion, "zona": i.zona, "precio": i.precio,
            "metros": i.metros_cuadrados, "habitaciones": i.habitaciones,
            "descripcion": i.descripcion,
        }
        for i in query.limit(5).all()
    ]