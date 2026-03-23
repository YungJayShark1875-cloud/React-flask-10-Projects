import { useState, useEffect } from 'react'
import { getData, sendData, updateData, deleteData } from './Api'
import './App.css'
import Form from './Form'
import TaskList from './TaskList'

function App() {
 const [tasks, setTasks] = useState([])
 const [todo, setTodo] = useState('')
 const [editId, setEditId] = useState(null)
 const [theme, setTheme] = useState('dark')

 const loadTask = async() =>{
  const data = await getData()
  setTasks(data)
  console.log(data);
 }

 useEffect(() => {
  loadTask()
 }, []);

 useEffect(()=>{
  document.documentElement.setAttribute('data-theme', theme)
 },[theme])

 const handleSubmit = async (e)=>{
   e.preventDefault()
  if(editId){
    await updateData(editId, {task:todo})
    setEditId(null)
  }else{
    await sendData(todo)
  }

  setTodo('')

  loadTask()
 }

 const handleDelete = async (id) =>{
  await deleteData(id)

  loadTask()
 }
  const toggleTheme = () => setTheme((prev) => prev === 'dark' ? 'light' : 'dark')
  const toggleLabel = theme === 'dark' ? 'Light mode' : 'Dark mode'

  return (
    <div className='app-shell'>
      <header className='app-header'>
        <div>
          <p className='eyebrow'>Todo Studio</p>
          <h1>Project Planner</h1>
        </div>
        <button className='theme-toggle' onClick={toggleTheme} aria-label={`Switch to ${toggleLabel}`}>
          <span className='toggle-dot' aria-hidden='true' />
          {toggleLabel}
        </button>
      </header>

      <section className='panel'>
        <p className='panel-meta'>A clean space to track the tasks that matter.</p>
        <Form
          todo={todo}
          setTodo={setTodo}
          editId={editId}
          handleSubmit={handleSubmit}
        />
        <TaskList
          tasks={tasks}
          setTodo={setTodo}
          setEditId={setEditId}
          handleDelete={handleDelete}
        />
      </section>
    </div>
  )
}

export default App