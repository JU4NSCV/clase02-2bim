import pandas as pd
import os
from sqlalchemy.orm import sessionmaker
from modelo import get_engine, Pais, init_db

def migrar_datos():

    engine = get_engine()
    Session = sessionmaker(bind=engine)
    session = Session()
    archivos_paises = ['../data/paises.csv', '../data/countries.csv']
    
    for archivo in archivos_paises:
        if os.path.exists(archivo):
            df = pd.read_csv(archivo)
            for index, row in df.iterrows():
                pais_existente = session.query(Pais).filter_by(nombre=row['nombre']).first()
                if not pais_existente:
                    pais = Pais(nombre=row['nombre'], continente=row['continente'])
                    session.add(pais)
            session.commit()
            
    session.close()

if __name__ == "__main__":
    migrar_datos()