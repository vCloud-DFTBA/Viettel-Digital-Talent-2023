import axios from "axios"
// env

const backendUrl = process.env.REACT_APP_BACKEND_URL

const server = axios.create({
  baseURL: "hoangndst.freeddns.org:5000",
  headers: {
    "Content-Type": "application/json",
  }
})
export default server
