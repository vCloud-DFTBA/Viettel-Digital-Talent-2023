import React from "react";
import * as Yup from "yup";
import { Formik, Form, Field, ErrorMessage } from "formik";
import { FormGroup, FormControl, Button } from "react-bootstrap";
  
const StudentForm = (props) => {
  const validationSchema = Yup.object().shape({
    fullName: Yup.string().required("Required"),
    doB: Yup.string(),
    gender: Yup.string(),
    school: Yup.string(),
    major: Yup.string()
  });
  // console.log(props);
  return (
    <div className="form-wrapper">
      <Formik {...props} validationSchema={validationSchema}>
        <Form>
          <FormGroup>
            Full Name
            <Field name="fullName" type="text" 
                className="form-control" />
            <ErrorMessage
              name="fullName"
              className="d-block invalid-feedback"
              component="span"
            />
          </FormGroup>
          <br></br>
          <FormGroup>
            Year of Birth:
            <Field name="doB" type="text" 
                className="form-control" />
            <ErrorMessage
              name="doB"
              className="d-block invalid-feedback"
              component="span"
            />
          </FormGroup>
          <br></br>

          <FormGroup>
            Gender:
            <Field name="gender" type="text" 
                className="form-control" />
            <ErrorMessage
              name="gender"
              className="d-block invalid-feedback"
              component="span"
            />
          </FormGroup>
          <br></br>

          <FormGroup>
            School:
            <Field name="school" type="text" 
                className="form-control" />
            <ErrorMessage
              name="school"
              className="d-block invalid-feedback"
              component="span"
            />
          </FormGroup>
          <br></br>

          <FormGroup>
            Major:
            <Field name="major" type="text" 
                className="form-control" />
            <ErrorMessage
              name="major"
              className="d-block invalid-feedback"
              component="span"
            />
          </FormGroup>
          <br></br>

          <Button variant="danger" size="lg" 
            block="block" type="submit">
            {props.children}
          </Button>
        </Form>
      </Formik>
    </div>
  );
};
  
export default StudentForm;