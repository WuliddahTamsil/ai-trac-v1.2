import os
from flask import Blueprint, render_template
ml_bp = Blueprint('ml', __name__)

@ml_bp.route('/ml-monitor')
def index():
    ml_backend_url = os.getenv('ML_BACKEND_URL', '') or ''
    ml_backend_url = ml_backend_url.rstrip('/')
    return render_template('pages/ml_monitor.html', active='ml', ml_backend_url=ml_backend_url)
