from sqlalchemy.orm import Session
from app.models.property import Property
from app.services.data_service import parse_property_data

def search_properties(
        db: Session, 
        zone: str | None = None,
        max_price: float | None = None,
        habitaciones_min: int | None = None
    ):
    data = db.query(Property).filter(Property.disponible == True)

    if zone is not None:
        data = data.filter(Property.zona.ilike(f"%{zone}%"))
    if max_price is not None:
        data = data.filter(Property.precio <= max_price)
    if habitaciones_min is not None:
        data = data.filter(Property.habitaciones >= habitaciones_min)

    return parse_property_data(data)

