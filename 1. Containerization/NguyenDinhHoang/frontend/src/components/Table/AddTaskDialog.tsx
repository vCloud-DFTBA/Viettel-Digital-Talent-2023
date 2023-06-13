import * as React from "react";
import Button from "@mui/material/Button";
import TextField from "@mui/material/TextField";
import Dialog from "@mui/material/Dialog";
import DialogActions from "@mui/material/DialogActions";
import DialogContent from "@mui/material/DialogContent";
import DialogContentText from "@mui/material/DialogContentText";
import DialogTitle from "@mui/material/DialogTitle";
import Stack from "@mui/material/Stack";
import useMediaQuery from "@mui/material/useMediaQuery";
import { useTheme } from "@mui/material/styles";
import { useMyTask } from "src/contexts/MyTasksContext";
import { useAppContext } from "src/contexts/AppContext";
import InternService from "src/services/intern.service";

export default function AddTaskDialog() {
  const theme = useTheme();
  const { setRows, setAddInternOpen, addInternOpen } = useMyTask();
  const fullScreen = useMediaQuery(theme.breakpoints.down("md"));
  const { setOpenSnackbar, setSnackbarMessage, setSnackbarSeverity } =
    useAppContext();
  const [name, setName] = React.useState<string>("");
  const [yearOfBirth, setYearOfBirth] = React.useState<string>("");
  const [university, setUniversity] = React.useState<string>("");

  const handleClose = () => {
    setAddInternOpen(false);
  };

  const clearFields = () => {
    setName("");
    setYearOfBirth("");
    setUniversity("");
  };

  const handleAddTask = () => {
    if (!name || !yearOfBirth || !university) {
      setSnackbarMessage("Please fill all the fields");
      setSnackbarSeverity("error");
      setOpenSnackbar(true);
      return;
    }
    InternService.AddIntern({
      name: name,
      year_of_birth: yearOfBirth,
      university: university,
    })
      .then((res) => {
        InternService.GetIntern()
          .then((res) => {
            setRows(res);
            setSnackbarMessage("Intern added successfully");
            setSnackbarSeverity("success");
            setOpenSnackbar(true);
            setAddInternOpen(false);
            clearFields();
          })
          .catch((err) => {
            setSnackbarMessage("Something went wrong");
            setSnackbarSeverity("error");
            setOpenSnackbar(true);
          });
      })
      .catch((err) => {
        setSnackbarMessage("Something went wrong");
        setSnackbarSeverity("error");
        setOpenSnackbar(true);
      });
  };

  return (
    <div>
      <Dialog
        open={addInternOpen}
        onClose={handleClose}
        fullScreen={fullScreen}
      >
        <DialogTitle>Add Intern</DialogTitle>
        <DialogContent>
          <DialogContentText>Add new intern to the list</DialogContentText>
          <Stack
            direction="column"
            spacing={2}
            sx={{
              minWidth: "500px",
            }}
          >
            <TextField
              autoFocus
              margin="dense"
              id="name"
              required
              label="Full Name"
              type="text"
              fullWidth
              variant="outlined"
              value={name}
              onChange={(e) => setName(e.target.value)}
            />
            <TextField
              autoFocus
              margin="dense"
              id="yearOfBirth"
              required
              label="Year of Birth"
              type="text"
              fullWidth
              variant="outlined"
              value={yearOfBirth}
              onChange={(e) => setYearOfBirth(e.target.value)}
            />
            <TextField
              autoFocus
              margin="dense"
              id="university"
              required
              label="University"
              type="text"
              fullWidth
              variant="outlined"
              value={university}
              onChange={(e) => setUniversity(e.target.value)}
            />
          </Stack>
        </DialogContent>
        <DialogActions>
          <Button onClick={handleClose}>Cancel</Button>
          <Button onClick={handleAddTask}>Add Intern</Button>
        </DialogActions>
      </Dialog>
    </div>
  );
}
