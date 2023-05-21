import * as Yup from 'yup';
import { useState } from "react";
import { useFormik } from 'formik';
import { toast } from "react-toastify";
import { Button } from "react-bootstrap";

import axiosClient from 'api/axiosClient';
import AppModal from 'components/AppModal';
import { Input } from "components/FormikField/Input";
import queryClient from 'api/queryClient';
import { attendeeKeys } from 'api/attendeeQuery';


function CreateButton({className}) {
    const [show, setShow] = useState(false);
    const formik = useFormik({
        initialValues: {
            username: '',
            fullname: '',
            birthYear: 2000,
            university: '',
            major: '',
        },
        validationSchema: Yup.object({
            username: Yup.string().required('Bắt buộc').matches(/^[A-Za-z0-9]+$/, 'username chỉ chứa chữ, chữ hoa và số'),
            fullname: Yup.string().required('Bắt buộc').trim(),
            birthYear: Yup.number().min(1900, 'Năm sinh không hợp lệ').max(2100, 'Năm sinh không hợp lệ'),
            university: Yup.string().optional().trim(),
            major: Yup.string().optional().trim(),
        }),
        async onSubmit(values) {
            await axiosClient.post(`/attendee`, values);
            await queryClient.invalidateQueries(attendeeKeys.list())
            toast.success('Thêm mới thành công')
        }
    })
    return (
        <>
            <Button className={`${className} font-weight-bold`} variant="primary"
                onClick={() => setShow(true)}
            >
                Thêm người tham dự
            </Button>
            <AppModal title="Thêm người tham dự" show={show} setShow={setShow} formik={formik}>
                <div className='d-flex flex-column'>
                    <Input id="username" name="username" placeholder="Username" formik={formik}/>
                    <Input id="fullname" name="fullname" placeholder="Họ và tên" formik={formik}/>
                    <Input id="birthYear" name="birthYear" type="number" placeholder="Năm sinh" formik={formik}/>
                    <Input id="university" name="university" placeholder="Tên trường" formik={formik}/>
                    <Input id="major" name="major" placeholder="Chuyên ngành" formik={formik}/>
                </div>
            </AppModal>
        </>
    )
}


export default CreateButton
