from config import db
class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    task = db.Column(db.String(200), nullable = False, unique = False)

    
    def to_json(self):
        return {
            'id': self.id, 'task': self.task
        }