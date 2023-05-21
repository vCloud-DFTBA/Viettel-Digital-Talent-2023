import renderer from 'react-test-renderer';
import userEvent from '@testing-library/user-event';
import { render, screen } from '@testing-library/react';

import AppModal from '.';
import * as Yup from 'yup';
import { useFormik } from 'formik';
import { Input } from "components/FormikField/Input";


test("It should render", async () => {
    expect(renderer.create(<AppModal/>).toJSON()).toMatchSnapshot()
})


test("It should submit form", async () => {
    const mockSubmit = jest.fn()

    // Wrap in function component to call useFormik hook
    function Wrapper() {
        const mockFormik = useFormik({
            initialValues: {
                username: '',
                fullname: '',
            },
            validationSchema: Yup.object({
                username: Yup.string().required('Bắt buộc').matches(/^[A-Za-z0-9]+$/, 'username chỉ chứa chữ, chữ hoa và số'),
                fullname: Yup.string().required('Bắt buộc').trim(),
            }),
            onSubmit: (values) => mockSubmit(values),
        })
        return (
            <AppModal show={true} formik={mockFormik}>
                <Input id="username" name="username" placeholder="username_test" formik={mockFormik}/>
                <Input id="fullname" name="fullname" placeholder="fullname_test" formik={mockFormik}/>
            </AppModal>
        )
    }

    render(<Wrapper/>)

    // Filling form
    await userEvent.type(screen.getByPlaceholderText('username_test'), username)
    await userEvent.type(screen.getByPlaceholderText('fullname_test'), fullname)

    // Submit form
    await userEvent.click(screen.getByRole('button', {name: "Thực hiện"}))

    expect(mockSubmit).toHaveBeenCalledWith({username, fullname})
})


// ---------------------------------------------------------


const username = 'anv'
const fullname = 'Nguyễn Văn A'
const birthDate = 2001
const university = 'BKHN'
const major = 'CNTT'
