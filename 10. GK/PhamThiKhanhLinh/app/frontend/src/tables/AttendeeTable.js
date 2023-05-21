import React from "react";
import "./AttendeeTable.css";

const AttendeeTable = (props) => {
  return (
    <table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Username</th>
          <th>Sex</th>
          <th>Year Of Birth</th>
          <th>University</th>
          <th>Major</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        {props.attendees.length > 0 ? (
          props.attendees.map((attendee) => (
            <tr key={attendee.username}>
              <td>{attendee.name}</td>
              <td>{attendee.username}</td>
              <td>{attendee.sex}</td>
              <td>{attendee.yearOfBirth}</td>
              <td>{attendee.university}</td>
              <td>{attendee.major}</td>
              <td>
                <div className="button-group">
                  <button
                    className="button-edit"
                    onClick={() => {
                      props.editRow(attendee, false);
                    }}
                  >
                    Edit
                  </button>
                  <button
                    className="button-delete"
                    onClick={() => {
                      props.editRow(attendee, true);
                    }}
                  >
                    Delete
                  </button>
                </div>
              </td>
            </tr>
          ))
        ) : (
          <tr>
            <td colSpan={3}>No users</td>
          </tr>
        )}
      </tbody>
    </table>
  );
};

export default AttendeeTable;
