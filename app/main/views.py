from flask import render_template,request,redirect,url_for,Response,flash
from . import main
from flask_login import login_required
from ..models import Lease
from .. import db,photos

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    
    title = 'Home - Welcome to The best Movie Review Website Online'
    return render_template('home.html')


@main.route('/lease',methods=['POST','GET'])
def lease():

    '''
    View lease page function that returns the lease details page and its data
    '''
     


    title = "My lease list "
    # lease = Lease.query.order_by(Lease.date_added)
    return render_template('lease.html',title = title)

@main.route('/lease/<int:lease_id>')
def search_lease(lease_id):

    '''
    View lease page function that returns the lease details page and its data
    '''

    Location = Lease.query.filter_by(Lease.location).sort()
    Size = Lease.query.filter_by(Lease.size).sort()
    Cost = Lease.query.filter_by(Lease.cost).sort()

    return render_template('search_lease.html',title = title)

@main.route('/properties')
def home():
    return render_template('index.html')

@login_required
@main.route('/leaser')
def lease_mine():
     
    
    flash('Your request has been received . We will contact you for more details')
        
   
    return render_template('lease_mine.html')
    redirect(url_for("main.home")) 

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def upload_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.lease_mine',uname=uname))

