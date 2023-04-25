import { Box } from "@mui/material"
import useMediaQuery from '@mui/material/useMediaQuery'
import { useTheme } from '@mui/material/styles'
import DataTable from "src/components/Table/Table"
import AddTaskDialog from "src/components/Table/AddTaskDialog"
import DeleteDialog from "src/modules/components/DeleteDialog"
import EditTaskDialog from "src/components/Table/EditTaskDialog"
import { useMyTask } from "src/contexts/MyTasksContext"
import InternService from "src/services/intern.service"
import { useAppContext } from "src/contexts/AppContext"

export const MyTasks = () => {
  const theme = useTheme()
  const mobile = useMediaQuery(theme.breakpoints.down('lg'))
  const { setRows, openDeleteDialog, setOpenDeleteDialog, selected, setSelected } = useMyTask()
  const { setOpenSnackbar, setSnackbarMessage, setSnackbarSeverity } = useAppContext();

  const handleDelete = () => {
    InternService.DeleteIntern(selected)
      .then((res) => {
        InternService.GetIntern()
          .then((res) => {
            setRows(res)
            setSelected([])
            setSnackbarMessage("Intern deleted successfully")
            setSnackbarSeverity("success")
            setOpenSnackbar(true)
            setOpenDeleteDialog(false)
          })
          .catch((err) => {
            setSnackbarMessage("Something went wrong")
            setSnackbarSeverity("error")
            setOpenSnackbar(true)
          })
      })
      .catch((err) => {
        setSnackbarMessage("Something went wrong")
        setSnackbarSeverity("error")
        setOpenSnackbar(true)
      })
  }

  return (
    <Box
      sx={{
        position: "relative",
        display: "flex",
        minWidth: "0",
        boxBizing: "border-box",
        padding: "10px 0 0 5px",
        width: mobile ? "100%" : "calc(100vw - 300px)",
        height: 'calc(100vh - 150px)'
      }}
    >
      <DataTable />
      <AddTaskDialog />
      <EditTaskDialog />
      <DeleteDialog
        open={openDeleteDialog}
        setOpen={setOpenDeleteDialog}
        title="Delete Intern"
        contentText="Are you sure you want to delete?"
        handleAction={handleDelete}
      />        
    </Box>
  )
}