import React, { useEffect, useState } from 'react'

const apiUrl = import.meta.env.VITE_API_URL || 'http://localhost:8000'

export default function App() {
  const [status, setStatus] = useState('loading...')

  useEffect(() => {
    fetch(`${apiUrl}/health`)
      .then(r => r.json())
      .then(d => setStatus(d.status || JSON.stringify(d)))
      .catch(() => setStatus('error'))
  }, [])

  return (
    <div style={{ fontFamily: 'sans-serif', padding: 24 }}>
      <h1>React + FastAPI</h1>
      <p>Backend health: {status}</p>
    </div>
  )
}

