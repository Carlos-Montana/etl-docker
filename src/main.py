'''
Probando dockerfile y docker-compose
'''
from decouple import config
from etl import run_pipeline


if __name__=='__main__':
    URL_CSV = config('DB')
    DB_CON = config('DB_CONSTRUCT')
    run_pipeline(URL_CSV, DB_CON)
