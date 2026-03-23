from flask import request, jsonify
from config import app, db
from models import Tasks

@app.route('/')
def home():
    return jsonify('home sweet home baby!')


@app.route('/tasks', methods = ['GET'])
def get_task():
    tasks = Tasks.query.all()
    todo = [task.to_json() for task in tasks]
    return jsonify(todo), 200


@app.route('/tasks', methods = ['POST'])
def add_task():
    data = request.json 
    new_task = Tasks(task = data['task'])
    db.session.add(new_task)
    db.session.commit()
    
    return jsonify({'message': 'task added successfully!'})



@app.route('/tasks/<int:task_id>', methods = ['PUT'])
def edit_task(task_id):
    todo = Tasks.query.get(task_id)
    if not todo:
        return jsonify({"Message": "task does not exist!"}), 404
    data = request.json
    todo.task = data['task']
    
    db.session.commit()
    
    return jsonify({'message': 'task upddated successfully!'}), 200




@app.route('/tasks/<int:task_id>', methods = ['DELETE'])
def delete_task(task_id):
    todo = Tasks.query.get(task_id)
    if not todo:
        return jsonify({'message': "This task does not exist!"}), 400
    
    db.session.delete(todo)
    db.session.commit()
    
    
    return jsonify({'message': 'task is deleted'})


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        if not Tasks.query.first():
            dummy_data =[
                Tasks(task = 'Cooking!'),
                Tasks(task = 'Readding!'),
                Tasks(task = 'Washiing!')
            ]
            
            
            db.session.add_all(dummy_data)
            db.session.commit()
            
    app.run (debug = True)
    

