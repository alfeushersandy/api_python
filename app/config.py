# app/config.py
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# Load environment variables
load_dotenv()

class Config:
    def __init__(self):
        self.host = os.getenv('DB_HOST')
        self.port = os.getenv('DB_PORT')
        self.name = os.getenv('DB_NAME')
        self.user = os.getenv('DB_USER')
        self.password = os.getenv('DB_PASSWORD')
        
        # Connection string untuk SQL Server
        self.connection_string = (
            f'mssql+pyodbc://{self.user}:{self.password}@{self.host}:{self.port}/{self.name}'
            '?driver=ODBC+Driver+17+for+SQL+Server'
        )
        
        self.engine = create_engine(self.connection_string)
        self.session = scoped_session(sessionmaker(bind=self.engine))

        try:
            connection =  self.engine.connect()
            print("koneksi berhasil")
            connection.close()
        except Exception as e:
            print(f'gagal koneksi ke database: {e}')

        

    def get_connection(self):
        return self.engine

    def get_session(self):
        return self.session