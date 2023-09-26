import pandas as pd 

def es_numero_entero(valor):
    try:
        int(valor)
        return True
    except ValueError:
        return False
    
        
enfermedades_por_covid = ["BRONQUITIS AGUDA","TOS","INFECCIONES AGUDAS DE LAS VIAS RESPIRATORIAS SUPERIORES, DE SITIOS NOESPECIFICADOS","FARINGITIS AGUDA"]
df = pd.read_csv("D:\- Lisandro\- Trust me I'm a software developer\Apps\datathon2023\datasets\consultas_por_patologia.csv")
# Limpieza de valores
df['fecha'] = pd.to_datetime(df['fecha'], format='%d-%m-%Y', errors='coerce')
df = df.dropna(subset=['patologia_desc'])
df = df.dropna(subset=['fecha'])
df['consulta_cantidad'] = df['consulta_cantidad'].apply(lambda x: int(x) if es_numero_entero(x) else 1)
df['consulta_cantidad'] = df['consulta_cantidad'].fillna(1) # Un solo registro sin la cantidad de cons. especificados, se rellena con 1
# Limitación de tiempo considerando fecha de inicio del covid en Corrientes y cantidad de datos por tiempo en el archivo csv
fecha_inicio = pd.to_datetime('2020-03-20')
fecha_fin = pd.to_datetime('2022-12-31')
df = df[(df['fecha'] >= fecha_inicio) & (df['fecha'] <= fecha_fin)]
# Filtro por enfermedades relacionadas con el covid
df = df[['fecha','consulta_cantidad','patologia_desc']]
filtro = df['patologia_desc'].isin(enfermedades_por_covid)
df = df[filtro]
df.to_csv("D:\- Lisandro\- Trust me I'm a software developer\Apps\datathon2023\datasets\patologia_data.csv", index=False)

