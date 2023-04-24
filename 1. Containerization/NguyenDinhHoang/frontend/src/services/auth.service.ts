import pmAuthorization from "../api/pmAuthorization"
import AuthHeader from "./auth.header"

const SignIn = async (username: string, password: string) => {
  const response = await pmAuthorization.post("/auth/signin", { username, password })
  if (response.data.accessToken) {
    localStorage.setItem("userAuth", JSON.stringify(response.data))
  }
  return response.data
}

const SignUp = async (username: string, email: string, password: string) => {
  const response = await pmAuthorization.post("/auth/signup", { username, email, password })
  return response.data
}

const SignOut = () => {
  localStorage.removeItem("userAuth")
  localStorage.removeItem("user")
}

const ChangePassword = async (id: string, currentPassword: string, newPassword: string) => {
  const response = await pmAuthorization.post("/auth/change-password", { id, currentPassword, newPassword }, { headers: AuthHeader() })
  return response.data
}

const AuthService = {
  SignIn,
  SignUp,
  SignOut,
  ChangePassword,
}

export default AuthService