import { createCtx } from "./CreateCtx"
import React from "react"

interface AppContextType {
  openSnackbar: boolean,
  setOpenSnackbar: React.Dispatch<React.SetStateAction<boolean>>,
  snackbarMessage: string,
  setSnackbarMessage: React.Dispatch<React.SetStateAction<string>>,
  snackbarSeverity: "success" | "info" | "warning" | "error" | undefined,
  setSnackbarSeverity: React.Dispatch<React.SetStateAction<"success" | "info" | "warning" | "error" | undefined>>
}

export const [useAppContext, AppContextProvider] = createCtx<AppContextType>()

export default function AppContext({ children }: { children: React.ReactNode }) {
  const [openSnackbar, setOpenSnackbar] = React.useState<boolean>(false)
  const [snackbarMessage, setSnackbarMessage] = React.useState<string>('')
  const [snackbarSeverity, setSnackbarSeverity] = React.useState<"success" | "info" | "warning" | "error" | undefined>(undefined)

  return (
    <AppContextProvider value={{
      openSnackbar, setOpenSnackbar, snackbarMessage,
      setSnackbarMessage, snackbarSeverity, setSnackbarSeverity,
    }}>
        {children}
    </AppContextProvider>
  )
}