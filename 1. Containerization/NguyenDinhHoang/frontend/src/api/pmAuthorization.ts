import axios from "axios"
// env

const pmAuthorization = axios.create({
  baseURL: "https://pm.g6cloud.freeddns.org",
  headers: {
    "Content-Type": "application/json",
  }
})
export default pmAuthorization
