"""
    TITULO DE SERIES CON EL PROMEDIO DE EDAD DE LOS ACTORES DE LA SERIE Y CUANTOS PREMIOS TIENE
"""

from sqlalchemy.orm import sessionmaker
from modelo import engine, Serie

Session = sessionmaker(bind=engine)
session = Session()

print("TITULO DE SERIES CON EL PROMEDIO DE EDAD DE LOS ACTORES DE LA SERIE Y CUANTOS PREMIOS TIENE")
resultados = session.query(Serie).all()
for s in resultados:
    promedio = s.obtener_edad_actores()
    cantidad_premios = s.obtener_num_premios()
    print(f"Serie: {s.titulo} | Promedio: {promedio:.2f} | Premios: {cantidad_premios}")