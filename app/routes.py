from app import app, response
from app.controller import UserController
from flask import request
from flask import jsonify, render_template,  redirect, url_for
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_cors import CORS  # Untuk mengizinkan CORS

CORS(app)  # Mengaktifkan CORS agar bisa diakses oleh aplikasi Flutter

@app.route('/api/login', methods=['POST'])
def api_login():
    return UserController.login()
    
@app.route('/api/register', methods=['POST'])
def api_register():
    return UserController.register()

@app.route('/')
def beranda():
    return render_template('beranda.html',template_folder='app/templates')

@app.route('/logout')
def logout():
    return redirect(url_for('beranda'))

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
@app.route('/auth/login')
def login_page():
    return render_template('login.html')

# Route untuk Registrasi
@app.route('/auth/register')
def register_page():
    return render_template('register.html')

# Route untuk Forgot Password
@app.route('/forgot')
def forgot():
    return render_template('forgot.html')


