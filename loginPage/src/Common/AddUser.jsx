import React from "react";
import { useFormik } from "formik";
import Axios from "axios";
import { useNavigate } from "react-router-dom";
import { notification } from "antd";
import { AddUserSchema } from "../Schema/AddUserSchema";
import { EditUserSchema } from "../Schema/EditUserSchema";
const token = localStorage.getItem("token");
const apiUrl = "http://127.0.0.1:8000/users/";

const initialValues = {
  username: "",
  email: "",
  password: "",
};

function AddUser({ editvalues, id }) {
  const navigate = useNavigate();

  const validationSchema = editvalues ? EditUserSchema : AddUserSchema;

  const { values, errors, handleBlur, handleChange, handleSubmit, touched } =
    useFormik({
      initialValues: editvalues || initialValues,
      validationSchema,
      enableReinitialize: true,
      onSubmit: async (values) => {
        // console.log("????????????????????????????????", values);
        // const data = {
        //   username: values?.username?.tr,
        //   email: values?.email?.trim(),
        // };
        // console.log("<><>????", editvalues);
        try {
          const url = editvalues
            ? `${apiUrl}${id}`
            : "http://127.0.0.1:8000/users/";

          const method = editvalues ? Axios.put : Axios.post;

          const response = await method(url, values, {
            headers: {
              "Content-Type": "application/json",
              Authorization: `${token}`,
            },
          });

          notification.success({
            message: response?.data,
            duration: 10,
          });
        } catch (error) {
          console.error("Error:", error);
          notification.error({
            message: "Error",
            description: `${error.response.data.detail}`,
            duration: 10,
          });
        }
        navigate(-1);
      },
    });

  return (
    <div className="form-parent">
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="username">Username</label>
          <input
            type="text"
            className={`form-control ${errors.username && "has-error"}`}
            id="username"
            autoComplete="off"
            placeholder="Enter Username"
            name="username"
            onChange={handleChange}
            onBlur={handleBlur}
            value={values.username}
          />
          {errors.username && touched.username && (
            <div className="error">{errors.username}</div>
          )}
        </div>

        <div className="form-group">
          <label htmlFor="email">E-Mail</label>
          <input
            type="text"
            className={`form-control ${errors.email && "has-error"}`}
            id="email"
            autoComplete="off"
            placeholder="Enter Email"
            name="email"
            onChange={handleChange}
            onBlur={handleBlur}
            value={values.email}
          />
          {errors.email && touched.email && (
            <div className="error">{errors.email}</div>
          )}
        </div>

        {!editvalues && (
          <div className="form-group">
            <label htmlFor="password">Password</label>
            <input
              type="text"
              className={`form-control ${errors.password && "has-error"}`}
              id="password"
              autoComplete="off"
              placeholder="Enter Password"
              name="password"
              onChange={handleChange}
              onBlur={handleBlur}
              value={values.password}
            />
            {errors.password && touched.password && (
              <div className="error">{errors.password}</div>
            )}
          </div>
        )}

        <div className="form-group">
          <button type="submit" className="btn btn-primary">
            Submit
          </button>
          <button
            type="button"
            className="btn btn-danger"
            onClick={() => navigate(-1)}
          >
            Cancel
          </button>
        </div>
      </form>
    </div>
  );
}

export default AddUser;
