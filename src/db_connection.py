# src/db_connection.py
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

def get_oltp_engine():
    """Cria e retorna a engine de conexão com o banco OLTP simulado."""
    user = os.getenv("OLTP_USER").strip()
    password = os.getenv("OLTP_PASSWORD").strip()
    db = os.getenv("OLTP_DB").strip()
    host = "localhost"
    port = "5434" 
    
    connection_string = f"postgresql://{user}:{password}@{host}:{port}/{db}?client_encoding=utf8"
    engine = create_engine(connection_string)
    
    return engine

def get_olap_engine():
    """Cria e retorna a engine de conexão com o banco OLAP (Data Warehouse)."""
    user = os.getenv("OLAP_USER").strip()
    password = os.getenv("OLAP_PASSWORD").strip()
    db = os.getenv("OLAP_DB").strip()
    host = "localhost"
    port = "5435" 
    
    connection_string = f"postgresql://{user}:{password}@{host}:{port}/{db}?client_encoding=utf8"
    engine = create_engine(connection_string)
    
    return engine

if __name__ == "__main__":
    print("Iniciando teste de conexão...")
    engine = get_oltp_engine()
    try:
        with engine.connect() as conn:
            print("Sucesso! Conexao com o banco OLTP estabelecida.")
    except Exception as e:
        print(f"Erro ao conectar: {repr(e)}")