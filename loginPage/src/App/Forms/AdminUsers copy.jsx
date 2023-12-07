// AdminUsers.js
import { Table } from "antd";
import React, { useEffect, useState } from "react";
import axios from "axios"; // Import the configured Axios instance

function AdminUsers() {
  const [dataSource, setDataSource] = useState([]);

  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/user/allusers")
      .then((response) => {
        // console.log('API Response:', response.data);
        setDataSource(response.data);
      })
      .catch((error) => console.error("Errors", error));
  }, []);

  const columns = [
    {
      key: "username",
      title: "Username",
      dataIndex: "username",
    },
    {
      key: "email",
      title: "Email",
      dataIndex: "email",
    },
    {
      key: "is_admin",
      title: "Is Admin",
      dataIndex: "is_admin",
      render: (is_admin) => (is_admin ? "Yes" : "No"),
    },
    {
      key: "items",
      title: "Items",
      dataIndex: "items",
      render: (items) => items.length, // Assuming you want to display the number of items
    },
  ];

  return (
    <>
      <div>AdminHome</div>
      <Table columns={columns} dataSource={dataSource} />
    </>
  );
}

export default AdminUsers;
