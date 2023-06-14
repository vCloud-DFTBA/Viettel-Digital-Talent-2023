import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css'

function App() {
  const [users, setUsers] = useState([]);
  const backendURL = process.env.REACT_APP_BACKEND_URL || "http://127.0.0.1:5000";
  useEffect(() => {
    axios.get(`${backendURL}/users`)
      .then((res) => {
        const usersWithId = res.data.map((user) => ({ ...user }));
        setUsers(usersWithId);
      })
      .catch((err) => console.log(err));
  }, []);

  const handleDelete = (userId) => {
    axios.delete(`${backendURL}/user/${userId}`)
      .then(res => {
        setUsers(prevUsers => prevUsers.filter(user => user.id !== userId));
        console.log(res.data);
      })
      .catch((err) => console.log(err));
  };

  const handleSubmit = (event) => {
    event.preventDefault();

    const formData = new FormData(event.target);
    const user = {
      STT: formData.get('STT'),
      Name: formData.get('Name'),
      YearOfBirth: formData.get('YearOfBirth'),
      Sex: formData.get('Sex'),
      School: formData.get('School'),
      Major: formData.get('Major')
    };

    axios.post(`${backendURL}/user`, user)
      .then(res => {
        console.log(res.data);
      })
      .catch((err) => console.log(err));
  };

  return (
    <div style={{display:'flex'}}>
<div style={{flex: '1'}}>
      <h1>List of Users</h1>
      <table>
        <thead>
          <tr>
            <th>STT</th>
            <th>Name</th>
            <th>Date of Birth</th>
            <th>Sex</th>
            <th>School</th>
            <th>Major</th>
            <th>Action</th>
          </tr>
        </thead>
        <tbody>
          {users.map(user => (
            <tr key={user.id}>
              <td>{user.STT}</td>
              <td>{user.Name}</td>
              <td>{user.YearOfBirth}</td>
              <td>{user.Sex}</td>
              <td>{user.School}</td>
              <td>{user.Major}</td>
              <td><button onClick={() => handleDelete(user.id)}>Delete</button></td>
            </tr>
          ))}
        </tbody>
      </table>
      </div>
      <div style={{margin: '0 40px'}}>
        <h2>Add a User</h2>
        <form onSubmit={handleSubmit} className='form'>
          <div>
            <label htmlFor="STT">STT</label>
            <input type="text" id="STT" name="STT" />
          </div>
          <div>
            <label htmlFor="Name">Name</label>
            <input type="text" id="Name" name="Name" />
          </div>
          <div>
            <label htmlFor="YearOfBirth">Year Of Birth</label>
            <input type="text" id="YearOfBirth" name="YearOfBirth" />
          </div>
          <div>
            <label htmlFor="Sex">Sex</label>
            <input type="text" id="Sex" name="Sex" />
          </div>
          <div>
            <label htmlFor="School">School</label>
            <input type="text" id="School" name="School" />
          </div>
          <div>
            <label htmlFor="Major">Major</label>
            <input type="text" id="Major" name="Major" />
          </div>
          <button type="submit">Save</button>
        </form>
      </div>
    </div>
  );
}

export default App;
