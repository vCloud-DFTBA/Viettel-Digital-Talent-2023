// EditStudent Component for update student data
  
// Import Modules
import React, { useState, useEffect } from "react";
import axios from "axios";
import StudentForm from "./StudentForm";
import { useParams } from "react-router-dom";
// EditStudent Component
const EditStudent = (props) => {
  const [formValues, setFormValues] = useState(
    { fullName: '', doB: '', gender: '', school: '', major: '' }
  );
  const { id } =useParams();
  // console.log(id);
  //onSubmit handler
  const onSubmit = (studentObject) => {
    axios
      .put(
        "/api/attendees/" +
         id,
        studentObject
      )
      .then((res) => {
        if (res.status === 200) {
          alert("Student successfully updated");
           props.history.push("/");
        } else Promise.reject();
      })
      .catch((err) => alert("Student updated successfully"));
  };
  
  // Load data from server and reinitialize student form
  useEffect(() => {
    axios
      .get(
        "/api/attendees/getone/" 
        + id
      )
      .then((res) => {
        const { fullName, gender, doB, school, major} = res.data;
        setFormValues({fullName, gender, doB, school, major});
        // console.log(id);
      })
      .catch((err) => console.log(err));
  }, []);
  
  // Return student form
  return (
    <StudentForm
      initialValues={formValues}
      onSubmit={onSubmit}
      enableReinitialize
    >
      Update Student
    </StudentForm>
  );
};
  
// Export EditStudent Component
export default EditStudent;