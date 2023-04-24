import AuthHeader from "./auth.header"
import pmServer from "src/api/pmServer"


const GetConversationsById = async (id: string) => {
  const response = await pmServer.get(`/pm/get-conversations?userId=${id}`, { headers: AuthHeader() })
  return response.data
}

const GetMessagesByConversationId = async (id: string) => {
  const response = await pmServer.get(`/pm/get-messages?conversationId=${id}`, { headers: AuthHeader() })
  return response.data
}

const createConversation = async (conversationName: string, users: any[]) => {
  const response = await pmServer.post(`/pm/create-conversation`, { conversationName: conversationName, users: users }, { headers: AuthHeader() })
  return response.data
}

const InboxService = {
  GetConversationsById,
  GetMessagesByConversationId,
  createConversation
}
export default InboxService