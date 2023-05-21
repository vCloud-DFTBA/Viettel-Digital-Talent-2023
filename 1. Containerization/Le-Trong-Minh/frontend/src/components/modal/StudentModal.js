import React, { useState, useEffect } from "react";
import { Form, Input, Button, message, Spin } from "antd";
import "./style.css";
import { addStudent, getStudent, updateStudent } from "../../apis";

const STUDENT = {
  stt: "100",
  name: "Minh Le",
  username: "minhlt",
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
        .then((result) => setStudent(result.data.data))
        .catch((error) => message.error(JSON.stringify(error)))
        .finally(() => setLoading(false));
    }
  }, [id]);

  useEffect(() => {
    if (id === "") return;
    form.setFields([
      { name: "stt", value: student.stt },
      { name: "name", value: student.name },
      { name: "username", value: student.username },
      { name: "year_of_birth", value: student.year_of_birth },
      { name: "gender", value: student.gender },
      { name: "university", value: student.university },
      { name: "major", value: student.major },
    ]);
  }, [student]);

  const handleSubmit = (newData) => {
    setLoading(true);
    const apiCall = id === "" ? addStudent(newData) : updateStudent(id, newData);

    apiCall
      .then(() => {
        message.success(id === "" ? "Add student successfully!" : "Update student successfully!");
        form.resetFields();
        onSuccess();
        onCancel();
      })
      .catch((err) => message.error(JSON.stringify(err.message)))
      .finally(() => setLoading(false));
  };

  return (
    <div className={`student-detail ${isOpen ? "show" : ""}`}>
      <div className="student-title">{id === "" ? "Add student" : `${student.name}`}</div>
      <div
        className="close-button"
        onClick={() => {
          if (onCancel) onCancel();
        }}
      >
        X
      </div>
      <br />
      <Form form={form} onFinish={handleSubmit} labelAlign="left">
        <Spin spinning={loading} size="large">
          <Form.Item
            name="stt"
            label="STT"
            wrapperCol={{ span: 16 }}
            labelCol={{ span: 8 }}
            rules={[{ required: true, message: "Please input STT" }]}
          >
            <Input disabled={!isEdit} placeholder="Input order" />
          </Form.Item>
          <Form.Item
            name="name"
            label="Name"
            wrapperCol={{ span: 16 }}
            labelCol={{ span: 8 }}
            rules={[{ required: true, message: "Please input name" }]}
          >
            <Input disabled={!isEdit} placeholder="Input full name" />
          </Form.Item>
          <Form.Item
            name="username"
            label="Username"
            wrapperCol={{ span: 16 }}
            labelCol={{ span: 8 }}
            rules={[{ required: true, message: "Please input username" }]}
          >
            <Input disabled={!isEdit} placeholder="Input username" />
          </Form.Item>
          <Form.Item
            name="year_of_birth"
            label="Year of birth"
            wrapperCol={{ span: 16 }}
            labelCol={{ span: 8 }}
            rules={[{ required: true, message: "Please input year_of_birth" }]}
          >
            <Input disabled={!isEdit} placeholder="Input year of birth" />
          </Form.Item>
          <Form.Item
            name="university"
            label="University"
            wrapperCol={{ span: 16 }}
            labelCol={{ span: 8 }}
            rules={[{ required: true, message: "Please input university" }]}
          >
            <Input disabled={!isEdit} placeholder="Input university" />
          </Form.Item>
          <Form.Item
            name="gender"
            label="Gender"
            wrapperCol={{ span: 16 }}
            labelCol={{ span: 8 }}
            rules={[{ required: true, message: " Input gender" }]}
          >
            <Input disabled={!isEdit} placeholder="Input gender" />
          </Form.Item>
          <Form.Item
            name="major"
            label="Major"
            wrapperCol={{ span: 16 }}
            labelCol={{ span: 8 }}
            rules={[{ required: true, message: "Input major" }]}
          >
            <Input disabled={!isEdit} placeholder="Input major" />
          </Form.Item>
          {isEdit && (
            <Form.Item wrapperCol={{ offset: 8, span: 16 }}>
              <Button type="primary" htmlType="Send">
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
