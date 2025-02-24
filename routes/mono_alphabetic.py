from flask import Blueprint, render_template
from functools import wraps
from flask import session, redirect, url_for

# Create blueprint with a unique name
mono_alphabetic_bp = Blueprint('mono_alphabetic', __name__)

# Login required decorator
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@mono_alphabetic_bp.route('/mono-alphabetic')
@login_required
def index():
    # Redirect to the aim page when clicking the main card
    return redirect(url_for('mono_alphabetic.aim'))

@mono_alphabetic_bp.route('/mono-alphabetic/aim')
@login_required
def aim():
    return render_template('pages/mono-alphabetic/aim.html')

@mono_alphabetic_bp.route('/mono-alphabetic/theory')
@login_required
def theory():
    return render_template('pages/mono-alphabetic/theory.html')

@mono_alphabetic_bp.route('/mono-alphabetic/objective')
@login_required
def objective():
    return render_template('pages/mono-alphabetic/objective.html')

@mono_alphabetic_bp.route('/mono-alphabetic/procedure')
@login_required
def procedure():
    return render_template('pages/mono-alphabetic/procedure.html')

@mono_alphabetic_bp.route('/mono-alphabetic/simulation')
@login_required
def simulation():
    return render_template('pages/mono-alphabetic/simulation.html')

@mono_alphabetic_bp.route('/mono-alphabetic/assignment')
@login_required
def assignment():
    return render_template('pages/mono-alphabetic/assignment.html')

@mono_alphabetic_bp.route('/mono-alphabetic/reference')
@login_required
def reference():
    return render_template('pages/mono-alphabetic/reference.html')

@mono_alphabetic_bp.route('/mono-alphabetic/feedback')
@login_required
def feedback():
    return render_template('pages/mono-alphabetic/feedback.html') 