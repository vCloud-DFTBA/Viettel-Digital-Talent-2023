import axiosInstance from "./axiosInstance";

export const getAllAttendees = async () => {
    const response = await axiosInstance.get(`attendees`);
    return response.data;
}

export const getAttendeeById = async (id) => {
    const response = await axiosInstance.get(`attendees/${id}`);
    return response.data;
}

export const deleteAttendee = async (id) => {
    const response = await axiosInstance.delete(`delete/${id}`);
    return response.data;
}

export const addAttendee = async (newAttendee) => {
    const response = await axiosInstance.post(`add`, newAttendee);
    return response.data;
}

export const updateAttendee = async (id, updatedAttendee) => {
    const response = await axiosInstance.put(`update/${id}`, updatedAttendee);
    return response.data;
}