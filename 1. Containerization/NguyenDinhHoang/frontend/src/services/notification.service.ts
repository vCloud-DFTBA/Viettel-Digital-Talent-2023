import AuthHeader from "./auth.header"
import pmServer from "src/api/pmServer"

const getNotificationsByUserId = async (id: string) => {
  const response = await pmServer.get(`/pm/get-notifications-by-userid?userId=${id}`, { headers: AuthHeader() })
  return response.data
}

const updateNotification = async (id: string) => {
  const response = await pmServer.put(`/pm/update-notification/${id}`, {}, { headers: AuthHeader() })
  return response.data
}

const updateNotificationByRoute = async (route: string, userId: string) => {
  const response = await pmServer.put(`/pm/update-notification-by-route`, { route: route, userId: userId }, { headers: AuthHeader() })
  return response.data
}

const NotificationService = {
  getNotificationsByUserId,
  updateNotification,
  updateNotificationByRoute
}
export default NotificationService

// GET http://localhost:5000/pm/get-notifications-by-userid?userId=3c4148glbqmga6i
// Content-Type: application/json
// Authorization: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjNjNDE0OGdsYnFtZ2E2aSIsImlhdCI6MTY3MTIwMjgyMCwiZXhwIjoxNjcxMjg5MjIwfQ.LiLmVKQsOo99Rda_kwFwsdQv6B-a_a1rx8sQ3C4RCaE

// ### 

// PUT http://localhost:5000/pm/update-notification/5
// Content-Type: application/json
// Authorization: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjNjNDE0OGdsYnFtZ2E2aSIsImlhdCI6MTY3MTIwMjgyMCwiZXhwIjoxNjcxMjg5MjIwfQ.LiLmVKQsOo99Rda_kwFwsdQv6B-a_a1rx8sQ3C4RCaE

