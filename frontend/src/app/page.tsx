'use client'
import React, {useState, useEffect} from 'react'

export default function Home() {
  const [data, setData] = useState([])

  const fetchData = async() =>{
    const response = await fetch('https://8000-idx-django-project-1744361696364.cluster-73qgvk7hjjadkrjeyexca5ivva.cloudworkstations.dev/Website/GetTask/')
    if(!response.ok){
      console.log('HTTP Error')
    }else{
      const result = await response.json()
      console.log('Running : ', result)
    }
  }

  useEffect(()=> {
    fetchData()
  }, [])

  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <h1>Todo App</h1>
    </main>
  );
}
