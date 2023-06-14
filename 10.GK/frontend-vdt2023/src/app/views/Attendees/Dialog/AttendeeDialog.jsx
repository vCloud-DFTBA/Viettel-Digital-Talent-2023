/* eslint-disable react-hooks/exhaustive-deps */
import React, { memo, useContext, useState, useEffect } from "react";
import styles from "./_attendee_dialog.module.scss";
import { ThemeContext } from "../AttendeesTable";
import { MdClose } from "react-icons/md";
import { getById, update, create } from "../AttendeeService";
import { toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";

function AttendeeDialog() {
  const providerValue = useContext(ThemeContext);
  const [id, setId] = useState("");
  const [name, setName] = useState("");
  const [username, setUsername] = useState("");
  const [yearOfBirth, setYearOfBirth] = useState("");
  const [sex, setSex] = useState("");
  const [school, setSchool] = useState("");
  const [major, setMajor] = useState("");

  useEffect(() => {
    let id = providerValue.id;
    console.log("Current id: " + id);

    if (id) {
        getById(id)
        .then((res) => {
          console.log(res);
          if (res?.data?.data) {
            console.log(res.data.data);
            let attendee = res.data.data;
            setId(attendee.id);
            setName(attendee.name);
            setUsername(attendee.username);
            setYearOfBirth(attendee.yearOfBirth);
            setSex(attendee.sex)
            setSchool(attendee.school);
            setMajor(attendee.major);
            return;
          }
          throw Error(res.status);
        })
        .catch(function (error) {
          toast.warning("Server error");
        });
    }
  }, []);

  const handleClose = () => {
    providerValue.setIsOpenFormInput(false);
  };

  const handleSubmit = () => {
    if (validateProfile()) {
      const obj = {
        id: id,
        name: name,
        username: username,
        yearOfBirth: yearOfBirth,
        sex: sex,
        school: school,
        major: major,
      };
      if (!id) {
        create(obj)
          .then((res) => {
            console.log(res);
            if (res?.data?.data) {
              toast.success("Create success");
              handleThenSubmit();
              return;
            }
            throw Error(res.status);
          })
          .catch(function (error) {
            toast.warning("Server error");
          });
      } else {
        update(obj)
          .then((res) => {
            console.log(res);
            if (res?.data?.data) {
              toast.success("Update success");
              handleThenSubmit();

              return;
            }
            throw Error(res.status);
          })
          .catch(function (error) {
            toast.warning("Server error");
          });
      }
    }
  };

  const handleThenSubmit = () => {
    providerValue.setIsOpenFormInput(false);
    providerValue.setId(null);
    providerValue.handleLoadPageData();
  };

  const validateProfile = () => {
    console.log("Validating...");
    if (name === "") {
      toast.warning("Name is required");
      return false;
    } else if (username === "") {
      toast.warning("Username is required");
      return false;
    } else if (yearOfBirth === "") {
      toast.warning("Year of Birth is required");
      return false;
    } else if (sex === "") {
      toast.warning("Sex is required");
      return false;
    } else if (school === "") {
      toast.warning("School is required");
      return false;
    } else if (major === "") {
      toast.warning("Major is required");
      return false;
    }
    return true;
  };

  const handleChange = (value, source) => {
    console.log("call handleChange" + value);
    switch (source) {
      case "name":
        setName(value);
        break;
      case "yearOfBirth":
        setYearOfBirth(value);
        break;
      case "sex":
        setSex(value);
        break;
      case "username":
        setUsername(value);
        break;
      case "school":
        setSchool(value);
        break;
      case "major":
        setMajor(value);
        break;
      default:
        break;
    }
  };

  return (
    <div className={styles.container}>
      <div className={styles.dialog}>
        {/* icon delete */}
        <div className={styles.box} onClick={() => handleClose()}>
          <MdClose className={styles.icon} />
        </div>
        {/* Title */}
        {!id && <h2 className={styles.title}>NEW STUDENT</h2>}
        {id && <h2 className={styles.title}>EDIT STUDENT</h2>}
        {/* Content */}
        <div className={styles.content}>
          {/* Name */}
          <div className={styles.form}>
            <input
              type="text"
              className={styles.formInput}
              autoComplete="off"
              placeholder=" "
              value={name ? name : ""}
              onChange={(input) => handleChange(input.target.value, "name")}
              required="required"
            />
            <label className={styles.formLabel}>Name</label>
          </div>
          {/* Username */}
          <div className={styles.form}>
            <input
              type="text"
              className={styles.formInput}
              autoComplete="off"
              placeholder=" "
              value={username ? username : ""}
              onChange={(input) => handleChange(input.target.value, "username")}
              required="required"
            />
            <label className={styles.formLabel}>Username</label>
          </div>
          {/* Year of Birth */}
          <div className={styles.form}>
            <input
              type="number"
              className={styles.formInput}
              autoComplete="off"
              placeholder=" "
              value={yearOfBirth ? yearOfBirth : ""}
              onChange={(input) =>
                handleChange(input.target.value, "yearOfBirth")
              }
              required="required"
            />
            <label className={styles.formLabel}>Year of Birth</label>
          </div>
           {/* Sex */}
           <div className={styles.form}>
            <input
              type="text"
              className={styles.formInput}
              autoComplete="off"
              placeholder=" "
              value={sex ? sex : ""}
              onChange={(input) => handleChange(input.target.value, "sex")}
              required="required"
            />
            <label className={styles.formLabel}>Sex</label>
          </div>
          {/* School */}
          <div className={styles.form}>
            <input
              type="text"
              className={styles.formInput}
              autoComplete="off"
              placeholder=" "
              value={school ? school : ""}
              onChange={(input) => handleChange(input.target.value, "school")}
              required="required"
            />
            <label className={styles.formLabel}>School</label>
          </div>
          {/* Major */}
          <div className={styles.form}>
            <input
              type="text"
              className={styles.formInput}
              autoComplete="off"
              placeholder=" "
              value={major ? major : ""}
              onChange={(input) => handleChange(input.target.value, "major")}
              required="required"
            />
            <label className={styles.formLabel}>Major</label>
          </div>
        </div>

        {/* Save */}
        <div className={styles.footer}>
          <button
            type="button"
            className={styles.btn}
            onClick={() => handleSubmit()}
          >
            SAVE
          </button>
        </div>
      </div>
    </div>
  );
}

export default memo(AttendeeDialog);
