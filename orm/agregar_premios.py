import pandas as pd
from sqlalchemy.orm import sessionmaker
from modelo import engine, Premio, Serie

def migrar_datos():

    Session = sessionmaker(bind=engine)
    session = Session()

    df = pd.read_csv('../data/premios.csv')

    for index, row in df.iterrows():
        serie = session.query(Serie).filter_by(titulo=row['serie']).first()
        premio = Premio(
            nombre_premio=row['nombre_premio'],
            categoria=row['categoria'],
            anio=row['anio'],
            serie=serie
        )
        session.add(premio)
    session.commit()
    session.close()

if __name__ == "__main__":
    migrar_datos()
