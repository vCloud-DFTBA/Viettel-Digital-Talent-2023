import * as types from "./actionTypes";

const initialState = {
  attendees: [],
  attendee: {},
  msg: "",
};

const attendeeReducer = (state = initialState, action) => {
  switch (action.type) {
    case types.GET_ATTENDEES:
      return {
        ...state,
        attendees: action.payload,
      };
    case types.ADD_ATTENDEE:
    case types.DELETE_ATTENDEE:
    case types.UPDATE_ATTENDEE:
      return {
        ...state,
        msg: action.payload,
      };
    case types.GET_SINGLE_ATTENDEE:
      return {
        ...state,
        attendee: action.payload,
      };
    default:
      return state;
  }
};

export default attendeeReducer;
