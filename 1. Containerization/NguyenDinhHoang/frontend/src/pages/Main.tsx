import { AppLayout } from "../modules/components/AppLayout"
import { Outlet } from "react-router-dom"

const Main = () => {
  return (
    <AppLayout>
      <Outlet />
    </AppLayout>
  )
}
export default Main