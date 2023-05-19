import axios from "axios";

const baseUrl = import.meta.env.VITE_APP_BASE_URL + "/cloud";
console.log("VITE_APP_BASE_URL", import.meta.env.VITE_APP_BASE_URL);

const getAll = async () => {
  const response = await axios.get(baseUrl);
  return response.data;
};

const getOne = async (id) => {
  const response = await axios.get(`${baseUrl}/${id}`);
  return response.data;
};

const create = async (newObject) => {
  const response = await axios.post(baseUrl, newObject);
  return response.data;
};

const remove = async (id) => {
  const response = await axios.delete(`${baseUrl}/${id}`);
  return response.data;
};

const update = async (id, newObject) => {
  const response = await axios.patch(`${baseUrl}/${id}`, newObject);
  return response.data;
};

export default {
  getAll,
  getOne,
  create,
  remove,
  update,
};
