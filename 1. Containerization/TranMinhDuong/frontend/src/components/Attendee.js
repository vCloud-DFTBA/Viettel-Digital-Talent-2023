import { useEffect, useState } from "react";
import { Modal, Button } from 'react-bootstrap';
import EditForm from "./EditForm";
import { deleteAttendee } from "../apis/attendeeCRUD";
const Attendee = ({attendee, handleChange}) => {

    const [show, setShow] = useState(false);

    const handleShow = () => setShow(true);
    const handleClose = () => setShow(false);

    useEffect(() => {
        handleClose()
    }, [attendee])

    const delAttendee = () => {
        deleteAttendee(attendee.id)
            .then((res) => {
                console.log(res);
            })
            .catch((error) => {
                console.log(error)
            })
            handleChange();
    }

    return (
        <>
        <td>{attendee.name}</td>
        <td>{attendee.birthyear}</td>
        <td>{attendee.gender}</td>
        <td>{attendee.university}</td>
        <td>{attendee.major}</td>
        <td>
            <button onClick={handleShow} className="btn text-warning btn-act" data-toggle="modal"><i className="material-icons" data-toggle="tooltip" title="Edit">&#xE254;</i></button>
            <button onClick={delAttendee} className="btn text-danger btn-act" data-toggle="modal"><i className="material-icons" data-toggle="tooltip" title="Delete">&#xE872;</i></button>
        </td>

        <Modal show={show} onHide={handleClose}> 
            <Modal.Header closeButton>
                <Modal.Title>
                    Edit Attendee
                </Modal.Title>
            </Modal.Header>
            <Modal.Body>
                <EditForm attendee={attendee} handleChange={handleChange}/>
            </Modal.Body>
            <Modal.Footer>
                <Button variant="secondary" onClick={handleClose}>
                    Close Button
                </Button>
            </Modal.Footer>
        </Modal>
        </>
    )
}

export default Attendee;