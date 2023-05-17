// Import React
import React from "react";
  
// Import Bootstrap
import { Nav, Navbar, Container, Row, Col } 
        from "react-bootstrap";
import "bootstrap/dist/css/bootstrap.css";
  
// Import Custom CSS
import "./App.css";
  
// Import from react-router-dom
import { BrowserRouter as Router, Routes,
    Route, Link } from "react-router-dom";
  
// Import other React Component
import CreateStudent from 
    "./Components/create-student.component";
import ViewStudent from 
    "./Components/view-student.component";
import EditStudent from 
    "./Components/edit-student.component";
import StudentList from 
    "./Components/student-list.component";
  
// App Component
const App = () => {
  return (
    <Router>
      <div className="App">
        <header className="App-header">
          <Navbar bg="dark" variant="dark">
            <Container>
              <Navbar.Brand>
                <Link to={"/create-student"} 
                  className="nav-link">
                  Vietel Digital Talent 2023
                </Link>
              </Navbar.Brand>
  
              <Nav className="justify-content-end">
                <Nav>
                  <Link to={"/create-student"} 
                    className="nav-link">
                    Create Attendee
                  </Link>
                </Nav>
  
                <Nav>
                  <Link to={"/student-list"} 
                    className="nav-link">
                    Attendee List
                  </Link>
                </Nav>
              </Nav>
            </Container>
          </Navbar>
        </header>
  
        <Container>
          <Row>
            <Col md={12}>
              <div className="wrapper">
                <Routes>
                  <Route path="/" 
                    element={<StudentList/>} />
                  <Route path="/create-student" 
                     element={<CreateStudent/>} />
                  <Route path="/view-student/:id" 
                     element={<ViewStudent/>} />
                  <Route path="/edit-student/:id" 
                     element={<EditStudent/>} />
                  <Route path="/student-list" 
                     element={<StudentList/>} />
                </Routes>
              </div>
            </Col>
          </Row>
        </Container>
      </div>
    </Router>
  );
};
  
export default App;