// CreateStudent Component for add new student

// Import Modules
import React, { useState, useEffect } from "react";
import axios from 'axios';
import StudentForm from "./StudentForm";

// CreateStudent Component
const CreateStudent = () => {
  const [formValues, setFormValues] =
    useState({ fullName: '', doB: '', gender: '', school: '', major: '' })
  // onSubmit handler
  const onSubmit = studentObject => {
    axios.post('/api/attendees',
      studentObject)
      .then(res => {
        if (res.status === 200)
          alert('Student successfully created')
        else
          Promise.reject()
      })
      .catch(err => alert('Something went wrong'))
  }

  // Return student form
  return (
    <StudentForm initialValues={formValues}
      onSubmit={onSubmit}
      enableReinitialize>
      Create Student
    </StudentForm>
  )
}

// Export CreateStudent Component
export default CreateStudent