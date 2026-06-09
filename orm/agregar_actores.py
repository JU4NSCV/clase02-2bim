import pandas as pd
from sqlalchemy.orm import sessionmaker
from modelo import get_engine, Actor, Serie, Pais

def migrar_datos():
    engine = get_engine()
    Session = sessionmaker(bind=engine)
    session = Session()
    
    df = pd.read_csv('../data/actores.csv')
    
    for index, row in df.iterrows():
        actor_existente = session.query(Actor).filter_by(nombre=row['nombre'], edad=row['edad']).first()
        if not actor_existente:
            pais = session.query(Pais).filter_by(nombre=row['pais']).first()
            serie = session.query(Serie).filter_by(titulo=row['serie']).first()
            
            actor = Actor(
                nombre=row['nombre'],
                edad=row['edad'],
                pais=pais,
                serie=serie
            )
            session.add(actor)
            
    session.commit()
    session.close()

if __name__ == "__main__":
    migrar_datos()