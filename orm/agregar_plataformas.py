import pandas as pd
from sqlalchemy.orm import sessionmaker
from modelo import get_engine, Pais, Plataforma

def migrar_datos():
    engine = get_engine()
    Session = sessionmaker(bind=engine)
    session = Session()

    df = pd.read_csv('../data/plataformas.csv')

    for index, row in df.iterrows():
        pais = session.query(Pais).filter_by(nombre=row['pais']).first()
        plataforma = Plataforma(
            nombre=row['nombre'],
            suscriptores_millones=row['suscriptores_millones'],
            pais=pais
        )
        session.add(plataforma)
    session.commit()
    session.close()

if __name__ == "__main__":
    migrar_datos()