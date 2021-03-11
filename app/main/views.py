from flask import render_template,request,redirect,url_for
from . import main
from flask_login import login_required
from ..models import Lease

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    key = bytes('key', encoding='utf-8')
    title = 'Home - Welcome to The best Movie Review Website Online'
    return render_template('index.html',title = title )


@main.route('/lease',methods=['POST','GET'])
def lease():

    '''
    View movie page function that returns the lease details page and its data
    '''
    if request.method == "POST":
        submit_lease = request.form[name]
        new_lease = Lease(name=submit_lease)
        db,session.add(new_lease)
        db.session.commit()
        return redirect ('/')
       
    else:
        return "You clicked this ..."
    title = "My lease list "
    # lease = Lease.query.order_by(Lease.date_added)
    return render_template('lease.html',title = title)

@main.route('/lease/<int:lease_id>')
def search_lease(lease_id):

    '''
    View movie page function that returns the lease details page and its data
    '''

    return render_template('search_lease.html',title = title)

