from app.db.session import SessionLocal, Base, engine
from app.models.property import Inmueble

Base.metadata.create_all(bind=engine)

datos = [
    Inmueble(direccion="C/ Mayor 12", zona="centro", precio=185000, metros_cuadrados=70, habitaciones=2, descripcion="Piso reformado, luminoso, cerca del metro"),
    Inmueble(direccion="Av. del Norte 45", zona="norte", precio=195000, metros_cuadrados=85, habitaciones=3, descripcion="Terraza amplia, garaje incluido"),
    Inmueble(direccion="C/ Olivos 8", zona="norte", precio=240000, metros_cuadrados=110, habitaciones=4, descripcion="Chalet adosado con jardín"),
    Inmueble(direccion="Pza. del Sol 3", zona="centro", precio=320000, metros_cuadrados=95, habitaciones=3, descripcion="Ático con terraza y vistas"),
    Inmueble(direccion="C/ Río 21", zona="sur", precio=130000, metros_cuadrados=55, habitaciones=1, descripcion="Apartamento ideal para inversión"),
]

db = SessionLocal()
db.add_all(datos)
db.commit()
db.close()

print("Objetos de ejemplo insertados")