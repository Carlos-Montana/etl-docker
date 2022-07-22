'''
Archivo simple que contiene funciones para un etl super sencillo
'''
from datetime import datetime
from sqlalchemy import create_engine, text
import pandas as pd


def mostrar(db_con: str) -> None:
    '''
    Muestra la cantidad de registros de la tabla

    Args:
        db_con (str): Datos de conexión con la base de datos
    '''
    engine = create_engine(db_con)
    query = "SELECT COUNT(*) FROM prueba"
    with engine.connect() as con:
        print(con.execute(text(query)).fetchall())

def load(df_load: pd.DataFrame, db_con: str) -> None:
    '''
    Carga el dataframe en la base de datos

    Args:
        df (pd.DataFrame): dataframe de datos
        db_con (str): Datos de conexión con la base de datos
    '''
    engine = create_engine(db_con)
    df_load.to_sql('prueba', con=engine, if_exists='replace', index=False)

def transform(df_transform: pd.DataFrame) -> pd.DataFrame:
    '''
    Agrega columna de fecha al dataframe

    Args:
        df (pd.DataFrame): dataframe de datos

    Returns:
        pd.DataFrame: devuelve dataframe con la columna fecha agregada
    '''
    df_transform['create_at'] = datetime.now().strftime('%d-%m-%Y')
    return df_transform

def extract(url: str) -> pd.DataFrame:
    '''
    Extrae dataframe para poderlos trabajar

    Args:
        url (str): Ruta donde se encuentra archivo.csv para cargar en un dataframe

    Returns:
        pd.DataFrame: devuelve el dataframe
    '''
    return pd.read_csv(url)

def run_pipeline(url: str, db_con: str):
    '''
    Fuención principal que ejecuta las otras funciones

    Args:
        url (str): Ruta donde se encuentra archivo.csv para cargar en un dataframe
        db_con (str): Datos de conexión con la base de datos
    '''
    df_extract = extract(url)
    df_nuevo = transform(df_extract)
    load(df_nuevo, db_con)
    mostrar(db_con)
