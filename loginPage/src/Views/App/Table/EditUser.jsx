import React, { useEffect, useState } from "react";
import AddUser from "../../../Common/AddUser";
import { useLocation, useParams } from "react-router-dom";
import axios from "axios";

const token = localStorage.getItem("token");
function EditUser() {
  const [data, setData] = useState();
  const location = useLocation();

  const id = useParams();
  // console.log("id:", id);
  useEffect(() => {
    // console.log(id);
    axios
      .get(`http://127.0.0.1:8000/users/${id.id}`, {
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
      <div>EditUser</div>
      <AddUser editvalues={data} id={id.id} />
    </>
  );
}

export default EditUser;
