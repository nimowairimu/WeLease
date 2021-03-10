from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')

@app.route('/lease/<int:lease_id>')
def lease(lease_id):

    '''
    View movie page function that returns the lease details page and its data
    '''
    title = f'lease this property {lease_id}'
    return render_template('lease.html',title = title)

