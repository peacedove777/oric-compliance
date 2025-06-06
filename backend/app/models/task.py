from app import db

class ComplianceTask(db.Model):
    id = db.Column(db.Integer, primary_key=True)