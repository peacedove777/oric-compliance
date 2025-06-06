from app import db

class ComplianceLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)