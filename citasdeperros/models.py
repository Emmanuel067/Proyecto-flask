from database import Database
from sqlalchemy import Column, Integer, String, DateTime  # Import DateTime for date and time

class Citas(Database):
    __tablename__ = 'citas'
    id = Column(Integer, primary_key=True)
    nombre_mascota = Column(String(100))
    tipo_animal = Column(String(50))
    fecha_cita = Column(DateTime)
    observaciones = Column(String(200))

