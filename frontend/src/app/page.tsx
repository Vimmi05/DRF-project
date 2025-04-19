'use client'
import React, { useState, useEffect} from 'react';

export default function Home(){
  const [data, setData] = useState([]);
  const [task, setTask] = useState([]);
  const [editId, setEditId] = useState(null);

    const fetchData = async () => {
      const response = await fetch('http://127.0.0.1:8000/Website/GetTask/');

      if(!response.ok){
        console.log("HTTP Error...")
      }else{
        const result = await response.json()
        console.log("Running...", result)
        setData(result.data);
      }
    }

  useEffect(() => {
    fetchData()
  }, [])

  console.log("Value : ", task)

  const CreateOrUpdateRecord = async (e) => {
    e.preventDefault()
    const data = {
    task : task
     }
    try {
    let url = 'http://127.0.0.1:8000/Website/CreateTask/';
    let method = "POST";
    
    if(editId){
    url = `http://127.0.0.1:8000/Website/UpdateTask/${editId}/`;
    method = "PUT";
    }
    const response = await fetch(url, {
    method: method,
    headers: {
       'Content-Type':"application/json",
    },
    body: JSON.stringify(data)
    })
    if(response.ok){
    const result = await response.json(); // Parse JSON on success
    console.log("Task Created/Updated successfully:", result);
    setTask("");
    setEditId(null); // Reset editId after successful update
    fetchData(); // Refresh the task list
    }
    else {
    // Handle error responses
    const errorResult = await response.json(); // Try to parse JSON error
    console.error("Failed to create/update task:", response.status, errorResult);
    // Optionally, display an error message to the user
     }
    } catch(error){
    console.error("Error during request:", error);
    }
    }

  const handleEdit = (record) => {
    setTask(record.task);
    setEditId(record.id)
  }

  const DeleteTask = async (id) => {
    const response = await fetch(`http://127.0.0.1:8000/Website/DeleteTask/${id}/`,{
    method: "DELETE",
    })
     if(response.ok){
    console.log("DELETED....")
    fetchData();
    }else{
    console.log("Deletion Failed...")
    }
    }
  
  return (
    <main>
            <h1 className="text-4xl font-extrabold tracking-wide text-center pt-5 mb-3"> Todo App </h1>
            <form onSubmit={CreateOrUpdateRecord} style={{display: "flex", justifyContent: "space-evenly", width: "80%", margin: "auto auto"}}>
              <input type="text" value={task} onChange={(e) => setTask(e.target.value)} placeholder='Enter Task' className='rounded border px-16 p-2' style={{ width: "80%" }}/>
              <button type="submit" >{editId ? "Update Task" : "Create Task" }</button>
            </form>
            <h2 className="text-2xl font-extrabold tracking-wide text-center pt-5 mt-5 mb-3">All Tasks</h2>
            <table className="border-collapse border mt-5 border-gray-400" style={{ width: "80%", margin: "auto auto"}}>
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
                            <td className="border border-gray-300 px-3 p-2">{index + 1}</td>
                            <td className="border border-gray-300 px-3 p-2">{record.task}</td>
                            <td className="border border-gray-300 px-3 p-2">{record.created_at}</td>
                            <td className="border border-gray-300 px-3 p-2">
                              <button onClick={() => handleEdit(record)}>Edit</button> |
                              <button onClick={() => DeleteTask(record.id)}> Delete</button>
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </main>
  );
}