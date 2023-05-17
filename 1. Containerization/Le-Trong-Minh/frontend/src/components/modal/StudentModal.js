import React, { useState, useEffect } from "react";
import { Row, Col, Form, Input, Button, message, Spin } from "antd";
import "./style.css";
import { addStudent, getStudent, updateStudent } from "../../apis";

const STUDENT = {
    stt: "100",
    name: "LTM",
    username: "ltm",
    year_of_birth: "2000",
    gender: "male",
    university: "ITMO",
    major: "CS",
};

const StudentModal = (props) => {
    const { id, isOpen, isEdit, onCancel, onSuccess } = props;
    const [student, setStudent] = useState(STUDENT);
    const [loading, setLoading] = useState(false);

    const [form] = Form.useForm();

    useEffect(() => {
        if (id === "") {
            form.resetFields();
        } else {
            setLoading(true);
            getStudent(id)
                .then((result) => {
                    setStudent(result.data.data);
                })
                .catch((error) => {
                    message.error(JSON.stringify(error));
                })
                .finally(() => setLoading(false));
        }
    }, [id]);

    useEffect(() => {
        if (id === "") return;
        form.setFields([
            {
                name: "stt",
                value: student.stt,
            },
            {
                name: "name",
                value: student.name,
            },
            {
                name: "username",
                value: student.username,
            },
            {
                name: "year_of_birth",
                value: student.year_of_birth,
            },
            {
                name: "gender",
                value: student.gender,
            },
            {
                name: "university",
                value: student.university,
            },
            {
                name: "major",
                value: student.major,
            },
        ]);
    }, [student]);

    const handleSubmit = (newData) => {
        if (id === "") {
            setLoading(true);
            addStudent(newData)
                .then(() => {
                    message.success("Add student successfully!");
                    form.resetFields();
                    onSuccess();
                    onCancel();
                })
                .catch((err) => {
                    message.error(JSON.stringify(err.message));
                })
                .finally(() => setLoading(false));
        } else {
            setLoading(true);
            updateStudent(id, newData)
                .then(() => {
                    message.success("Update student successfully!");
                    form.resetFields();
                    onSuccess();
                    onCancel();
                })
                .catch((err) => {
                    message.error(JSON.stringify(err.message));
                })
                .finally(() => setLoading(false));
        }
    };

    return (
        <div className={`student-detail ${isOpen ? "show" : ""}`}>
            <div className='student-title'>
                {id === "" ? "Add student" : `Detail student ${student.name}`}
            </div>
            <div
                className='close-button'
                onClick={() => {
                    if (onCancel) onCancel();
                }}
            >
                X
            </div>
            <br></br>
            <Form
                form={form}
                onFinish={(newData) => {
                    handleSubmit(newData);
                }}
                labelAlign='left'
            >
                <Spin spinning={loading} size='large'>
                    <Row gutter={[24, 24]}>
                        <Col span={12}>
                            <Form.Item
                                name='stt'
                                label={"STT"}
                                wrapperCol={16}
                                labelCol={{ span: 8 }}
                                rules={[
                                    {
                                        required: true,
                                        message: "Please input STT",
                                    },
                                ]}
                            >
                                <Input
                                    disabled={!isEdit}
                                    placeholder={"Nhập số thứ tự"}
                                />
                            </Form.Item>
                        </Col>
                        <Col span={12}>
                            <Form.Item
                                name='name'
                                label={"Name"}
                                wrapperCol={16}
                                labelCol={{ span: 8 }}
                                rules={[
                                    {
                                        required: true,
                                        message: "Please input name",
                                    },
                                ]}
                            >
                                <Input
                                    disabled={!isEdit}
                                    placeholder={"Nhập họ tên"}
                                />
                            </Form.Item>
                        </Col>
                        <Col span={12}>
                            <Form.Item
                                name='username'
                                label={"username"}
                                wrapperCol={16}
                                labelCol={{ span: 8 }}
                                rules={[
                                    {
                                        required: true,
                                        message: "Please input username",
                                    },
                                ]}
                            >
                                <Input
                                    disabled={!isEdit}
                                    placeholder='Nhập tên người dùng'
                                />
                            </Form.Item>
                        </Col>
                        <Col span={12}>
                            <Form.Item
                                name='year_of_birth'
                                label={"Year of birth"}
                                wrapperCol={16}
                                labelCol={{ span: 8 }}
                                rules={[
                                    {
                                        required: true,
                                        message: "Please input year_of_birth",
                                    },
                                ]}
                            >
                                <Input
                                    disabled={!isEdit}
                                    placeholder='Nhập năm sinh'
                                />
                            </Form.Item>
                        </Col>
                        <Col span={12}>
                            <Form.Item
                                name='university'
                                label={"University"}
                                wrapperCol={16}
                                labelCol={{ span: 8 }}
                                rules={[
                                    {
                                        required: true,
                                        message: "Please input university",
                                    },
                                ]}
                            >
                                <Input
                                    disabled={!isEdit}
                                    placeholder='Nhập trường đại học'
                                />
                            </Form.Item>
                        </Col>
                        <Col span={12}>
                            <Form.Item
                                name='gender'
                                label={"Gender"}
                                wrapperCol={16}
                                labelCol={{ span: 8 }}
                                rules={[
                                    {
                                        required: true,
                                        message: "Please input gender",
                                    },
                                ]}
                            >
                                <Input
                                    disabled={!isEdit}
                                    placeholder='Nhập giới tính'
                                />
                            </Form.Item>
                        </Col>
                        <Col span={12}>
                            <Form.Item
                                name='major'
                                label={"Major"}
                                wrapperCol={16}
                                labelCol={{ span: 8 }}
                                rules={[
                                    {
                                        required: true,
                                        message: "Please input major",
                                    },
                                ]}
                            >
                                <Input
                                    disabled={!isEdit}
                                    placeholder='Nhập chuyên ngành'
                                />
                            </Form.Item>
                        </Col>
                    </Row>
                    {isEdit && (
                        <Form.Item wrapperCol={{ offset: 8, span: 16 }}>
                            <Button type='primary' htmlType='submit'>
                                Submit
                            </Button>
                        </Form.Item>
                    )}
                </Spin>
            </Form>
        </div>
    );
};

export default StudentModal;
