import server from "src/api/server"

const GetIntern = async () => {
  const response = await server.get(`/interns`)
  return response.data
}

const AddIntern = async (intern: any) => {
  console.log(intern)
  const response = await server.post(`/interns`, intern)
  return response.data
}

const DeleteIntern = async (ids: any) => {
  const response = await server.post(`/interns/delete_many`, { ids: ids })
  return response.data
}

const UpdateIntern = async (intern: any) => {
  const response = await server.put(`/interns/${intern.id}`, intern)
  return response.data
}

const GetIdentity = async () => {
  const response = await server.get(`/identity`)
  return response.data
}

const InternService = {
  GetIntern,
  AddIntern,
  DeleteIntern,
  UpdateIntern,
  GetIdentity
}

export default InternService