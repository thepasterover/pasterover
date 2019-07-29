from datetime import datetime
from seriously_portfolio import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_client(client_id):
    return Client.query.get(int(client_id))

class Client(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    message = db.Column(db.Text, nullable=False)
    date_submitted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
     
    def __repr__(self):
        return f"Client('{self.name}', '{self.email}', '{self.message}', '{self.date_submitted}')"