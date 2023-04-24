import axios from "axios"

const pmServer = axios.create({
  baseURL: "https://pm.g6cloud.freeddns.org",
  headers: {
    "Content-Type": "application/json",
  }
})
export default pmServer
