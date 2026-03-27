
import { useEffect, useState } from 'react'
import { getNote, sendNote, updateNote, deleteNote } from './Api'

function App() {
  const [notes, setNotes] = useState([])
  const [title, setTitle] = useState('')
  const [content, setContent] = useState('')
  const [editId, setEditId] = useState(null)
  const [darkMode, setDarkMode] = useState(true)

  const loadNotes = async () => {
    const data = await getNote()
    setNotes(data)
  }

  useEffect(() => {
    loadNotes()
  }, [])

  const handleSubmit = async (e) => {
    e.preventDefault()
    if (editId) {
      await updateNote(editId, { title, content })
      setEditId(null)
    } else {
      await sendNote(title, content)
    }

    setTitle('')
    setContent('')
    loadNotes()
  }

  const handleDelete = async (id) => {
    await deleteNote(id)
    loadNotes()
  }

  return (
    <div className={darkMode ? 'app dark' : 'app'}>
      <div className="container">
        <header>
          <h1>Notes</h1>
          <button onClick={() => setDarkMode(!darkMode)}>
            {darkMode ? 'Light' : 'Dark'}
          </button>
        </header>

        <form onSubmit={handleSubmit} className="form">
          <input
            type="text"
            placeholder="Title"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
          />

          <textarea
            placeholder="Write your note..."
            value={content}
            onChange={(e) => setContent(e.target.value)}
          />

          <button className="primary">
            {editId ? 'Update Note' : 'Add Note'}
          </button>
        </form>

        <div className="notes">
          {notes.map((note) => (
            <div key={note.id} className="card">
              <h2>{note.title}</h2>
              <p>{note.content}</p>

              <div className="actions">
                <button
                  onClick={() => {
                    setTitle(note.title)
                    setContent(note.content)
                    setEditId(note.id)
                  }}
                >
                  Edit
                </button>

                <button onClick={() => handleDelete(note.id)}>
                  Delete
                </button> 

                <p>{note.date}</p>
              </div>
            </div>
          ))}
        </div>
      </div>

   
    </div>
  )
}

export default App;