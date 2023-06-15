import React, { useState, useEffect } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Table, Modal, Form, Button } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import axios from 'axios';
import './App.css'

function App() {
  const [users, setUsers] = useState([]);
  const [selectedUser, setSelectedUser] = useState(null);
  const [showModal, setShowModal] = useState(false);
  const [editedUser, setEditedUser] = useState(null);
  const [selectedUserId, setSelectedUserId] = useState(null);


  const backendURL = process.env.REACT_APP_BACKEND_URL || "http://172.18.0.3:30001";
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

  const handleRowClick = (user) => {
    setSelectedUserId(user.id);
    axios.get(`${backendURL}/user/${user.id}`)
      .then((res) => {
        setSelectedUser(res.data);
        setShowModal(true);
      })
      .catch((err) => console.log(err));
  };

  const handleCloseModal = () => {
    setShowModal(false);
  };



  const handleEdit = (user) => {
    setEditedUser({ ...user });
    setShowModal(true);
  };
  const handleSave = () => {
    axios.put(`${backendURL}/user/${editedUser.id}`, editedUser)
      .then(res => {
        // Cập nhật thông tin người dùng đã chỉnh sửa trong danh sách users
        setUsers(prevUsers =>
          prevUsers.map(user => (user.id === editedUser.id ? editedUser : user))
        );
        console.log(res.data);
        setShowModal(false);
      })
      .catch(err => console.log(err));
  };

  return (
    <div style={{ display: 'flex' }}>
      <div style={{ flex: 'auto' }}>
        <h1>List of Users</h1>
        <Table striped bordered hover>
          <thead>
            <tr>

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
              <tr key={user.id} onClick={() => handleRowClick(user)} >

                <td>{user.Name}</td>
                <td>{user.YearOfBirth}</td>
                <td>{user.Sex}</td>
                <td>{user.School}</td>
                <td>{user.Major}</td>
                <td>

                  <button onClick={() => handleDelete(user.id)} className="btn btn-danger">
                    Delete
                  </button>


                  <button onClick={() => handleEdit(user)} className="btn btn-warning">Edit</button>
                </td>
              </tr>
            ))}
          </tbody>
        </Table>
      </div>
      {selectedUserId && selectedUser && (
        <div >
          <Modal show={showModal} onHide={handleCloseModal} size='xl'>
            <Modal.Header closeButton>
              <Modal.Title>User Details</Modal.Title>
            </Modal.Header>
            <Modal.Body>
              <Table striped bordered hover>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th>Date of Birth</th>
                    <th>Sex</th>
                    <th>School</th>
                    <th>Major</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>{selectedUser.Name}</td>
                    <td>{selectedUser.YearOfBirth}</td>
                    <td>{selectedUser.Sex}</td>
                    <td>{selectedUser.School}</td>
                    <td>{selectedUser.Major}</td>
                  </tr>
                </tbody>
              </Table>
            </Modal.Body>
            <Modal.Footer>

            </Modal.Footer>
          </Modal>
        </div>)}

      {editedUser && (
        <div>
          <Modal show={showModal} onHide={handleCloseModal} size='xl'>
            <Modal.Header closeButton>
              <Modal.Title>Edit User</Modal.Title>
            </Modal.Header>
            <Modal.Body>
              <Form onSubmit={handleSave}>
                <Form.Group>
                  <Form.Label htmlFor="Name">Name</Form.Label>
                  <Form.Control
                    type="text"
                    id="Name"
                    name="Name"
                    value={editedUser.Name}
                    onChange={(e) =>
                      setEditedUser({ ...editedUser, Name: e.target.value })
                    }
                  />
                </Form.Group>
                <Form.Group>
                  <Form.Label htmlFor="YearOfBirth">Year Of Birth</Form.Label>
                  <Form.Control
                    type="text"
                    id="YearOfBirth"
                    name="YearOfBirth"
                    value={editedUser.YearOfBirth}
                    onChange={(e) => setEditedUser({ ...editedUser, YearOfBirth: e.target.value })}
                  />
                </Form.Group>
                <Form.Group>
                  <Form.Label htmlFor="Sex">Sex</Form.Label>
                  <Form.Control
                    type="text"
                    id="Sex"
                    name="Sex"
                    value={editedUser.Sex}
                    onChange={(e) => setEditedUser({ ...editedUser, Sex: e.target.value })}
                  />
                </Form.Group>
                <Form.Group>
                  <Form.Label htmlFor="School">School</Form.Label>
                  <Form.Control
                    type="text"
                    id="School"
                    name="School"
                    value={editedUser.School}
                    onChange={(e) => setEditedUser({ ...editedUser, School: e.target.value })}
                  />
                </Form.Group>
                <Form.Group>
                  <Form.Label htmlFor="Major">Major</Form.Label>
                  <Form.Control
                    type="text"
                    id="Major"
                    name="Major"
                    value={editedUser.Major}
                    onChange={(e) => setEditedUser({ ...editedUser, Major: e.target.value })}
                  />
                </Form.Group>
                <Button type="submit" variant="primary">
                  Save
                </Button>
              </Form>
            </Modal.Body>
            <Modal.Footer>
              <Button variant="secondary" onClick={handleCloseModal}>
                Cancel
              </Button>
            </Modal.Footer>
          </Modal>
        </div>
      )}
      <div style={{ margin: '0 40px' }}>
  <h2>Add a User</h2>
  <Form onSubmit={handleSubmit} className='form'>

    <Form.Group>
      <Form.Label className="form-label" htmlFor="Name">Name</Form.Label>
      <Form.Control className="form-control" type="text" id="Name" name="Name" />
    </Form.Group>
    <Form.Group>
      <Form.Label className="form-label" htmlFor="YearOfBirth">Year Of Birth</Form.Label>
      <Form.Control className="form-control" type="text" id="YearOfBirth" name="YearOfBirth" />
    </Form.Group>
    <Form.Group>
      <Form.Label className="form-label" htmlFor="Sex">Sex</Form.Label>
      <Form.Control className="form-control" type="text" id="Sex" name="Sex" />
    </Form.Group>
    <Form.Group>
      <Form.Label className="form-label" htmlFor="School">School</Form.Label>
      <Form.Control className="form-control" type="text" id="School" name="School" />
    </Form.Group>
    <Form.Group>
      <Form.Label className="form-label" htmlFor="Major">Major</Form.Label>
      <Form.Control className="form-control" type="text" id="Major" name="Major" />
    </Form.Group>
    <Button className="form-button" type="submit" variant="primary">Save</Button>
  </Form>
</div>
    </div>
  );
}

export default App;
