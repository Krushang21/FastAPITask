import React from "react";
import { useFormik } from "formik";
import Axios from "axios";
import { useNavigate } from "react-router-dom";
import { notification } from "antd";
import { AddProductSchema } from "../Schema/AddProductSchema";

const token = localStorage.getItem("token");
const initialValues = {
  title: "",
  content: "",
};

function AddProduct({ editvalues }) {
  const navigate = useNavigate();

  const { values, errors, touched, handleBlur, handleChange, handleSubmit } =
    useFormik({
      initialValues: editvalues ? editvalues : initialValues,
      validationSchema: AddProductSchema,
      enableReinitialize: true,
      onSubmit: async (values) => {
        try {
          const url = editvalues
            ? `http://127.0.0.1:8000/products/${editvalues.id}`
            : "http://127.0.0.1:8000/products/";
          const response = await (editvalues ? Axios.put : Axios.post)(
            url,
            values,
            {
              headers: {
                "Content-Type": "application/json",
                Authorization: `${token}`,
              },
            }
          );
          console.log("Response from server:", response);
          notification.success({
            message: response?.data,
            duration: 10,
          });
        } catch (error) {
          console.error("Error:", error);
        }
        navigate(-1);
      },
    });
  return (
    <div className="container mt-5">
      <form onSubmit={handleSubmit}>
        <div className="mb-3">
          <label htmlFor="title" className="form-label">
            Product Title
          </label>
          <input
            type="text"
            className={`form-control ${
              errors.title && touched.title && "is-invalid"
            }`}
            id="title"
            autoComplete="off"
            placeholder="Enter Product Title"
            name="title"
            onChange={handleChange}
            onBlur={handleBlur}
            value={values.title}
          />
          {errors.title && touched.title && (
            <div className="invalid-feedback">{errors.title}</div>
          )}
        </div>

        <div className="mb-3">
          <label htmlFor="content" className="form-label">
            Product Content
          </label>
          <input
            type="text"
            className={`form-control ${
              errors.content && touched.content && "is-invalid"
            }`}
            id="content"
            autoComplete="off"
            placeholder="Enter Product Content"
            name="content"
            onChange={handleChange}
            onBlur={handleBlur}
            value={values.content}
          />
          {errors.content && touched.content && (
            <div className="invalid-feedback">{errors.content}</div>
          )}
        </div>

        <div className="d-flex justify-content-between">
          <button type="submit" className="btn btn-primary">
            {editvalues ? "Update Product" : "Add Product"}
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

export default AddProduct;
