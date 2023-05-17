// EditStudent Component for update student data
  
// Import Modules
import React, { useState, useEffect } from "react";
import axios from "axios";
import { useParams } from "react-router-dom";
// EditStudent Component
const ViewStudent = (props) => {
  const [formValues, setFormValues] = useState(
    { fullName: '', doB: '', gender: '', school: '', major: '' }
  );
  const { id } =useParams();
  // console.log(id);
  //onSubmit handler
  
  
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
    <div style={{ 
      display: 'flex', 
      flexDirection: 'column', 
      alignItems: 'center' 
    }}>
    <h2 style={{ 
        textAlign: 'center', 
        marginBottom: '1rem' 
      }}>Attendee Detail</h2>
    <div style={{ 
        backgroundColor: '#f5f5f5', 
        padding: '1rem', 
        borderRadius: '0.5rem', 
        boxShadow: '0 0 10px rgba(0, 0, 0, 0.2)' 
      }}>
      <p><strong>Full Name:</strong> {formValues.fullName}</p>
      <p><strong>Date of Birth:</strong> {formValues.doB}</p>
      <p><strong>Gender:</strong> {formValues.gender}</p>
      <p><strong>School:</strong> {formValues.school}</p>
      <p><strong>Major:</strong> {formValues.major}</p>
    </div>
  </div>
  );
};
  
// Export EditStudent Component
export default ViewStudent;