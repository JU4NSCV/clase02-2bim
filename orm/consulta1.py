"""
    TITULO DE SERIES CON EL PROMEDIO DE EDAD DE LOS ACTORES DE LA SERIE
"""

from sqlalchemy.orm import sessionmaker
from modelo import engine, Serie

Session = sessionmaker(bind=engine)
session = Session()

print("TITULO DE SERIES CON EL PROMEDIO DE EDAD DE LOS ACTORES DE LA SERIE")
resultados = session.query(Serie).all()
for s in resultados:
    promedio = s.obtener_edad_actores()
    print(f"Serie: {s.titulo} | Promedio: {promedio:.2f}")