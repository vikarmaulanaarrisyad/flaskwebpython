from app import response  # Pastikan impor ini ada
from app.model.user import User
from app import db
from flask import request
from flask_jwt_extended import *  # Jangan lupa mengimpor semua yang dibutuhkan dari flask_jwt_extended
import datetime

def buatAdmin():
    try:
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        level = 1
        
        users = User(name=name, email=email, level=level)
        users.setPassword(password)
        db.session.add(users)
        db.session.commit()

        return response.success('', 'Sukses Menambahkan Data Admin!')
    
    except Exception as e:
        print(e)
        return response.badRequest([], 'Terjadi kesalahan pada server')

# Fungsi untuk register pengguna baru
def register():
    try:
        name = request.json.get('name')
        email = request.json.get('email')
        password = request.json.get('password')
        level = 2  # User biasa
        
        if not name or not email or not password:
            return response.badRequest([], 'Semua field harus diisi')

        # Cek apakah email sudah ada
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return response.badRequest([], 'Email sudah terdaftar')

        # Menyimpan user baru
        users = User(name=name, email=email, level=level)
        users.setPassword(password)
        db.session.add(users)
        db.session.commit()

        return response.success('', 'Sukses Menambahkan Data Baru!')
    
    except Exception as e:
        print(e)
        return response.badRequest([], 'Terjadi kesalahan pada server')

def singleObject(data):
    data = {
        'id': data.id,
        'name': data.name,
        'email': data.email,
        'level': data.level
    }
    
    return data

def login():
    try:
        email = request.json.get('email')
        password = request.json.get('password')

        # Cek apakah email terdaftar
        user = User.query.filter_by(email=email).first()
        if not user:
            return response.badRequest([], 'Email tidak terdaftar')

        # Cek apakah password benar
        if not user.checkPassword(password):
            return response.badRequest([], 'Kombinasi password salah')

        # Data user yang akan dikembalikan
        data = {
            'id': user.id,
            'name': user.name,
            'email': user.email,
            'level': user.level
        }

        # Menentukan waktu kedaluwarsa untuk token
        expires = datetime.timedelta(days=7)
        expires_refresh = datetime.timedelta(days=7)

        # Membuat access token dan refresh token
        access_token = create_access_token(identity=data, fresh=True, expires_delta=expires)
        refresh_token = create_refresh_token(identity=data, expires_delta=expires_refresh)

        return response.success({
            "data": data,
            "access_token": access_token,
            "refresh_token": refresh_token,
        }, "Sukses Login!")

    except Exception as e:
        print(e)
        return response.badRequest([], 'Terjadi kesalahan pada server')