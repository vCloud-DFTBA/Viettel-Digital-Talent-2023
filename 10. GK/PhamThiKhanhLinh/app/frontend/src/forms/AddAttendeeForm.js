import React, { useState } from "react";
import "./AttendeeForm.css";

const AddAttendeeForm = (props) => {
  const initialFormState = {
    name: "",
    username: "",
    sex: "",
    yearOfBirth: 2002,
    university: "",
    major: "",
  };
  const [attendee, setAttendee] = useState(initialFormState);

  const handleInputChange = (event) => {
    const { name, value } = event.target;

    setAttendee({ ...attendee, [name]: value });
  };

  return (
    <form
      onSubmit={(event) => {
        event.preventDefault();
        if (!attendee.name || !attendee.username) return;

        props.addAttendee(attendee);
        setAttendee(initialFormState);
      }}
    >
      <div>
        <label>Name</label>
        <input
          type="text"
          name="name"
          required="yes"
          value={attendee.name}
          onChange={handleInputChange}
        />
      </div>
      <div>
        <label>Username</label>
        <input
          type="text"
          name="username"
          required="yes"
          value={attendee.username}
          onChange={handleInputChange}
        />
      </div>
      <div>
        <label>Sex</label>
        <input
          type="text"
          name="sex"
          required="yes"
          value={attendee.sex}
          onChange={handleInputChange}
        />
      </div>
      <div>
        <label>Year Of Birth</label>
        <input
          type="text"
          name="yearOfBirth"
          required="yes"
          value={attendee.yearOfBirth}
          onChange={handleInputChange}
        />
      </div>
      <div>
        <label>University</label>
        <input
          type="text"
          name="university"
          required="yes"
          value={attendee.university}
          onChange={handleInputChange}
        />
      </div>
      <div>
        <label>Major</label>
        <input
          type="text"
          name="major"
          required="yes"
          value={attendee.major}
          onChange={handleInputChange}
        />
      </div>
      <div>
        <button>Add new user</button>
      </div>
    </form>
  );
};

export default AddAttendeeForm;
