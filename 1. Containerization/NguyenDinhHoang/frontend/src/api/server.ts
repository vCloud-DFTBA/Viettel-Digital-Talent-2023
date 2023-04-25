import axios from "axios"
// env

const backendUrl = 'http://127.0.0.1:5000'

const server = axios.create({
  baseURL: backendUrl,
  headers: {
    "Content-Type": "application/json",
  }
})
export default server
