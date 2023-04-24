import { Box } from "@mui/material"
import useMediaQuery from '@mui/material/useMediaQuery'
import { useTheme } from '@mui/material/styles'
import DataTable from "src/components/Table/Table"

export const MyTasks = () => {
  const theme = useTheme()
  const mobile = useMediaQuery(theme.breakpoints.down('lg'))
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
    </Box>
  )
}