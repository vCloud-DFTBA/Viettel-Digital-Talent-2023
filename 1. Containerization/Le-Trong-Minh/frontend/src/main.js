// import React, { useState, useEffect } from "react";
// import axios from "axios";

// import logo from "./assets/viettel.png";
// import "./App.css";
// import StudentModal from "./components/modal/StudentModal";
// import { message } from "antd";
// import { UserAddOutlined } from "@ant-design/icons";

// function App() {
//     const [students, setStudents] = useState();
//     const [currentId, setCurrentId] = useState("");
//     const [isOpen, setIsOpen] = useState();
//     const [isEdit, setIsEdit] = useState(true);
//     const [reload, setReload] = useState(true);
//     const port = process.env.REACT_APP_PORT_API;
//     const url = `http://localhost:${port}/api/v1`;
//     console.log(process.env.REACT_APP_PORT_API);
//     useEffect(() => {
//         if (reload) {
//             axios
//                 .get(`${url}/students`)
//                 .then((res) => {
//                     setStudents(res.data.data);
//                 })
//                 .then(() => {
//                     setReload(false);
//                 });
//         }
//     }, [reload]);

//     const deleteStudent = (id, name) => {
//         axios
//             .delete(`${url}/students/${id}`)
//             .then(() => {
//                 message.success(`Da xoa hoc sinh ${name}`);
//                 setReload(true);
//             })
//             .catch((err) => {
//                 message.error(JSON.stringify(err));
//             });
//     };

//     return (
//         <div className={`App ${isOpen ? "mask" : ""}`}>
//             <header className='header'>
//                 <div className='logo'>
//                     <img src={logo} alt='Logo' />
//                 </div>
//             </header>
//             <div className='text-list'>
//                 Apprentices in Cloud Computing
//             </div>
//             <div className='table-container'>
//                 <table style={{ position: "relative" }}>
//                     <div
//                         style={{
//                             position: "absolute",
//                             top: "-5px",
//                             right: 0,
//                             transform: "translate(0,-100%)",
//                             display: "flex",
//                         }}
//                     >
//                         <UserAddOutlined
//                             style={{ fontSize: "2rem", color: "#2986cc" }}
//                             onClick={() => {
//                                 setCurrentId("");
//                                 setIsEdit(true);
//                                 setIsOpen(true);
//                             }}
//                         ></UserAddOutlined>
//                     </div>
//                     <thead>
//                         <tr>
//                             <th>STT</th>
//                             <th className='name'>Name</th>
//                             <th>Username</th>
//                             {/* <th>Year</th>
//                             <th>Gender</th>
//                             <th>University</th>
//                             <th>Major</th> */}
//                             <th>Action</th>
//                         </tr>
//                     </thead>
//                     <tbody>
//                         {students?.map((student) => (
//                             <tr
//                                 key={student.id}
//                                 onClick={() => {
//                                     setIsOpen(true);
//                                     setIsEdit(false);
//                                     setCurrentId(student.id);
//                                 }}
//                             >
//                                 <td>{student.stt}</td>
//                                 <td>{student.name}</td>
//                                 <td>{student.username}</td>
//                                 {/* <td>{student.year_of_birth}</td>
//                                 <td>{student.gender}</td>
//                                 <td>{student.university}</td>
//                                 <td>{student.major}</td> */}
//                                 <td className='button-row'>
//                                     <button
//                                         className='edit'
//                                         onClick={(e) => {
//                                             e.stopPropagation();
//                                             setIsOpen(true);
//                                             setCurrentId(student.id);
//                                             setIsEdit(true);
//                                         }}
//                                     >
//                                         Edit
//                                     </button>
//                                     <button
//                                         className='delete'
//                                         onClick={(e) => {
//                                             e.stopPropagation();
//                                             deleteStudent(
//                                                 student.id,
//                                                 student.name
//                                             );
//                                         }}
//                                     >
//                                         Delete
//                                     </button>
//                                 </td>
//                             </tr>
//                         ))}
//                     </tbody>
//                 </table>
//             </div>
//             <footer className='footer'>Copyright ©minhlt</footer>

//             <StudentModal
//                 id={currentId}
//                 isOpen={isOpen}
//                 isEdit={isEdit}
//                 onCancel={() => setIsOpen(false)}
//                 onSuccess={() => {
//                     setReload(true);
//                 }}
//             />
//         </div>
//     );
// }

// export default App;

import React, { useState, useEffect } from "react";
import axios from "axios";
import { message } from "antd";
import { UserAddOutlined } from "@ant-design/icons";
import logo from "./assets/viettel.png";
import "./main.css";
import StudentModal from "./components/modal/StudentModal";

const App = () => {
  const [students, setStudents] = useState([]);
  const [currentId, setCurrentId] = useState("");
  const [isOpen, setIsOpen] = useState(false);
  const [isEdit, setIsEdit] = useState(true);
  const [reload, setReload] = useState(true);
  const port = process.env.REACT_APP_PORT_API;
  const url = `http://localhost:${port}/api/v1`;

  useEffect(() => {
    if (reload) {
      axios
        .get(`${url}/students`)
        .then((res) => {
          setStudents(res.data.data);
        })
        .finally(() => {
          setReload(false);
        });
    }
  }, [reload]);

  const deleteStudent = (id, name) => {
    axios
      .delete(`${url}/students/${id}`)
      .then(() => {
        message.success(`Deleted ${name}`);
        setReload(true);
      })
      .catch((err) => {
        message.error(JSON.stringify(err));
      });
  };

  return (
    <div className={`App ${isOpen ? "mask" : ""}`} style={{ }}>
      <header className="header" style={{ position: "", color:'black',}}>
        <h1>VDT 2023</h1>
      </header>
      <div className="text-list" style={{ }}>Apprentices in Cloud Computing</div>
      <td className="button-row" style={{ fontSize: "2rem", position: "absolute", transform:"translate(300%, -50%)"}} >
                
                <button
                onClick={() => {
                    setCurrentId("");
                    setIsEdit(true);
                    setIsOpen(true);
                }}
                >
                Add student
                </button>
            </td>
      <div className="table-container">
        
        <table style={{ position: "relative" }}>
          <div
            style={{
              position: "absolute",
              top: "0px",
              right: 0,
              transform: "translate(0,-100%)",
              display: "flex",
            }}
          >

          </div>
          <thead className='thead-table'>
            <tr className='head-table'>
              <th style={{}}>STT</th>
              <th className="name" style={{}}>Name</th>
              <th style={{}}>Username</th>
              <th style={{}}>Edit information/Delete</th>
            </tr>
          </thead>
          <tbody>
            {students.map((student) => (
              <tr
                key={student.id}
                onClick={() => {
                  setIsOpen(true);
                  setIsEdit(false);
                  setCurrentId(student.id);
                }}
              >
                <td style={{}}>{student.stt}</td>
                <td style={{}}>{student.name}</td>
                <td style={{}}>{student.username}</td>
                <td className="button-row" style={{}}>
                  <button
                    className="edit"
                    onClick={(e) => {
                      e.stopPropagation();
                      setIsOpen(true);
                      setCurrentId(student.id);
                      setIsEdit(true);
                    }}
                  >
                    Edit
                  </button>
                  <button
                    className="delete"
                    onClick={(e) => {
                      e.stopPropagation();
                      deleteStudent(student.id, student.name);
                    }}
                  >
                    Delete
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
      {/* <footer className="footer">Copyright ©minhlt</footer> */}
      <div></div>
      <div></div>
      <div></div>
      <StudentModal
        id={currentId}
        isOpen={isOpen}
        isEdit={isEdit}
        onCancel={() => setIsOpen(false)}
        onSuccess={() => {
          setReload(true);
        }}
      />
    </div>
  );
};

export default App;
