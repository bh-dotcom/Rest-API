from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, index=True)  # Indexed for performance
    amount = db.Column(db.Float)
    status = db.Column(db.String(50))
