import * as types from "./actionTypes";
import axios from "axios";

const API = "api";

const getAttendees = (attendees) => ({
  type: types.GET_ATTENDEES,
  payload: attendees,
});

const getAttendee = (attendees) => ({
  type: types.GET_SINGLE_ATTENDEE,
  payload: attendees,
});

const attendeeAdded = (msg) => ({
  type: types.ADD_ATTENDEE,
  payload: msg,
});

const attendeeDelete = (msg) => ({
  type: types.DELETE_ATTENDEE,
  payload: msg,
});

const attendeeUpdate = (msg) => ({
  type: types.UPDATE_ATTENDEE,
  payload: msg,
});

export const loadAttendees = () => {
  return function (dispatch) {
    axios
      .get(`${API}/attendees`)
      .then((resp) => dispatch(getAttendees(resp.data)))
      .catch((err) => console.log(err));
  };
};

export const addAttendee = (attendee) => {
  return function (dispatch) {
    axios
      .post(`${API}/attendees`, attendee)
      .then((resp) => {
        dispatch(attendeeAdded(resp.data.msg));
        dispatch(loadAttendees());
      })
      .catch((err) => console.log(err));
  };
};

export const deleteAttendee = (id) => {
  return function (dispatch) {
    axios
      .delete(`${API}/attendees/${id}`)
      .then((resp) => {
        dispatch(attendeeDelete(resp.data.msg));
        dispatch(loadAttendees());
      })
      .catch((err) => console.log(err));
  };
};

export const loadSingleAttendee = (id) => {
  return function (dispatch) {
    axios
      .get(`${API}/attendees/${id}`)
      .then((resp) => {
        dispatch(getAttendee(resp.data));
      })
      .catch((err) => console.log(err));
  };
};

export const updateAttendee = (attendee, id) => {
  return function (dispatch) {
    axios
      .put(`${API}/attendees/${id}`, attendee)
      .then((resp) => {
        dispatch(attendeeUpdate(resp.data.msg));
        dispatch(loadAttendees());
      })
      .catch((err) => console.log(err));
  };
};
