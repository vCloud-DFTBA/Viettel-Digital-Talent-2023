import { Modal, Button } from 'react-bootstrap';
import { useState, useEffect } from "react";
import Attendee from "./Attendee";
import AddForm from "./AddForm";
import { getAllAttendees } from '../apis/attendeeCRUD';


const AttendeeList = () => {

    const [attendeeList, setAttendeeList] = useState([]);
    const [show, setShow] = useState(false);
    const [isChange, setIsChange] = useState(false);
    const handleShow = () => setShow(true);
    const handleClose = () => setShow(false);
    const handleChange = () => setIsChange(!isChange);
    useEffect(() => {
        getAllAttendees()
            .then((data) => {
                console.log(data);
                setAttendeeList(data);
            })
            .catch((error) => {
                console.log(error)
            })
        handleClose();
    }, [isChange])

    return (
        <>
        <div className="table-title">
            <div className="row">
                <div className="col-sm-6">
                    <h2>Manage <b>Attendees</b></h2>
                </div>
                <div className="col-sm-6">
                    <Button onClick={handleShow} className="btn btn-success" data-toggle="modal"><i className="material-icons">&#xE147;</i> <span>Add New Attendee</span></Button>					
                </div>
            </div>
        </div>
        <table className="table table-striped table-hover">
            <thead>
                <tr>
                    <th>Name</th>
                    <th>BirthYear</th>
                    <th>Gender</th>
                    <th>University</th>
                    <th>Major</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody>
                
                { attendeeList &&
                    attendeeList.map(attendee => (
                        <tr key={attendee.id}>
                            <Attendee attendee={attendee} handleChange={handleChange}/>
                        </tr>
                    ))
                }
                
            </tbody>
        </table>

        <Modal show={show} onHide={handleClose}> 
            <Modal.Header closeButton>
                <Modal.Title>
                    Add Attendee
                </Modal.Title>
            </Modal.Header>
            <Modal.Body>
                <AddForm handleChange={handleChange}/>
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

export default AttendeeList;