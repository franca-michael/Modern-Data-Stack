import os
import pandas as pd
from db_connection import get_oltp_engine

def load_csv_to_postgres():
    """Lê todos os ficheiros CSV da pasta raw e envia-os para a base de dados OLTP."""
    
    data_dir = "data/raw"
    engine = get_oltp_engine()

    for filename in os.listdir(data_dir):
        if filename.endswith(".csv"):
            file_path = os.path.join(data_dir, filename)
            table_name = filename.replace(".csv", "")
            
            df = pd.read_csv(file_path)
            
            print(f"Enviando dados da tabela '{table_name}'...")
            df.to_sql(table_name, engine, if_exists='replace', index=False, chunksize=10000)
            print(f"Tabela '{table_name}' carregada com {len(df)} linhas!")

if __name__ == "__main__":
    load_csv_to_postgres()