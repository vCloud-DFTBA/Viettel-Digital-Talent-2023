import axios from 'axios'
import {toast} from 'react-toastify'


const axiosClient = axios.create({
    baseURL: `${process.env.REACT_APP_API_URL || ''}/api/v1`,
});


axiosClient.interceptors.request.use(async (config) => {
    const {method, baseURL, url} = config
    console.log(`${new Date().toISOString()}  ${method.toUpperCase()}  ${baseURL + url}`);
    return config;
});

  

axiosClient.interceptors.response.use(
    ({data}) => {
        return data;
    },
    (error) => {
        const { data } = error.response || {};

        data?.message?.forEach(toast.error)
        !data && toast.error('Lỗi kết nối')

        throw error;
    }
);


export default axiosClient
