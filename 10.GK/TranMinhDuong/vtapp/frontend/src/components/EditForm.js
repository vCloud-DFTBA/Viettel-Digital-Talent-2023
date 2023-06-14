import { Form, Button } from 'react-bootstrap'
import { useState } from 'react';
import { updateAttendee } from '../apis/attendeeCRUD';

const EditForm = ({attendee, handleChange}) => {

    const id = attendee.id;
    const [name, setName] = useState(attendee.name);
    const [birthyear, setBirthyear] = useState(attendee.birthyear);
    const [gender, setGender] = useState(attendee.gender);
    const [university, setUniversity] = useState(attendee.university);
    const [major, setMajor] = useState(attendee.major);

    const updatedAttendee = {id, name, birthyear, gender, university, major};

    const handleSubmit = (e) => {
        e.preventDefault();
        updateAttendee(id, updatedAttendee)
            .then((res) => {
                console.log(res);
            })
            .catch((error) => {
                console.log(error)
            })
        handleChange();
    }

    return (
        <Form onSubmit={handleSubmit}>
            <Form.Group>
                <Form.Control
                    type="text"
                    placeholder="Name *"
                    name="name"
                    value={name}
                    onChange={(e) => setName(e.target.value)}
                    required
                >
                </Form.Control>
            </Form.Group>
            <Form.Group>
                <Form.Control
                    type="number"
                    placeholder="Birthyear *"
                    name="birthyear"
                    value={birthyear}
                    onChange={(e) => setBirthyear(e.target.value)}
                    required
                >
                </Form.Control>
            </Form.Group>
            <Form.Group>
                <Form.Select
                    name="gender"
                    value={gender}
                    onChange={(e) => setGender(e.target.value)}
                >
                    <option value="Nam">Nam</option>
                    <option value="Nữ">Nữ</option>
                </Form.Select>
            </Form.Group>
            <Form.Group>
                <Form.Control
                    type="text"
                    placeholder="University *"
                    name="university"
                    value={university}
                    onChange={(e) => setUniversity(e.target.value)}
                    required
                >
                </Form.Control>
            </Form.Group>
            <Form.Group>
                <Form.Control
                    type="text"
                    placeholder="Major *"
                    name="major"
                    value={major}
                    onChange={(e) => setMajor(e.target.value)}
                    required
                >
                </Form.Control>
            </Form.Group>

            <Button variant="success" type="submit">
                Edit Attendee
            </Button>
        </Form>
    )
}

export default EditForm;