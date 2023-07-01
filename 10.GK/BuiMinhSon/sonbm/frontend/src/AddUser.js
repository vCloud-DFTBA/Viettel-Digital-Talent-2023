// import React, { useState, useEffect } from 'react';

// function AddUser({ backendURL, handleAddUser }) {
//     const [users, setUsers] = useState({
//         Name: '',
//         YearOfBirth: '',
//         School: ''
//     });
//     const backendURL = process.env.REACT_APP_BACKEND_URL || "http://127.0.0.1:5000"

//     const handleSubmit = (event) => {
//         event.preventDefault();
//         fetch(`${backendURL}/user`, {
//             method: 'POST',
//             headers: {
//                 'Content-Type': 'application/json'
//             },
//             body: JSON.stringify(user)
//         })
//         .then(res => res.json())
//         .then(data => {
//             setUsers({
//                 Name: '',
//                 YearOfBirth: '',
//                 School: ''
//             });
//             handleAddUser(data);
//         });
//     };

//     const handleInputChange = (event) => {
//         const { name, value } = event.target;
//         setUsers(prevState => ({
//             ...prevState,
//             [name]: value
//         }));
//     };

//     return (
//         <div>
//             <h2>Add a User</h2>
//             <form onSubmit={handleSubmit}>
//                 <div>
//                     <label htmlFor="Name">Họ tên:</label>
//                     <input type="text" id="Name" name="Name" value={users.Name} onChange={handleInputChange} />
//                 </div>
//                 <div>
//                     <label htmlFor="YearOfBirth">Năm sinh:</label>
//                     <input type="text" id="YearOfBirth" name="YearOfBirth" value={users.YearOfBirth} onChange={handleInputChange} />
//                 </div>
//                 <div>
//                     <label htmlFor="School">Trường:</label>
//                     <input type="text" id="School" name="School" value={users.School} onChange={handleInputChange} />
//                 </div>
//                 <button type="submit">Save</button>
//             </form>
//         </div>
//     );
// }

// export default AddUser;
