import React from "react";
import { Button } from "react-bootstrap";
import { Link } from "react-router-dom";
import axios from "axios";
  
const StudentTableRow = (props) => {
  const { _ID, fullName, doB, gender, school, major } = props.obj;
  console.log(props.obj);
  const deleteStudent = () => {
    axios
      .delete("/api/attendees/" + _ID)
      .then((res) => {
        if (res.status === 200) {
          alert("Student successfully deleted");
          window.location.reload();
        } else Promise.reject();
      })
      .catch((err) => alert("Click again to confirm delete"));
  };
  
  return (
    <tr>
      <td>{fullName}</td>
      <td>{doB}</td>
      <td>{gender}</td>
      <td>{school}</td>
      <td>{major}</td>
      <td>
        <Link className="view-link" 
          to={"/view-student/" + _ID}>
          View
        </Link>
      </td>
      <td>
        <Link className="edit-link" 
          to={"/edit-student/" + _ID}>
          Edit
        </Link>
      </td>
      <td>
        <Button onClick={deleteStudent} 
          size="sm" variant="danger">
          Delete
        </Button>
      </td>
    </tr>
  );
};
  
export default StudentTableRow;