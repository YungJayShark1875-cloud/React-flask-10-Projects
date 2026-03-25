from flask import request, jsonify
from config import app, db
from models import Notes

@app.route('/')
def Home():
    return jsonify('This Is Home Baby!')


@app.route('/notes', methods = ["GET"])
def get_data():
    data = Notes.query.all()
    note_data = [note.to_json() for note in data]
    return jsonify(note_data), 200


@app.route('/notes', methods= ["POST"])
def add_data():
    data = request.json
    new_data = Notes(title = data['title'], content = data['content'])
    db.session.add(new_data)
    db.session.commit()
    
    return jsonify({'message': 'User Added'}), 201
    
    
    
@app.route('/notes/<int:note_id>', methods = ["PUT"])
def edit_user(note_id):
    note = Notes.query.get(note_id)
    if not note:
        return jsonify({"Message": "note does not exist!"}), 404
    data = request.json
    note.title = data["title"]
    note.date = data["date"]
    db.session.commit()
    
    return jsonify({"message": "note updated"}), 200
            
            
            
@app.route('/notes/<int:notes_id>', methods = ["DELETE"])
def delete_user(note_id):
    note = Notes.query.get(note_id)
    if not note:
        return jsonify({"Message": "The note does not Exist!"}),400
    
    db.session.delete(note)
    db.session.commit()
    
    
    return jsonify({"message": "User deleted"})
    
if __name__ == '__main__':
   with app.app_context():
     db.create_all()
     if not Notes.query.first():
            dummy_data = [
                Notes(title="Conference of viana", content="How ever Our Souls are made of..."),
                Notes(title="Kill The Boy..", content="Kill the Boy and let the man in you grow.."),
                         ]
            
            db.session.add_all(dummy_data)
            db.session.commit()
            
     app.run (debug=True)