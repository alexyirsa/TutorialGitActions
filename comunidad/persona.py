import datetime
from comunidad.base import Session, engine, Base
from sqlalchemy import Column, Integer, String

class Persona(Base):

   __tablename__ = 'persona'
   id = Column(Integer, primary_key=True)
   nombre = Column(String)
   edad = Column(Integer)

   def __init__(self, nombre, edad):
       self.nombre = nombre
       self.edad = edad

   def asignar_edad(self, edad):
       self.edad = edad

   def asignar_nombre(self, nombre):
       self.nombre = nombre

   def dar_edad(self):
       return(self.edad)

   def dar_nombre(self):
       return(self.nombre)

   def calcular_anio_nacimiento(self, ya_cumplio_anios):
       anio_actual = datetime.datetime.now().year
       if ya_cumplio_anios:
           return (anio_actual - self.edad)
       else:
           return (anio_actual - self.edad + 1)

   def almacenar(self):
       Base.metadata.create_all(engine)
       session = Session()
       session.add(self)
       session.commit()
       session.close()

   def recuperar(self, nombre, edad):
       session = Session()
       persona = session.query(Persona).filter(Persona.nombre == nombre and Persona.edad == edad).first()
       session.close()
       self.nombre = persona.nombre
       self.edad = persona.edad
       self.id = persona.id