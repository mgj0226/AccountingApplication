import './App.css';
import axios from 'axios';
import React, { useState, useEffect } from 'react';

function App() {
  const [accounts, setAccounts] = useState([]);
  const [token, setToken] = useState(localStorage.getItem('token') || '');

  useEffect(() => {
    if (token) {
      axios.get('http://localhost:8000/api/accounts/', {
        headers: {
          'Authorization': `Token ${token}`
        }
      })
      .then(res => {
        setAccounts(res.data);
      })
      .catch(err => {
        console.log(err);
      });
    }
  }, [token]);

  const handleLogin = (username, password) => {
    axios.post('http://localhost:8000/api/auth/token/login/', { username, password })
      .then(res => {
        setToken(res.data.auth_token);
        localStorage.setItem('token', res.data.auth_token);
      })
      .catch(err => {
        console.log(err);
      });
  };

  return (
    <div className="App">
      <h1>Accounts</h1>
      <ul>
        {accounts.map(account => (
          <li key={account.id}>
            <h2>{account.name}</h2>
          </li>
        ))}
      </ul>
      <button onClick={() => handleLogin('username', 'password')}>Login</button>
    </div>
  );
}

export default App;