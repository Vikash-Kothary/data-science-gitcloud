
from flask import Blueprint
from flask import render_template

views = Blueprint('views', __name__,
	static_folder='static', 
	static_url_path='', 
	template_folder='templates')

@views.route('/')
def index():
    return render_template('index.html')

@views.route('/repos')
def repos():
    return render_template('repos.html')