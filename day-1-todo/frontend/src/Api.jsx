import axios from 'axios'

const url = 'http://127.0.0.1:5000/tasks'

export const getData = async ()=>{
    const response = await axios.get(url);
    
    return response.data
}

export const sendData = async (task) =>{
  await axios.post(url, {task})
}

export const updateData = async (id, newData) => {
    await axios.put(`${url}/${id}`, newData)
}

export const deleteData = async (id) =>{
    await axios.delete(`${url}/${id}`)
}