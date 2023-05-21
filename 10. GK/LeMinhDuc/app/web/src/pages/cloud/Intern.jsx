import { Button, Stack, TextField } from "@mui/material";
import { DesktopDatePicker } from "@mui/x-date-pickers";
import { AdapterMoment } from "@mui/x-date-pickers/AdapterMoment";
import { LocalizationProvider } from "@mui/x-date-pickers/LocalizationProvider";
import moment from "moment";
import { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";
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
  const [intern, setIntern] = useState({});
  const [formData, setFormData] = useState(newEmptyFormData);
  const [readOnly, setReadOnly] = useState(true);
  const [error, setError] = useState(null);
  const { id } = useParams();

  useEffect(() => {
    const request = async () => {
      try {
        const returnedIntern = await cloudService.getOne(id);
        console.log("Returned intern: ", returnedIntern);
        setIntern(returnedIntern);
        setFormData(returnedIntern);
      } catch (err) {
        alert("Failed to get intern!");
        console.log(err);
      }
    };

    request();
  }, [id]);

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
      const returnedIntern = await cloudService.update(id, formData);
      console.log("Returned intern after updating: ", returnedIntern);
      setIntern(returnedIntern);
      setReadOnly(true);
      alert("Updated intern successfully!");
    } catch (err) {
      alert("Failed to update intern!");
      console.log(err);
    }
  };

  console.log("Form data: ", formData);
  return (
    <LocalizationProvider dateAdapter={AdapterMoment}>
      <Stack alignItems="center" spacing={1} sx={{ p: 4 }}>
        <Stack
          component="form"
          gap={2}
          onSubmit={handleFormSubmit}
          width="100%"
          maxWidth={500}
          style={{ border: "1px solid black", padding: "1rem" }}
        >
          <Stack spacing={2}>
            <TextField disabled name="id" label="ID" defaultValue={id} />
            <TextField
              required={!readOnly}
              InputProps={{
                readOnly: readOnly,
              }}
              name="full_name"
              label="Full Name"
              value={formData.full_name}
              onChange={(e) => handleFormChange(e)}
            />
            <TextField
              required={!readOnly}
              InputProps={{
                readOnly: readOnly,
              }}
              name="username"
              label="Username"
              value={formData.username}
              onChange={(e) => handleFormChange(e)}
            />
            <DesktopDatePicker
              readOnly={readOnly}
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
              required={!readOnly}
              InputProps={{
                readOnly: readOnly,
              }}
              name="gender"
              label="Gender"
              value={formData.gender}
              onChange={(e) => handleFormChange(e)}
            />
            <TextField
              required={!readOnly}
              InputProps={{
                readOnly: readOnly,
              }}
              name="university"
              label="University"
              value={formData.university}
              onChange={(e) => handleFormChange(e)}
            />
            <TextField
              required={!readOnly}
              InputProps={{
                readOnly: readOnly,
              }}
              name="major"
              label="Major"
              value={formData.major}
              onChange={(e) => handleFormChange(e)}
            />
          </Stack>
          <Stack direction="row" spacing={2}>
            {readOnly && (
              <>
                <Button
                  variant="contained"
                  type="button"
                  component={Link}
                  to="/"
                >
                  Home
                </Button>
                <Button
                  variant="contained"
                  type="button"
                  onClick={() => setReadOnly(false)}
                >
                  Edit
                </Button>
              </>
            )}
            {!readOnly && (
              <>
                <Button variant="contained" size="medium" type="submit">
                  Update
                </Button>
                <Button
                  variant="contained"
                  size="medium"
                  type="button"
                  onClick={() => {
                    setFormData(intern);
                    setReadOnly(true);
                  }}
                >
                  Cancel
                </Button>
              </>
            )}
          </Stack>
        </Stack>
      </Stack>
    </LocalizationProvider>
  );
}
