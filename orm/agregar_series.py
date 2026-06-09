import pandas as pd
from sqlalchemy.orm import sessionmaker
from modelo import engine, Serie, Plataforma, Pais

def migrar_datos():

    Session = sessionmaker(bind=engine)
    session = Session()

    df = pd.read_csv('../data/series.csv')

    for index, row in df.iterrows():
        serie_existente = session.query(Serie).filter_by(titulo=row['titulo']).first()
        if not serie_existente:
            plataforma = session.query(Plataforma).filter_by(nombre=row['plataforma']).first()
            pais = session.query(Pais).filter_by(nombre=row['pais']).first()
            
            serie = Serie(
                titulo=row['titulo'],
                genero=row['genero'],
                anio_estreno=row['anio_estreno'],
                temporadas=row['temporadas'],
                plataforma=plataforma,
                pais=pais
            )
            session.add(serie)
            
    session.commit()
    session.close()

if __name__ == "__main__":
    migrar_datos()
