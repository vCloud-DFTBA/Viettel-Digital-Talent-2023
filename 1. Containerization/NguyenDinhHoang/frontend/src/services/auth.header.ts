const AuthHeader = () => {
  const userAuth = JSON.parse(localStorage.getItem("userAuth") || "{}");
  if (userAuth && userAuth.accessToken) {
    return { Authorization: userAuth.accessToken };
  } else {
    return {};
  }
} 
export default AuthHeader