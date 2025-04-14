'use client'
import { error } from 'console';
import React, { useState, useEffect } from 'react'

export default function Home() {
  const [data, setData] = useState([]);
  const [task, setTask] = useState("");
  const [editId, setEditId] = useState(null);

  const fetchData = async () => {
    const response = await fetch('https://8000-idx-django-project-1744361696364.cluster-73qgvk7hjjadkrjeyexca5ivva.cloudworkstations.dev/Website/GetTask/')
    if (!response.ok) {
      console.log('HTTP Error')
    } else {
      const result = await response.json()
      console.log('Running : ', result)
      setData(result.data); //data from backend
    }
  }

  useEffect(() => {
    fetchData()
  }, [])

  console.log("Value : ", task)
  const createOrUpdateRecord = async (e) => {
    e.preventDefault();
    const data = {
      task : task
    }
    try{
      let url = 'https://8000-idx-django-project-1744361696364.cluster-73qgvk7hjjadkrjeyexca5ivva.cloudworkstations.dev/Website/CreateTask/';
      let method = 'POST'

      if(editId){
        url = `https://8000-idx-django-project-1744361696364.cluster-73qgvk7hjjadkrjeyexca5ivva.cloudworkstations.dev/Website/UpdateTask/${editId}/`
        method = 'PUT'
      }
      const response = await fetch('url', {
        method: method,
        headers: {
          "Content-Type":"application/json",
        },
        body: JSON.stringify(data)
      })
      if (response.ok){
        const res = await response.json()
        console.log("Response : ", res)
        setTask('')
        fetchData();
      }else{
        console.log("Error : ")
      }

    }
    catch(error){
      console.log("Error : ", error)
    }
  }


  const handleEdit = (record) => {
    setTask(record.task);
    setEditId(record.id);
  }

  const DeleteTask = async(id) =>{
    const response = await fetch('https://8000-idx-django-project-1744361696364.cluster-73qgvk7hjjadkrjeyexca5ivva.cloudworkstations.dev/Website/DeleteTask/${editId}/', {
      method: "DELETE",
    })
    if (response.ok){
      console.log("DELETED ")
      fetchData()
    }else{
      console.log("Error")
    }
  } 

  return (
    <main className="">
      <h1 className="text-4xl font-extrabold tracking-wide text-center pt-5 mb-3"> Todo App </h1>
      
      <form onSubmit={createOrUpdateRecord} style={{display: "flex", justifyContent:"space-evenly", width:"80%", margin:"auto auto"}}>
        <input type="text" value={task} onChange={(e) => setTask(e.target.value)} placeholder="Enter Task" className='rounded border px-16 p-2'
        style={{width: "80%"}}/>
        <button type="submit">{editId ? "Update Task" : "Create Task"}</button>
      </form>
      <h2  className="text-2xl font-extrabold tracking-wide text-center pt-5 mb-3">All Tasks</h2>
      <table className="border-collapse border mt-5 border-gray-400 ..." style={{ width: "80%", margin: "auto auto"}}>
        <thead>
          <tr>
            <th className="border border-gray-300 text-xl p-3">Sr. No.</th>
            <th className="border border-gray-300 text-xl p-3">Task</th>
            <th className="border border-gray-300 text-xl p-3">Created At</th>
            <th className="border border-gray-300 text-xl p-3">Actions</th>
          </tr>
        </thead>
        <tbody>

        {data && data.map((record, index) => (
          <tr key={record}>
            <td className="border border-gray-300 px-3 p-2">{index+1}</td>
            <td className="border border-gray-300 px-3 p-2">{record.task}</td>
            <td className="border border-gray-300 px-3 p-2">{record.created_date}</td>
            <td className="border border-gray-300 px-3 p-2">
              <button onClick={()=> handleEdit(record)}>Edit</button>
              <button className='ml-5' onClick={()=> DeleteTask(record)}>Delete</button>
            </td>
          </tr>
      ))}
      </tbody>
      </table>
    </main>
  );
}
