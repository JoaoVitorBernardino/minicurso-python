import psycopg 
from dotenv import dotenv_values

config = dotenv_values('../.env')

def get_connection():
    try:
        conn = psycopg.connect(
            host=config["POSTGRES_HOST"],
            port=config["POSTGRES_PORT"],
            dbname=config["POSTGRES_NAME"],
            user=config["POSTGRES_USER"],
            password=config["POSTGRES_PASSWORD"]
        )
        return conn
    except psycopg.Error as e:
        print(f"Erro ao conectar ao PostgreSQL: {e}")
        return None
    
def close_connection(conn):
    if conn is not None:
        conn.close()    
    