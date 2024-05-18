from proje import db,app

class hassan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    
    
# with app.app_context():
#     db.create_all()