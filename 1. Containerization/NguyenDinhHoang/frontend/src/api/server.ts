import axios from "axios"
// env

const backendUrl = process.env.BACKEND_URL

const server = axios.create({
  baseURL: backendUrl,
  headers: {
    "Content-Type": "application/json",
  }
})
export default server
