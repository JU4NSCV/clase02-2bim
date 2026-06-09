"""
    Mostrar los actores de cada país.
"""

import streamlit as st
import pandas as pd
from sqlalchemy import text
from modelo import get_engine

def con3():
    engine = get_engine()
    st.subheader("3. Actores por país")
    
    query = """
        SELECT
            pais.nombre as pais,
            actor.nombre as actor,
            actor.rol as rol,
            actor.edad as edad
        FROM pais
        INNER JOIN actor ON pais.id = actor.pais_id
        ORDER BY pais.nombre, actor.nombre
    """
    df = pd.read_sql(text(query), engine.connect())
    st.dataframe(df)
