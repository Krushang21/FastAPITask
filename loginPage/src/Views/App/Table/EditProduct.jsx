import React, { useEffect, useState } from "react";
import PostAPIAddUser from "../../../Common/AddProduct";
import { useLocation, useParams } from "react-router-dom";
import axios from "axios";

const token = localStorage.getItem("token");
function EditProduct() {
  const [data, setData] = useState();
  const location = useLocation();

  const id = useParams();

  useEffect(() => {
    axios
      .get(`http://127.0.0.1:8000/products/${+id.id}`, {
        headers: {
          "Content-Type": "application/json",
          Authorization: `${token}`,
        },
      })
      .then((response) => {
        setData(response.data);
      });
  }, [setData]);
  return (
    <>
      <div>EditProduct</div>
      <PostAPIAddUser editvalues={data} />
    </>
  );
}

export default EditProduct;
