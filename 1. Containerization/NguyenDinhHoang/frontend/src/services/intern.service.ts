import server from "src/api/server"

const GetIntern = async () => {
  const response = await server.get(`/interns/`)
  if (response.data) {
    localStorage.setItem("user", JSON.stringify(response.data))
  }
  return response.data
}

const InternService = {
  GetIntern,
}

export default InternService