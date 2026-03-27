from flask import request, jsonify
from config import app, db
from models import Notes

@app.route('/')
def Home():
    return jsonify('This Is Home Baby!')

@app.route('/notes', methods = ['GET'])
def get_note():
    notes = Notes.query.all()
    noteData = [note.to_json() for note in notes]

    return jsonify(noteData), 200

@app.route('/notes', methods = ["POST"])
def add_data():
    data = request.json
    new_note = Notes(title = data['title'], content = data['content'])
    db.session.add(new_note)
    db.session.commit()
    
    return jsonify({'message': 'Note Added'}), 201


@app.route('/notes/<int:note_id>', methods = ["PUT"])
def edit_user(note_id):   
    note = Notes.query.get(note_id)
    if not note:
        return jsonify({"Message": "note does not exist!"}), 404
    
    data = request.json
    
    note.title = data['title']
    note.content = data['content']
    
    db.session.commit()
    
    return jsonify({"message": "note updated"}), 200
            
            
            
@app.route('/notes/<int:note_id>', methods = ["DELETE"])
def delete_note(note_id):
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
                Notes(title="To Kill a MockingBird ", content="It's when you know you're licked before you begin but you begin anyway"),
                Notes(title="The Little Prince ", content="Essential is invisible.."),
                Notes(title = "A Tale of Two Cities ", content = "Best of times...")
                         ]
            
            db.session.add_all(dummy_data)
            db.session.commit()
            
     app.run (debug=True)