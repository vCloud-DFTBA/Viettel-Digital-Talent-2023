import * as Yup from 'yup';
import { useFormik } from 'formik';
import { toast } from "react-toastify";
import { Button } from "react-bootstrap";
import { useCallback, useState } from "react";

import axiosClient from 'api/axiosClient';
import queryClient from 'api/queryClient';
import { attendeeKeys } from 'api/attendeeQuery';
import AppModal from 'components/AppModal';
import { Input } from "components/FormikField/Input";


function AttendeeRow(props) {
    return (
        <div className="row border-bottom py-1">
            <div className="col-3">{props.fullname}</div>
            <div className="col-2">{props.birthYear}</div>
            <div className="col-5">{props.university}</div>
            <div className="col-2 d-flex flex-row gap-2">
                <EditButton {...props}/>
                <DelButton attendeeId={props.attendeeId}/>
            </div>
        </div>
    )
}


export default AttendeeRow


// ----------------------------------------------------------


function EditButton({attendeeId, username, fullname, birthYear, university, major}) {
    const [show, setShow] = useState(false);
    const formik = useFormik({
        initialValues: {
            username,
            fullname,
            birthYear,
            university,
            major,
        },
        validationSchema: Yup.object({
            username: Yup.string().optional().matches(/^[A-Za-z0-9]+$/, 'username chỉ chứa chữ, chữ hoa và số'),
            fullname: Yup.string().optional().trim(),
            birthYear: Yup.number().optional().min(1900, 'Năm sinh không hợp lệ').max(2100, 'Năm sinh không hợp lệ'),
            university: Yup.string().optional().trim(),
            major: Yup.string().optional().trim(),
        }),
        async onSubmit(values) {
            await axiosClient.put(`/attendee/${attendeeId}`, values)
            await queryClient.invalidateQueries(attendeeKeys.list())
            toast.success('Sửa thông tin thành công')
        }
    })
    return (<>
        <Button className='px-2 py-0' variant="primary" onClick={() => setShow(true)}>
            Sửa
        </Button>

        {show && 
        <AppModal title="Sửa thông tin" show={true} setShow={setShow} formik={formik}>
            <div className='d-flex flex-column'>
                <Input id="username" name="username" placeholder="Username" formik={formik}/>
                <Input id="fullname" name="fullname" placeholder="Họ và tên" formik={formik}/>
                <Input id="birthYear" name="birthYear" type="number" placeholder="Năm sinh" formik={formik}/>
                <Input id="university" name="university" placeholder="Tên trường" formik={formik}/>
                <Input id="major" name="major" placeholder="Chuyên ngành" formik={formik}/>
            </div>
        </AppModal>}
    </>)
}


function DelButton({attendeeId}) {
    const [isSubmitting, setIsSubmitting] = useState(false);
    async function del() {
        setIsSubmitting(true)
        await axiosClient.delete(`/attendee`, {data: {attendeeIds: [attendeeId]}})
            .then(async () => {
                await queryClient.invalidateQueries(attendeeKeys.list())
                toast.success('Xóa thành công')
            })
            .catch(()=>{})
        setIsSubmitting(false)
    }
    return (
        <Button className='px-2 py-0' variant="danger" onClick={del} disabled={isSubmitting}>
            Xóa
        </Button>
    )
}
