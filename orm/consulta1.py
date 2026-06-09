"""
    TITULO DE SERIES CON EL PROMEDIO DE EDAD DE LOS ACTORES DE LA SERIE
"""

import streamlit as st
import pandas as pd
from sqlalchemy import text
from modelo import get_engine

def con1():
    engine = get_engine()
    st.subheader("1. Promedio de edad de los actores por serie")
    
    query = """
        SELECT
            serie.titulo AS "Título de la Serie",
            AVG(actor.edad) AS "Promedio de Edad"
        FROM serie
        INNER JOIN actor ON serie.id = actor.serie_id
        GROUP BY serie.id, serie.titulo
        ORDER BY "Promedio de Edad" DESC
    """
    with engine.connect() as conn:
        df = pd.read_sql(text(query), conn)
    st.dataframe(df)
