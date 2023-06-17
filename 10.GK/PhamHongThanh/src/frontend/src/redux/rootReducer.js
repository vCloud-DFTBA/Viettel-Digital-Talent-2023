import { combineReducers } from "redux";
import attendeeReducer from "./reducer";

const rootReducer = combineReducers({
  data: attendeeReducer,
});

export default rootReducer;
