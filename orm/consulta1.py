"""
    obtener los premios de la plataformas:
    IberiaTV
    Berlin Stream
    Kiwi Stories

    Por cada serie presentar la serie y los actores
"""

import streamlit as st
import pandas as pd
from sqlalchemy import text
from modelo import get_engine

def con1():
    engine = get_engine()
    st.subheader("Consulta 1 - Premios de las plataformas")
    query_premios = """
        SELECT
            plataforma.nombre as plataforma,
            serie.titulo as serie,
            premio.nombre_premio as premio,
            premio.categoria as categoria
        FROM premio
        INNER JOIN serie ON premio.serie_id = serie.id
        INNER JOIN plataforma ON serie.plataforma_id = plataforma.id
        WHERE plataforma.nombre IN ('IberiaTV', 'Berlin Stream', 'Kiwi Stories')
        ORDER BY plataforma.nombre
    """
    df_premios = pd.read_sql(text(query_premios), engine.connect())
    st.dataframe(df_premios)

    st.subheader("Consulta 1 - Actores por serie en estas plataformas")
    query_actores = """
        SELECT
            plataforma.nombre as plataforma,
            serie.titulo as serie,
            actor.nombre as actor,
            actor.rol as rol
        FROM actor
        INNER JOIN serie ON actor.serie_id = serie.id
        INNER JOIN plataforma ON serie.plataforma_id = plataforma.id
        WHERE plataforma.nombre IN ('IberiaTV', 'Berlin Stream', 'Kiwi Stories')
        ORDER BY plataforma.nombre, serie.titulo
    """
    df_actores = pd.read_sql(text(query_actores), engine.connect())
    st.dataframe(df_actores)
