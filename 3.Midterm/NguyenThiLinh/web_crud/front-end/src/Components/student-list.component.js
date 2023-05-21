import React, { useState, useEffect } from "react";
import axios from "axios";
import { Table } from "react-bootstrap";
import StudentTableRow from "./StudentTableRow";

const StudentList = () => {
  const [students, setStudents] = useState([]);
  
  useEffect(() => {
    axios
      .get("/api/attendees")
      .then(({ data }) => {
        setStudents(data);
      })
      .catch((error) => {
        console.log(error);
      });
  }, []);
  
  const DataTable = () => {
    students.sort((a, b) => a.fullName.localeCompare(b.fullName));
    return students.map((res, i) => {
      return <StudentTableRow obj={res} key={i} />;
    });
  };
  
  return (
    <div className="table-wrapper">
      <Table striped bordered hover>
        <thead>
          <tr>
            <th> Full Name </th>
            <th> Year of Birth  </th>
            <th> Gender </th>
            <th> School </th>
            <th> Major </th>
            <th> Detail </th>
            <th> Edit </th>
            <th> Delete </th>
          </tr>
        </thead>
        <tbody>{DataTable()}</tbody>
      </Table>
    </div>
  );
};
  
export default StudentList;