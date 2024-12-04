import os
from flask import Flask
from app.config import Config
from app.controller.mahasiswa import MahasiswaController
from app.routes.mahasiswa_route import init_mahasiswa_routes

def create_app():
    app = Flask(__name__, template_folder='templates')
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

    # Konfigurasi Database
    db_config = Config()
    
    # Inisialisasi Controller,Blueprint mahasiswa
    mahasiswa_controller = MahasiswaController(db_config)
    mahasiswa_routes = init_mahasiswa_routes(mahasiswa_controller)
    app.register_blueprint(mahasiswa_routes, url_prefix='/mahasiswa')


    return app