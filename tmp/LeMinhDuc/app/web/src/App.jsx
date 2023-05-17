import { CssBaseline } from "@mui/material";
import { BrowserRouter } from "react-router-dom";
import "./App.css";
import Router from "./routes";

export default function App() {
  return (
    <BrowserRouter>
      <CssBaseline />
      <Router />
    </BrowserRouter>
  );
}
