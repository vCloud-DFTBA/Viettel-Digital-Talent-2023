import axios from "axios";

axios.defaults.baseURL = "http://0.0.0.0:5000";

export function editAttendee(attendee) {
  axios.put(`/editAttendee=${attendee.username}`, {
    name: attendee.name,
    username: attendee.username,
    sex: attendee.sex,
    yearOfBirth: attendee.yearOfBirth,
    university: attendee.university,
    major: attendee.major,
  });
}

export function addAttendee(attendee) {
  axios.post(`/newAttendee=${attendee.username}`, {
    name: attendee.name,
    username: attendee.username,
    sex: attendee.sex,
    yearOfBirth: attendee.yearOfBirth,
    university: attendee.university,
    major: attendee.major,
  });
}

export function deleteAttendee(attendee) {
  axios.delete(`/deleteAttendee=${attendee.username}`);
}
