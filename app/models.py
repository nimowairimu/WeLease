class Lease(db.Model):
  id = db.Column(db.Integer,primary_key=True)
  size = db.Column(db.Integer,nullable=False)
  location = db.Column(db.String(250),nullable=False)
  cost = db.Column(db.Integer,nullable=False)
  date_added = db.Column(db.DateTime,default=datetime.utcnow)

  def __repr__(self):
    return '<Location %r>' % self.id

   
  