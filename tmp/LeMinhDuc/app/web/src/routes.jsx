import { useRoutes } from "react-router-dom";
import Intern from "./pages/cloud/Intern";
import Interns from "./pages/cloud/Interns";

export default function Router() {
  const routes = useRoutes([
    {
      path: "/",
      element: <Interns />,
    },
    {
      path: "/interns",
      element: <Interns />,
    },
    {
      path: "/interns/:id",
      element: <Intern />,
    },
  ]);

  return routes;
}
