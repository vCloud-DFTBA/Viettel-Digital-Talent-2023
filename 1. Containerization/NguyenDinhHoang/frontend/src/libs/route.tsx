import { createBrowserRouter } from "react-router-dom"
import { MyTasks } from "../pages/MyTasks"
import Main from "../pages/Main"
import Home from "../pages/Home"

const route = createBrowserRouter([
  {
    path: "/",
    element: <Main />,
    children: [
      {
        path: "/",
        element: <Home />,
      },
      {
        path: "tasks",
        element: <MyTasks />,
      }
    ]
  },

])

export default route
