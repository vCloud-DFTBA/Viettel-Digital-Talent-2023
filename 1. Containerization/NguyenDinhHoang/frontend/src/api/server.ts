import axios from "axios"
// env

const backendUrl = process.env.REACT_APP_BACKEND_URL || "http://localhost:5000"
console.log(backendUrl)
const server = axios.create({
  baseURL: backendUrl,
  headers: {
    "Content-Type": "application/json",
  }
})
export default server
