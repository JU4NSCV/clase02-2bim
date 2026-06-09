from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Pais(Base):
    __tablename__ = 'pais'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    continente = Column(String(100))
    
    
    plataformas = relationship("Plataforma", back_populates="pais")
    series = relationship("Serie", back_populates="pais")
    actores = relationship("Actor", back_populates="pais")

class Plataforma(Base):
    __tablename__ = 'plataforma'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    suscriptores_millones = Column(Integer)
    pais_id = Column(Integer, ForeignKey('pais.id'))
    
    pais = relationship("Pais", back_populates="plataformas")
    series = relationship("Serie", back_populates="plataforma")

class Serie(Base):
    __tablename__ = 'serie'
    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(200), nullable=False)
    genero = Column(String(100))
    anio_estreno = Column(Integer)
    temporadas = Column(Integer)
    plataforma_id = Column(Integer, ForeignKey('plataforma.id'))
    pais_id = Column(Integer, ForeignKey('pais.id'))
    
    plataforma = relationship("Plataforma", back_populates="series")
    pais = relationship("Pais", back_populates="series")
    actores = relationship("Actor", back_populates="serie")
    premios = relationship("Premio", back_populates="serie")

class Actor(Base):
    __tablename__ = 'actor'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(150), nullable=False)
    edad = Column(Integer)
    rol = Column(String(100))
    pais_id = Column(Integer, ForeignKey('pais.id'))
    serie_id = Column(Integer, ForeignKey('serie.id'))
    
    pais = relationship("Pais", back_populates="actores")
    serie = relationship("Serie", back_populates="actores")

class Premio(Base):
    __tablename__ = 'premio'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre_premio = Column(String(200), nullable=False)
    categoria = Column(String(100))
    anio = Column(Integer)
    serie_id = Column(Integer, ForeignKey('serie.id'))
    serie = relationship("Serie", back_populates="premios")


engine = create_engine('sqlite:///data.db')

def get_engine():
    return engine
    
def init_db():
    Base.metadata.create_all(engine)
    print("Base de datos y tablas creadas con éxito.")

if __name__ == "__main__":
    init_db()