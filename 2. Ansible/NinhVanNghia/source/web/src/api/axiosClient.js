import axios from 'axios'


const axiosClient = axios.create({
    baseURL: process.env.REACT_APP_API_URL,
});


axiosClient.interceptors.response.use(
    (response) => {
        return response?.data;
    },
);


export default axiosClient
