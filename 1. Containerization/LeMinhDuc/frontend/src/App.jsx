import { Box, CircularProgress } from "@mui/material";
import { DataGrid } from "@mui/x-data-grid";
import { useEffect, useState } from "react";
import "./App.css";
import cloudService from "./services/cloud";

const columns = [
  {
    field: "id",
    headerName: "STT",
    flex: 1,
  },
  {
    field: "full_name",
    headerName: "Họ và tên",
    flex: 2,
  },
  {
    field: "birth_year",
    headerName: "Năm sinh",
    flex: 1,
  },
  {
    field: "gender",
    headerName: "Giới tính",
    flex: 1,
  },
  {
    field: "university",
    headerName: "Trường",
    flex: 3,
  },
  {
    field: "major",
    headerName: "Chuyên ngành",
    flex: 3,
  },
];

function App() {
  const [cloudInterns, setCloudInterns] = useState([]);
  const [loading, setLoading] = useState(false);

  const tableStyle = {
    "& .MuiDataGrid-cell:focus-within": {
      outline: "none",
    },
    "& .MuiDataGrid-columnHeader:focus-within": {
      outline: "none",
    },
    "& .MuiDataGrid-virtualScroller": {
      overflow: "hidden",
    },
  };

  useEffect(() => {
    setLoading(true);
    const fetchData = async () => {
      try {
        const interns = await cloudService.getAll();
        setCloudInterns(interns);
      } catch (error) {
        console.log(error);
      }
      setLoading(false);
    };
    fetchData();
  }, []);

  return (
    <Box className="content">
      <h1>Viettel Digital Talent 2023</h1>
      <h2>Cloud Interns</h2>

      {loading ? (
        <CircularProgress />
      ) : (
        <Box sx={{ width: "100%" }}>
          <DataGrid
            autoHeight
            rows={cloudInterns}
            columns={columns}
            initialState={{
              pagination: { paginationModel: { pageSize: 10 } },
            }}
            pageSizeOptions={[10, 20, 50]}
            disableRowSelectionOnClick
            sx={tableStyle}
          />
        </Box>
      )}
    </Box>
  );
}

export default App;
