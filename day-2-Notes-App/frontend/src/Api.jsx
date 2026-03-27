import axios from "axios";

const endPoint = "http://localhost:5000/notes"

export const getNote = async () =>{
    const response = await axios.get(endPoint)
    return response.data
}

export const sendNote = async (title, content) =>{
    await axios.post(endPoint, {title, content})
}

export const updateNote = async (id, newNote) => {
    await axios.put(`${endPoint}/${id}`, newNote)
}

export const deleteNote = async (id) =>{
    await axios.delete(`${endPoint}/${id}`)
}