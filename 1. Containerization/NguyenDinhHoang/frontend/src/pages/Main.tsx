import { AppLayout } from "../modules/components/AppLayout"
import { Outlet } from "react-router-dom"
import { useAppContext } from 'src/contexts/AppContext'
import Snackbar from '@mui/material/Snackbar'
import Alert from '@mui/material/Alert'

const Main = () => {

  const { openSnackbar, setOpenSnackbar, snackbarSeverity, snackbarMessage } = useAppContext()

  return (
    <AppLayout>
      <Outlet />
      <Snackbar open={openSnackbar} autoHideDuration={3000} onClose={() => setOpenSnackbar(false)}>
        <Alert onClose={() => setOpenSnackbar(false)} severity={snackbarSeverity} sx={{ width: '100%' }}>
          {snackbarMessage}
        </Alert>
      </Snackbar>
    </AppLayout>
  )
}
export default Main