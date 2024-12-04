from flask import request, jsonify
from app.model.mahasiswa import MahasiswaModel

class MahasiswaController:
    def __init__(self, db_config):
        self.model = MahasiswaModel(db_config)

    def index(self):
        try:
            mahasiswa = self.model.get_all_mahasiswa()
            return jsonify(
                {
                    'status' : 200,
                    'Message' : 'Berhasil mengambil data mahasiswa',
                    'data' : [ 
                        {
                            'id' : row.id,
                            'nama' : row.nama,
                            'nim' : row.nim,
                            'jurusan' : row.jurusan
                        } for row in mahasiswa 
                    ] 
                } 
            ), 200
        except Exception as e:
            return jsonify({'error' : str(e)}), 500

    def tambah(self):
            data = {
                'nim': request.form['nim'],
                'nama': request.form['nama'],
                'jurusan': request.form['jurusan']
            }
            try:
                self.model.tambah_mahasiswa(data)
                return jsonify(
                    {
                        'status': 201,
                        'Message': 'Berhasil Menambahkan Mahasiswa',
                        'data' : data
                    }
                ), 201
            except Exception as e:
                return jsonify({
                    'status': 500,
                    'Message': str(e)
                }), 500

    def edit(self, mahasiswa_id):
            data = {
                'nim': request.form['nim'],
                'nama': request.form['nama'],
                'jurusan': request.form['jurusan']
            }
            try:
                self.model.update_mahasiswa(mahasiswa_id, data)
                return jsonify({
                     'status' : 200,
                     'Message': 'Berhasil mengupdate data'
                }), 200
            except Exception as e:
                return jsonify({'status' : 500, 'Message': f'Gagal update data : {e}'})

    def hapus(self, mahasiswa_id):
        try:
            self.model.hapus_mahasiswa(mahasiswa_id)
            return jsonify({
                 'status' : 200,
                 'Message': 'Data Mahasiswa berhasil dihapus'
            })
        except Exception as e:
            return jsonify({'Error' : 'str{e}'}), 500