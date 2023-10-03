import pandas as pd
from funciones import *
   
if __name__ == '__main__':
    # Códigos de patología según CIE-10
    categorias_covid = ['U07', 'B34', 'J120', 'J20']
    otras_categorias_estrechamente_vinculadas = ['J12','J80', 'B97','J02']
    filtro_categorias = categorias_covid + otras_categorias_estrechamente_vinculadas
    df = pd.read_csv("D:/- Lisandro/- Trust me I'm a software developer/Apps/datathon2023/datasets/consultas_por_patologia.csv")
    # Limpieza de valores
    df['fecha'] = pd.to_datetime(df['fecha'], format='%d-%m-%Y', errors='coerce')
    df = df.dropna(subset=['fecha'])
    # Limitación de tiempo considerando el primer caso de covid en Corrientes
    fecha_inicio = pd.to_datetime('2020-03-20')
    fecha_fin = pd.to_datetime('2022-12-31')
    df = df[(df['fecha'] >= fecha_inicio) & (df['fecha'] <= fecha_fin)]
    # Filtro segun categorias relacionadas al covid
    filtro = df['patologia_cod'].isin(filtro_categorias) 
    df = df[filtro]
    # Limpieza de valores nulos y erroneos
    df['consulta_cantidad'] = df['consulta_cantidad'].apply(lambda x: int(x) if not es_cadena(x) and not es_nulo(x) else encontrar_numero_entero_simple(x))
    df['rango_etario'] = df['rango_etario'].apply(lambda x: modificar_rango_etario(x) if es_cadena(x) else 'No declarado') 
    # DF a exportar
    df = df[['fecha','consulta_cantidad','patologia_desc', 'rango_etario', 'patologia_cod']]
    df.to_csv("D:/- Lisandro/- Trust me I'm a software developer/Apps/datathon2023/datasets/transform.csv")
