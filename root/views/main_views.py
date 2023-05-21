# views/main_views.py

from flask import Blueprint, render_template

bp = Blueprint('main', __name__, url_prefix='/')
    
@bp.route('/')
def index():
    return render_template("index.html")