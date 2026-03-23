from config import db 


class Users(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(120), nullable = False, unique = False)
    age = db.Column(db.Integer(), unique = False)
    
    def to_json(self):
        return {"id": self.id, "name": self.name, "age": self.age}
    