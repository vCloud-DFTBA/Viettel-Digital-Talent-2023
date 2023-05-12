import { Form, Button } from 'react-bootstrap'
import { useState } from 'react';
import { addAttendee } from '../apis/attendeeCRUD';

const AddForm = ({handleChange}) => {

    const [newAttendee, setNewAttendee] = useState({
        id: "", name: "", birthyear: "", gender: "Nam", university: "", major: ""
    })

    const onInputChange = (e) => {
        setNewAttendee({...newAttendee,[e.target.name]: e.target.value})
    }

    const {id, name, birthyear, gender, university, major} = newAttendee;

    const handleSubmit = (e) => {
        e.preventDefault();
        addAttendee(newAttendee)
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
                    type="number"
                    placeholder="ID *"
                    name="id"
                    value={id}
                    onChange={(e) => onInputChange(e)}
                    required
                >
                </Form.Control>
            </Form.Group>
            <Form.Group>
                <Form.Control
                    type="text"
                    placeholder="Name *"
                    name="name"
                    value={name}
                    onChange={(e) => onInputChange(e)}
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
                    onChange={(e) => onInputChange(e)}
                    required
                >
                </Form.Control>
            </Form.Group>
            <Form.Group>
                <Form.Select

                    name="gender"
                    value={gender}
                    onChange={(e) => onInputChange(e)}
                    required
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
                    onChange={(e) => onInputChange(e)}
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
                    onChange={(e) => onInputChange(e)}
                    required
                >
                </Form.Control>
            </Form.Group>

            <Button variant="success" type="submit" block>
                Add New Attendee
            </Button>
        </Form>
    )
}

export default AddForm;