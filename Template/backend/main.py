from flask import request, jsonify
from config import app, db
from models import Users

@app.route('/')
def Home():
    return jsonify('This Is Home Baby!')


@app.route('/users', methods = ["GET"])
def get_data():
    data = Users.query.all()
    user_info = [user.to_json() for user in data]
    return jsonify(user_info), 200


@app.route('/users', methods= ["POST"])
def add_data():
    data = request.json
    print(data)
    new_user =Users(name = data["name"], age = data["age"])
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({'message': 'User Added'}), 201
    
    
    
@app.route('/users/<int:user_id>', methods = ["PUT"])
def edit_user(user_id):
    user = Users.query.get(user_id)
    if not user:
        return jsonify({"Message": "user does not exist!"}), 404
    data = request.json
    user.name = data["name"]
    user.age = data["age"]
    db.session.commit()
    
    return jsonify({"message": "User updated"}), 200
            
            
            
@app.route('/users/<int:user_id>', methods = ["DELETE"])
def delete_user(user_id):
    user = Users.query.get(user_id)
    if not user:
        return jsonify({"Message": "This user do Isn't Exist!"}),400
    
    db.session.delete(user)
    db.session.commit()
    
    
    return jsonify({"message": "User deleted"})
    
if __name__ == '__main__':
   with app.app_context():
     db.create_all()
     if not Users.query.first():
            dummy_data = [
                Users(name="Alice", age="34"),
                Users(name="Jaden", age="45"),
                Users(name="Helen", age="23"),
                Users(name="Edward", age="31"),
                         ]
            
            db.session.add_all(dummy_data)
            db.session.commit()
            
     app.run (debug=True)