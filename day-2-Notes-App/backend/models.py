from config import db 
from datetime import datetime


class Notes(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(50), nullable = False, unique = False)
    content = db.Column(db.String(500), nullable = False, unique = False)
    date = db.Column(db.DateTime, nullable =False, default = datetime.utcnow)
    
    
    def to_json(self):
        return {
            "id": self.id, 
            "title": self.title, 
            "content": self.content, 
            "date": self.date
            }
    