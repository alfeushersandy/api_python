from flask import Blueprint

def init_mahasiswa_routes(mahasiswa_controller):
    mahasiswa_bp = Blueprint('mahasiswa', __name__)

    # Route untuk index/list mahasiswa
    mahasiswa_bp.route('/', methods=['GET'])(mahasiswa_controller.index)

    # Route untuk tambah mahasiswa
    mahasiswa_bp.route('/tambah', methods=['POST'])(mahasiswa_controller.tambah)

    # Route untuk edit mahasiswa
    mahasiswa_bp.route('/edit/<int:mahasiswa_id>', methods=['PUT'])(mahasiswa_controller.edit)

    # Route untuk hapus mahasiswa
    mahasiswa_bp.route('/hapus/<int:mahasiswa_id>', methods=['DELETE'])(mahasiswa_controller.hapus)

    return mahasiswa_bp