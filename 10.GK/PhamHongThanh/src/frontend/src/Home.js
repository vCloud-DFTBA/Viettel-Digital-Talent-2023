import React, { useEffect, useState } from "react";
import {
  Navbar,
  Table,
  Container,
  Row,
  Col,
  Button,
  ButtonGroup,
  Form,
} from "react-bootstrap";
import { useDispatch, useSelector } from "react-redux";
import { toast } from "react-toastify";
import {
  addAttendee,
  deleteAttendee,
  loadSingleAttendee,
  loadAttendees,
  updateAttendee,
} from "./redux/actions";

const initialState = {
  id: "",
  name: "",
  birth: "",
  sex:"",
  university: "",
  major: "",
};

const Home = () => {
  const [state, setState] = useState(initialState);
  const [editMode, setEditMode] = useState(false);
  const [attendeeId, setAttendeeId] = useState(null);
  const dispatch = useDispatch();
  const { attendees, msg, attendee } = useSelector((state) => state.data);

  const { id, name, birth, sex, university, major } = state;

  useEffect(() => {
    dispatch(loadAttendees());
  }, []);

  useEffect(() => {
    if (msg) {
      toast.success(msg);
    }
  }, [msg]);

  useEffect(() => {
    if (attendee) {
      setState({ ...attendee });
    }
  }, [attendee]);

  const handleChange = (e) => {
    let { name, value } = e.target;
    setState({ ...state, [name]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!id || !name || !birth || !sex || !university || !major) {
      toast.error("Please fill all input field");
    } else {
      if (!editMode) {
        dispatch(addAttendee(state));
        setState({ id:"", name: "", birth: "", sex: "", university: "", major: "" });
      } else {
        dispatch(updateAttendee(state, attendeeId));
        setState({ id:"", name: "", birth: "", sex: "", university: "", major: "" });
        setEditMode(false);
        setAttendeeId(null);
      }
    }
  };

  const handleDelete = (id) => {
    if (window.confirm("Are you sure that you wanted to delete that Attendee ?")) {
      dispatch(deleteAttendee(id));
    }
  };

  const handleUpdate = (id) => {
    dispatch(loadSingleAttendee(id));
    setAttendeeId(id);
    setEditMode(true);
  };
  return (
    <>
      <Navbar bg="primary" variant="dark" className="justify-content-center">
        <Navbar.Brand>
          Viettel Digital Talent 2023 Information
        </Navbar.Brand>
      </Navbar>
      <Container style={{ marginTop: "70px" }}>
        <Row>
          <Col md={4}>
            <Form onSubmit={handleSubmit}>
              <Form.Group>
                <Form.Label>ID</Form.Label>
                <Form.Control
                  type="number"
                  placeholder="Id"
                  name="id"
                  value={id || ""}
                  onChange={handleChange}
                />
              </Form.Group>
              <Form.Group>
                <Form.Label>Name</Form.Label>
                <Form.Control
                  type="text"
                  placeholder="Name"
                  name="name"
                  value={name || ""}
                  onChange={handleChange}
                />
              </Form.Group>
              <Form.Group>
                <Form.Label>Birth</Form.Label>
                <Form.Control
                  type="text"
                  placeholder="Birth"
                  name="birth"
                  value={birth || ""}
                  onChange={handleChange}
                />
              </Form.Group>
              <Form.Group>
                <Form.Label>Sex</Form.Label>
                <Form.Control
                  type="sex"
                  placeholder="Sex"
                  name="sex"
                  value={sex || ""}
                  onChange={handleChange}
                />
              </Form.Group>
              <Form.Group>
                <Form.Label>University</Form.Label>
                <Form.Control
                  type="text"
                  placeholder="University"
                  name="university"
                  value={university || ""}
                  onChange={handleChange}
                />
              </Form.Group>
              <Form.Group>
                <Form.Label>Major</Form.Label>
                <Form.Control
                  type="text"
                  placeholder="Major"
                  name="major"
                  value={major || ""}
                  onChange={handleChange}
                />
              </Form.Group>
              <div className="d-grid gap-2 mt-2">
                <Button type="submit" variant="primary" size="lg">
                  {editMode ? "Update" : "Submit"}
                </Button>
              </div>
            </Form>
          </Col>
          <Col md={8}>
            <Table bordered hover>
              <thead>
                <tr>
                  <th>ID</th>
                  <th>Name</th>
                  <th>Birth</th>
                  <th>Sex</th>
                  <th>University</th>
                  <th>Major</th>
                </tr>
              </thead>
              {attendees &&
                attendees.map((item, index) => (
                  <tbody key={index}>
                    <tr>
                      <td>{item.id}</td>
                      <td>{item.name}</td>
                      <td>{item.birth}</td>
                      <td>{item.sex}</td>
                      <td>{item.university}</td>
                      <td>{item.major}</td>
                      <td>
                        <ButtonGroup>
                          <Button
                            style={{ marginRight: "5px" }}
                            variant="danger"
                            onClick={() => handleDelete(item.id)}
                          >
                            Delete
                          </Button>
                          <Button
                            variant="secondary"
                            onClick={() => handleUpdate(item.id)}
                          >
                            Update
                          </Button>
                        </ButtonGroup>
                      </td>
                    </tr>
                  </tbody>
                ))}
            </Table>
          </Col>
        </Row>
      </Container>
    </>
  );
};

export default Home;
