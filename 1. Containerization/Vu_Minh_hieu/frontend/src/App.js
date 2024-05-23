import React, { useState, useEffect } from "react";
import axios from "axios";

import logo from "./assets/viettel.png";
import "./App.css";

function App() {
    const [students, setStudents] = useState();

    useEffect(() => {
        axios.get("http://localhost:80").then((res) => {
            setStudents(res.data);
        });
    }, []);

    return (
        <div className='App'>
            <header className='header'>
                <div className='logo'>
                    <img src={logo} alt='Logo' />
                </div>
            </header>
            <div className='text-list'>
                List of intern Viettel Digital Talent 2023
            </div>
            <table className='table'>
                <thead>
                    <tr>
                        <th>STT</th>
                        <th>Name</th>
                        <th>Year Of Birth</th>
                        <th>Gender</th>
                        <th>University</th>
                        <th>Major</th>
                    </tr>
                </thead>
                <tbody>
                    {students?.map((student) => (
                        <tr key={student._id}>
                            <td>{student.stt}</td>
                            <td>{student.name}</td>
                            <td>{student.year_of_birth}</td>
                            <td>{student.gender}</td>
                            <td>{student.university}</td>
                            <td>{student.major}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
            <footer className='footer'>Copyright © hieuminhvuu 2023</footer>
        </div>
    );
}

export default App;
