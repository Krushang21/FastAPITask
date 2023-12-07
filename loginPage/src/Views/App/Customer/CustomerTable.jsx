import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import { Table, Button, Space, notification } from "antd";

function CustomerTable() {
  const [dataSource, setDataSource] = useState([]);
  const token = localStorage.getItem("token");
  const navigate = useNavigate();

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get("http://127.0.0.1:8000/products/", {
          headers: {
            "Content-Type": "application/json",
            Authorization: `${token}`,
          },
        });
        setDataSource(response.data);
      } catch (error) {
        console.error("Error fetching data:", error);
        // You can handle the error here, e.g., show a notification
        notification.error({
          message: "Error",
          description: "Failed to fetch data. Please try again.",
        });
      }
    };

    fetchData();
  }, [token]);

  const columns = [
    {
      title: "Index",
      dataIndex: "index",
      key: "index",
      render: (text, record, index) => index + 1,
    },
    {
      key: "content",
      title: "Content",
      dataIndex: "content",
    },
    {
      key: "title",
      title: "Title",
      dataIndex: "title",
    },
    {
      key: "createdBy",
      title: "Created by",
      dataIndex: "creator_id",
    },
  ];
  const handleLogout = () => {
    localStorage.removeItem("token");
    navigate("/");
  };
  const handleEdit = (record) => {
    // Add your edit logic here
    navigate(`EditCustomer/${record.id}`, { state: { record: record } });
  };

  const handleDelete = async (record) => {
    try {
      let id = record.id;
      await axios.delete(`http://127.0.0.1:8000/products/${id}`, {
        headers: {
          "Content-Type": "application/json",
          Authorization: `${token}`,
        },
      });

      const updatedData = await axios.get("http://127.0.0.1:8000/products/", {
        headers: {
          "Content-Type": "application/json",
          Authorization: `${token}`,
        },
      });

      setDataSource(updatedData.data);
    } catch (error) {
      console.error("Error deleting or fetching data:", error);

      notification.error({
        message: "Error",
        description: "Error deleting product. Please try again.",
      });
    }
  };

  return (
    <div>
      <h1>Customer Table</h1>
      <Table columns={columns} dataSource={dataSource} />
      <Button onClick={handleLogout}>Logout</Button>
    </div>
  );
}

export default CustomerTable;
