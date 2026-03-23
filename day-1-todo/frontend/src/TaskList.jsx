import React from 'react'

const TaskList = ({ tasks, setTodo, setEditId, handleDelete }) => {
  return (
    <ul>
      {tasks.map((task) => (
        <li key={task.id}>
          <span>{task.task}</span>
          <div className="task-actions">
            <button
              type="button"
              className="edit-btn"
              onClick={() => {
                setTodo(task.task)
                setEditId(task.id)
              }}
            >
              Edit
            </button>
            <button
              type="button"
              className="delete-btn"
              onClick={() => handleDelete(task.id)}
            >
              Delete
            </button>
          </div>
        </li>
      ))}
    </ul>
  )
}

export default TaskList