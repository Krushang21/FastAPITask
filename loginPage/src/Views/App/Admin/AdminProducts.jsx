import { Table, Button, Space, Flex, notification } from "antd";
import axios from "axios";
import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

function AdminProducts() {
  const [dataSource, setDataSource] = useState([]);

  const token = localStorage.getItem("token");
  const navigate = useNavigate();
  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/products/", {
        headers: {
          "Content-Type": "application/json",
          Authorization: `${token}`,
        },
      })
      .then((response) => {
        setDataSource(response?.data);
      })
      .catch((error) => console.error("Errors", error));
  }, [token]);
  const columns = [
    {
      title: "Index",
      dataIndex: "index",
      key: "index",
      render: (text, record, index) => index + 1,
    },

    {
      key: "title",
      title: "Title",
      dataIndex: "title",
    },
    {
      key: "content",
      title: "Content",
      dataIndex: "content",
    },
    {
      key: "action",
      title: "Action",
      dataIndex: "action",
      render: (_, record) => (
        <>
          <Space>
            <Button
              type="dashed"
              onClick={() => {
                handleEdit(record);
              }}
            >
              Edit
            </Button>
            <Button type="dashed" onClick={() => handleDelete(record)}>
              Delete
            </Button>
          </Space>
        </>
      ),
    },
  ];

  const handleEdit = (record) => {
    // Add your edit logic here
    navigate(`EditProduct/${record.id}`, { state: { record: record } });
  };
  const handleDelete = (record) => {
    let id = record.id;
    axios
      .delete(`http://127.0.0.1:8000/products/${id}`, {
        headers: {
          "Content-Type": "application/json",
          Authorization: `${token}`,
        },
      })
      .then((res) => {
        if (res?.status == 200) {
          notification.warning({
            message: res?.data,
            duration: 10,
          });
        }
        return axios.get("http://127.0.0.1:8000/products/", {
          headers: {
            "Content-Type": "application/json",
            Authorization: `${token}`,
          },
        });
      })
      .then((updatedData) => {
        setDataSource(updatedData?.data);
      })
      .catch((error) => {
        console.error("Error deleting or fetching data:", error);
        notification.error({
          message: "Error",
          description: "An error occurred while deleting the record.",
        });
      });
  };

  return (
    <>
      <h1>Product Table</h1>
      <Button type="dashed" onClick={() => navigate("addProduct")}>
        Add Product
      </Button>
      <Table columns={columns} dataSource={dataSource} />
      <Flex gap="small" wrap="wrap"></Flex>
    </>
  );
}

export default AdminProducts;
