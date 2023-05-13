import { createBrowserRouter } from "react-router-dom"
import { MyTasks } from "../pages/MyTasks"
import Main from "../pages/Main"
import Home from "../pages/Home"
import MyTaskContext from "src/contexts/MyTasksContext"
import AppContext from "src/contexts/AppContext"

const route = createBrowserRouter([
  {
    path: "/",
    element: <AppContext><Main /></AppContext>,
    children: [
      {
        path: "/",
        element: <Home />,
      },
      {
        path: "tasks",
        element: <MyTaskContext><MyTasks /></MyTaskContext>,
      }
    ]
  },

])

export default route
