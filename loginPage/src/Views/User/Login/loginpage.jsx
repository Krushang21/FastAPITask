import "../../../assets/loginpage.css";
import * as yup from "yup";
import React, { useState, useEffect } from "react";
import { useFormik } from "formik";
import { TfiCheck } from "react-icons/tfi";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import { loginSchema } from "../../../Schema/loginschema";
import { notification } from "antd";

const Loginpage = () => {
  const [inputName, setInputName] = useState("");
  const [inputPassword, setInputPassword] = useState("");
  const navigate = useNavigate();

  const { errors, handleBlur, handleChange, touched } = useFormik({
    initialValues: {
      username: "",
      password: "",
    },
    validationSchema: loginSchema,
  });

  const onSubmit = async (e) => {
    e.preventDefault();

    try {
      const formData = new FormData();
      formData.append("username", inputName);
      formData.append("password", inputPassword);

      const response = await axios.post(
        "http://127.0.0.1:8000/login/login'",
        formData
      );

      const data = response.data;
      // console.log(data);

      if (data.access_token) {
        const token = data.access_token;
        localStorage.setItem("token", `Bearer ${token}`);

        if (data.user_type) {
          // console.log("Admin has Logged In");
          navigate("/admin/table");
        } else {
          // console.log("User has Logged In");
          navigate("/customer");
        }
      } else {
        console.error("Login failed:", data.detail);
      }
    } catch (error) {
      console.error("Error:", error);
      // console.log(error.response.data.detail);
      notification.error({
        message: error.response.data.detail,
      });
    }
  };

  return (
    <div className="mainDiv">
      <div className="ctn-parent">
        <div className="container d-flex justify-content-center align-items-center">
          <div className="row border rounded-5 bg-white shadow box-area shadow-pads">
            <div className="col-md-6 d-flex rounded-4 justify-content-center align-items-center flex-column leftbox">
              <p className="mt-3 mb-3">Welcome to</p>
              <img
                width="64"
                height="64"
                src="https://img.icons8.com/sf-black-filled/64/000000/rocket.png"
                alt="rocket"
                className="img-fluid mt-3"
              />
              <p className="fs-1 mb-0 text-wrap text-center spacer-head">
                Spacer
              </p>
              <p className="mt-5 mb-5 spacerPara text-wrap text-center">
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
                eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut
                enim ad minim veniam
              </p>
              <div className="left-links mb-4">
                <span>
                  {" "}
                  <a>CREATOR HERE </a>
                </span>
                |{" "}
                <span>
                  <a>DESIGNER HERE</a>
                </span>
              </div>
            </div>
            <div className="col-md-6 right-box">
              <div className="row-align-items-center">
                <div className="header-text mb-4">
                  <form onSubmit={onSubmit}>
                    <p className="mt-5 right-box-title">Create your account</p>
                    <div className="tickparent row">
                      <div className="name">
                        <label htmlFor="username">Name</label>
                        <input
                          type="text"
                          className={`form-control ${
                            errors.username && touched.username
                              ? "has-error"
                              : "has-success"
                          }`}
                          id="username"
                          autoComplete="off"
                          placeholder="Enter Name"
                          name="username"
                          value={inputName}
                          onChange={(e) => {
                            handleChange(e);
                            setInputName(e.target.value);
                          }}
                          onBlur={handleBlur}
                        />
                        {errors.username && touched.username && (
                          <div className="error">{errors.username}</div>
                        )}
                        {inputName.length > 0 && (
                          <div>
                            <TfiCheck
                              className={errors.username ? "red" : "green"}
                            />
                          </div>
                        )}
                      </div>
                    </div>
                    <div className="tickparent">
                      <div className="password">
                        <label htmlFor="password">Password</label>
                        <input
                          type="password"
                          className={`form-control ${
                            errors.password && touched.password
                              ? "has-error"
                              : "has-success"
                          }`}
                          id="password"
                          autoComplete="off"
                          placeholder="Enter Password"
                          name="password"
                          value={inputPassword}
                          onChange={(e) => {
                            handleChange(e);
                            setInputPassword(e.target.value);
                          }}
                          onBlur={handleBlur}
                        />
                        {errors.password && touched.password && (
                          <div className="error">{errors.password}</div>
                        )}
                        {inputPassword.length > 0 && (
                          <div>
                            <TfiCheck
                              className={errors.password ? "red" : "green"}
                            />
                          </div>
                        )}
                      </div>
                    </div>
                    <span>
                      <input type="checkbox" /> By Signing up I Agree{" "}
                      <a>Terms and conditions</a>
                    </span>
                    <div className="rightButtons">
                      <button type="submit">Sign In</button>
                    </div>
                  </form>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Loginpage;
