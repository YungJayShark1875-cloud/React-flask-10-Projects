import { useState } from 'react'

import './App.css'

function App() {
 const [hello, setHello] = useState('Hello World!')
 const changeHello = () =>{
  setHello("To Those who had a dream")
 }
  return (
    <>
     <h1>{hello}</h1>
     <button onClick={changeHello}>Click</button>
          
    </>
  )
}

export default App
