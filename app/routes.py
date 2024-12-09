from app import app, response
from app.controller import UserController
from flask import request
from flask import jsonify, render_template
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_cors import CORS  # Untuk mengizinkan CORS


CORS(app)  # Mengaktifkan CORS agar bisa diakses oleh aplikasi Flutter

@app.route('/')
def beranda():
    return render_template('beranda.html',template_folder='app/templates')

# Route untuk Chatbot
@app.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')

# Route untuk Scan Kamera
@app.route('/scan_kamera')
def scan_kamera():
    return render_template('scan_kamera.html')

# Route untuk Profil
@app.route('/profile')
def profil():
    return render_template('profile.html')

# Route untuk Outfit
@app.route('/outfit')
def outfit():
    return render_template('outfit.html')

# Route untuk Login
@app.route('/auth')
def login():
    return render_template('login.html')

# Route untuk Registrasi
@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/login', methods=['POST'])
def logins():
    return UserController.login()

# Route untuk Forgot Password
@app.route('/forgot')
def forgot():
    return render_template('forgot.html')