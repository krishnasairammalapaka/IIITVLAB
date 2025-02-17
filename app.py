from flask import Flask, render_template, redirect, url_for, flash, jsonify, session
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Change this to a secure secret key

# Login required decorator
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# Routes
@app.route('/')
@login_required
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Add your login logic here
    # For demonstration, we'll just set a session
    session['user'] = 'demo_user'
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.clear()
    return jsonify({'success': True, 'message': 'Logged out successfully'})

# Cryptography algorithm routes
@app.route('/shift-cipher')
@login_required
def shift_cipher():
    # Redirect to the aim page when clicking the main card
    return redirect(url_for('shift_cipher_aim'))

@app.route('/mono-alphabetic')
@login_required
def mono_alphabetic():
    # Redirect to the aim page when clicking the main card
    return redirect(url_for('mono_alphabetic_aim'))

@app.route('/one-time-pad')
@login_required
def one_time_pad():
    return render_template('pages/one-time-pad.html')

# Add more routes for other algorithms...

@app.route('/hash-functions')
@login_required
def hash_functions():
    return render_template('pages/hash-functions.html')

@app.route('/des')
@login_required
def des():
    return render_template('pages/des.html')

@app.route('/aes')
@login_required
def aes():
    return render_template('pages/aes.html')

@app.route('/diffie-hellman')
@login_required
def diffie_hellman():
    return render_template('pages/diffie-hellman.html')

@app.route('/public-key')
@login_required
def public_key():
    return render_template('pages/public-key.html')

@app.route('/digital-signatures')
@login_required
def digital_signatures():
    return render_template('pages/digital-signatures.html')

@app.route('/message-auth')
@login_required
def message_auth():
    return render_template('pages/message-auth.html')

# Add these routes for shift cipher pages
@app.route('/shift-cipher/aim')
@login_required
def shift_cipher_aim():
    return render_template('pages/shift-cipher/aim.html')

@app.route('/shift-cipher/theory')
@login_required
def shift_cipher_theory():
    return render_template('pages/shift-cipher/theory.html')

@app.route('/shift-cipher/objective')
@login_required
def shift_cipher_objective():
    return render_template('pages/shift-cipher/objective.html')

@app.route('/shift-cipher/procedure')
@login_required
def shift_cipher_procedure():
    return render_template('pages/shift-cipher/procedure.html')

@app.route('/shift-cipher/simulation')
@login_required
def shift_cipher_simulation():
    return render_template('pages/shift-cipher/simulation.html')

@app.route('/shift-cipher/assignment')
@login_required
def shift_cipher_assignment():
    return render_template('pages/shift-cipher/assignment.html')

@app.route('/shift-cipher/reference')
@login_required
def shift_cipher_reference():
    return render_template('pages/shift-cipher/reference.html')

@app.route('/shift-cipher/feedback')
@login_required
def shift_cipher_feedback():
    return render_template('pages/shift-cipher/feedback.html')

# Add these routes for mono-alphabetic cipher pages
@app.route('/mono-alphabetic/aim')
@login_required
def mono_alphabetic_aim():
    return render_template('pages/mono-alphabetic/aim.html')

@app.route('/mono-alphabetic/theory')
@login_required
def mono_alphabetic_theory():
    return render_template('pages/mono-alphabetic/theory.html')

@app.route('/mono-alphabetic/objective')
@login_required
def mono_alphabetic_objective():
    return render_template('pages/mono-alphabetic/objective.html')

@app.route('/mono-alphabetic/procedure')
@login_required
def mono_alphabetic_procedure():
    return render_template('pages/mono-alphabetic/procedure.html')

@app.route('/mono-alphabetic/simulation')
@login_required
def mono_alphabetic_simulation():
    return render_template('pages/mono-alphabetic/simulation.html')

@app.route('/mono-alphabetic/assignment')
@login_required
def mono_alphabetic_assignment():
    return render_template('pages/mono-alphabetic/assignment.html')

@app.route('/mono-alphabetic/reference')
@login_required
def mono_alphabetic_reference():
    return render_template('pages/mono-alphabetic/reference.html')

@app.route('/mono-alphabetic/feedback')
@login_required
def mono_alphabetic_feedback():
    return render_template('pages/mono-alphabetic/feedback.html')

if __name__ == '__main__':
    app.run(debug=True) 