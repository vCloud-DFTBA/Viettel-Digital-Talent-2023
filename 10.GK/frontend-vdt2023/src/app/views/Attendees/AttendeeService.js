import axios from 'axios';
import { API_ENPOINT } from '../../../Constraint';
const API_ATTENDEES = API_ENPOINT + "/attendees";

export const getAllAttendees = () => {
    let apiPath = API_ATTENDEES + "/all";
    console.log("Call api:" + apiPath);
    return axios.get(apiPath);
};

export const getById = (id) => {
    let apiPath = API_ATTENDEES + "/" + id;
    console.log("Call api:" + apiPath);
    return axios.get(apiPath);
};

export const update = (obj) => {
    let apiPath = API_ATTENDEES;
    console.log("Call api:" + apiPath);
    return axios.put(apiPath, obj);
};

export const create = (obj) => {
    let apiPath = API_ATTENDEES;
    console.log("Call api:" + apiPath);
    return axios.post(apiPath, obj);
};

export const deleteById = (id) => {
    let apiPath = API_ATTENDEES + "/" + id;
    console.log("Call api:" + apiPath);
    return axios.delete(apiPath);
};