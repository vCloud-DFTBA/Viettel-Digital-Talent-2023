import React, { useState, useEffect } from "react";
import "./AttendeeForm.css";

const EditAttendeeForm = (props) => {
  const [attendee, setAttendee] = useState(props.currentAttendee);

  useEffect(() => {
    setAttendee(props.currentAttendee);
  }, [props]);
  // You can tell React to skip applying an effect if certain values haven’t changed between re-renders. [ props ]

  const handleInputChange = (event) => {
    const { name, value } = event.target;

    setAttendee({ ...attendee, [name]: value });
  };

  return (
    <form
      onSubmit={(event) => {
        event.preventDefault();
        props.updateAttendee(attendee.username, attendee);
      }}
    >
      <div>
        <label>Name</label>
        <input
          type="text"
          name="name"
          value={attendee.name}
          onChange={handleInputChange}
        />
      </div>
      <div>
        <label>Sex</label>
        <input
          type="text"
          name="sex"
          value={attendee.sex}
          onChange={handleInputChange}
        />
      </div>
      <div>
        <label>Year Of Birth</label>
        <input
          type="text"
          name="yearOfBirth"
          value={attendee.yearOfBirth}
          onChange={handleInputChange}
        />
      </div>
      <div>
        <label>University</label>
        <input
          type="text"
          name="university"
          value={attendee.university}
          onChange={handleInputChange}
        />
      </div>
      <div>
        <label>Major</label>
        <input
          type="text"
          name="major"
          value={attendee.major}
          onChange={handleInputChange}
        />
      </div>
      <div>
        <button>Update attendee</button>
        <button
          onClick={() => props.setEditing(false)}
          className="cancel-button"
        >
          Cancel
        </button>
      </div>
    </form>
  );
};

export default EditAttendeeForm;
