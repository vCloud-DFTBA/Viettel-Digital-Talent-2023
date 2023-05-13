import axios from "axios";

export const isAxiosError = axios.isAxiosError;
const backend = window._env_.REACT_APP_BACKEND_URL || "http://localhost:5000"


const axiosInstance = axios.create({
  baseURL: backend,
  headers: {
    "Content-Type": "application/json",
  },
});

export default axiosInstance;