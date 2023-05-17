import {
  Button,
  Stack,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  TextField,
} from "@mui/material";
import { DesktopDatePicker } from "@mui/x-date-pickers";
import { AdapterMoment } from "@mui/x-date-pickers/AdapterMoment";
import { LocalizationProvider } from "@mui/x-date-pickers/LocalizationProvider";
import moment from "moment";
import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import cloudService from "../../services/cloud";

function newEmptyFormData() {
  return {
    full_name: "",
    username: "",
    birth_year: moment().year(),
    gender: "",
    university: "",
    major: "",
  };
}

export default function App() {
  const [interns, setInterns] = useState([]);
  const [formData, setFormData] = useState(newEmptyFormData);
  const [error, setError] = useState(null);

  useEffect(() => {
    const request = async () => {
      try {
        const returnedInterns = await cloudService.getAll();
        console.log("Returned interns: ", returnedInterns);
        setInterns(returnedInterns);
      } catch (err) {
        alert("Failed to get intern list!");
        console.log(err);
      }
    };

    request();
  }, []);

  const handleFormChange = (...args) => {
    let fieldName = null;
    let fieldValue = null;
    if (args.length === 1) {
      const e = args[0];
      fieldName = e.target.name;
      fieldValue = e.target.value;
    } else if (args.length > 1) {
      [fieldName, fieldValue] = args;
    }

    const newIntern = { ...formData };
    newIntern[fieldName] = fieldValue;
    setFormData(newIntern);
  };

  const handleFormSubmit = async (e) => {
    e.preventDefault();
    if (error) {
      alert("Found invalid input!");
      return;
    }

    try {
      const returnedIntern = await cloudService.create(formData);
      console.log("Returned intern after creating: ", returnedIntern);
      const newInterns = interns.concat(returnedIntern);
      setInterns(newInterns);
      setFormData(newEmptyFormData());
      alert("Created intern successfully!");
    } catch (err) {
      alert("Failed to create intern!");
      console.log(err);
    }
  };

  const handleClickDelete = async (internId) => {
    try {
      const returnedIntern = await cloudService.remove(internId);
      const newInterns = interns.filter(
        (intern) => intern.id !== returnedIntern.id
      );
      setInterns(newInterns);
      alert("Deleted intern successfully!");
    } catch (err) {
      alert("Failed to delete intern!");
      console.log(err);
    }
  };

  console.log("Form data: ", formData);
  return (
    <LocalizationProvider dateAdapter={AdapterMoment}>
      <Stack sx={{ p: 4 }} spacing={1}>
        <Stack
          component="form"
          gap={2}
          onSubmit={handleFormSubmit}
          style={{ border: "1px solid black", padding: "1rem" }}
        >
          <Stack direction="row" spacing={2}>
            <TextField
              required
              name="full_name"
              label="Full Name"
              value={formData.full_name}
              onChange={(e) => handleFormChange(e)}
            />
            <TextField
              required
              name="username"
              label="Username"
              value={formData.username}
              onChange={(e) => handleFormChange(e)}
            />
            <DesktopDatePicker
              required
              name="birth_year"
              label="Birth Year"
              openTo="year"
              views={["year"]}
              format="YYYY"
              disableFuture
              value={moment().year(formData.birth_year)}
              onChange={(v) => {
                handleFormChange("birth_year", v ? v.year() : 0);
              }}
              onError={(newError) => setError(newError)}
              slotProps={{ textField: {} }}
            />
            <TextField
              required
              name="gender"
              label="Gender"
              value={formData.gender}
              onChange={(e) => handleFormChange(e)}
            />
            <TextField
              required
              name="university"
              label="University"
              value={formData.university}
              onChange={(e) => handleFormChange(e)}
            />
            <TextField
              required
              name="major"
              label="Major"
              value={formData.major}
              onChange={(e) => handleFormChange(e)}
            />
          </Stack>
          <Stack direction="row" spacing={2}>
            <Button variant="contained" size="medium" type="submit">
              Create
            </Button>
          </Stack>
        </Stack>

        <TableContainer>
          <Table>
            <TableHead>
              <TableRow>
                <TableCell>ID</TableCell>
                <TableCell>Full Name</TableCell>
                <TableCell>Username</TableCell>
                <TableCell>Birth Year</TableCell>
                <TableCell>Gender</TableCell>
                <TableCell>University</TableCell>
                <TableCell>Major</TableCell>
                <TableCell></TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {interns.map((intern) => (
                <TableRow key={intern.id}>
                  <TableCell>{intern.id}</TableCell>
                  <TableCell>{intern.full_name}</TableCell>
                  <TableCell>{intern.username}</TableCell>
                  <TableCell>{intern.birth_year}</TableCell>
                  <TableCell>{intern.gender}</TableCell>
                  <TableCell>{intern.university}</TableCell>
                  <TableCell>{intern.major}</TableCell>
                  <TableCell>
                    <Stack direction="row" spacing={1}>
                      <Button
                        variant="contained"
                        size="small"
                        type="button"
                        component={Link}
                        to={`/interns/${intern.id}`}
                      >
                        View
                      </Button>
                      <Button
                        variant="contained"
                        size="small"
                        type="button"
                        onClick={() => handleClickDelete(intern.id)}
                      >
                        Delete
                      </Button>
                    </Stack>
                  </TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </TableContainer>
      </Stack>
    </LocalizationProvider>
  );
}
