import React from 'react'

const Form = ({ todo, setTodo, editId, handleSubmit }) => {
  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        placeholder="Add a task..."
        value={todo}
        onChange={(e) => setTodo(e.target.value)}
      />

      <button type="submit">{editId ? 'Update' : 'Add'}</button>
    </form>
  )
}

export default Form