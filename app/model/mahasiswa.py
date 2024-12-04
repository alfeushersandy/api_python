from sqlalchemy import Table, MetaData, select, insert, update, delete

class MahasiswaModel:
    def __init__(self, db_config):
        self.db_config = db_config
        self.engine = db_config.get_connection()
        self.metadata = MetaData()
        
        # Definisi tabel tanpa membuat model
        self.mahasiswa = Table('mahasiswa', self.metadata, 
            autoload_with=self.engine
        )

    def get_all_mahasiswa(self):
        with self.engine.connect() as connection:
            query = select(self.mahasiswa)
            result = connection.execute(query)
            return result.fetchall()

    def get_mahasiswa_by_id(self, mahasiswa_id):
        with self.engine.connect() as connection:
            query = select(self.mahasiswa).where(self.mahasiswa.c.id == mahasiswa_id)
            result = connection.execute(query)
            return result.fetchone()

    def tambah_mahasiswa(self, data):
        with self.engine.connect() as connection:
            query = insert(self.mahasiswa).values(**data)
            result = connection.execute(query)
            connection.commit()
            return result.inserted_primary_key[0]

    def update_mahasiswa(self, mahasiswa_id, data):
        with self.engine.connect() as connection:
            query = update(self.mahasiswa).where(
                self.mahasiswa.c.id == mahasiswa_id
            ).values(**data)
            connection.execute(query)
            connection.commit()

    def hapus_mahasiswa(self, mahasiswa_id):
        with self.engine.connect() as connection:
            query = delete(self.mahasiswa).where(
                self.mahasiswa.c.id == mahasiswa_id
            )
            connection.execute(query)
            connection.commit()