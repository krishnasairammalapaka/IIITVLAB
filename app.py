from flask import Flask, render_template, redirect, url_for, session, request
from auth import check_credentials, login_required
from routes.mono_alphabetic import mono_alphabetic
from routes.shift_cipher import shift_cipher
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

# Register blueprints
app.register_blueprint(mono_alphabetic)
app.register_blueprint(shift_cipher)

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if check_credentials(username, password):
            session['user'] = {
                'username': username,
                'email': f'{username}@example.com'
            }
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error='Invalid username or password')
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True) 