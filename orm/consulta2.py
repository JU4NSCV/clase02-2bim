"""
    Mostrar todas las series de cada plataforma.
"""

import streamlit as st
import pandas as pd
from sqlalchemy import text
from modelo import get_engine

def con2():
    engine = get_engine()
    st.subheader("2. Series por plataforma")
    
    query = """
        SELECT
            plataforma.nombre as plataforma,
            serie.titulo as serie,
            serie.genero as genero,
            serie.temporadas as temporadas,
            serie.anio_estreno as anio_estreno
        FROM plataforma
        INNER JOIN serie ON plataforma.id = serie.plataforma_id
        ORDER BY plataforma.nombre, serie.titulo
    """
    df = pd.read_sql(text(query), engine.connect())
    st.dataframe(df)
