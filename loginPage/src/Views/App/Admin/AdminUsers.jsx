import { Table, Button, Space, Flex, notification, message } from "antd";
import axios from "axios";
import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
function AdminUser() {
  const [errorMessage, setErrorMessage] = useState();
  const [dataSource, setDataSource] = useState([]);
  const token = localStorage.getItem("token");
  const navigate = useNavigate();
  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/users/", {
        headers: {
          "Content-Type": "application/json",
          Authorization: `${token}`,
        },
      })
      .then((response) => {
        setDataSource(response.data);
      })
      .catch((error) => console.error("Errors", error));
  }, [token]);
  // console.log(dataSource);
  const columns = [
    {
      title: "Index",
      dataIndex: "index",
      key: "index",
      render: (text, record, index) => index + 1,
    },
    {
      key: "username",
      title: "username",
      dataIndex: "username",
    },
    {
      key: "email",
      title: "email",
      dataIndex: "email",
    },
    // {
    //   key: 'Number of Items Created*',
    //   title: 'Number of Items Created*',
    //   dataIndex: 'Number of Items Created*',
    //   render:(_,record)=>(
    //     <>

    //       <div>{record.items.length}</div>
    //     </>
    //   )
    // },
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
            <Button type="danger" onClick={() => handleDelete(record)}>
              Delete
            </Button>
          </Space>
        </>
      ),
    },
  ];

  const handleEdit = (record) => {
    // Add your edit logic here
    // console.log("<?>>>>>Rec", record);
    navigate(`EditUser/${record.id}`, { state: { record: record } });
  };

  const handleDelete = async (record) => {
    try {
      let id = record.id;
      await axios
        .delete(`http://127.0.0.1:8000/users/${id}`, {
          headers: {
            "Content-Type": "application/json",
            Authorization: `${token}`,
          },
        })
        .then((res) => {
          if (res?.status == 200) notification.warning({ message: res?.data });
        });

      const updatedData = await axios.get("http://127.0.0.1:8000/users/", {
        headers: {
          "Content-Type": "application/json",
          Authorization: `${token}`,
        },
      });

      setDataSource(updatedData.data);
      // navigate(-1);
    } catch (error) {
      console.error(error.response.data.detail, error);
      setErrorMessage(
        error.response?.status == 403 &&
          error.response?.data.detail === "Cannot Delete Self"
          ? "You cannot Delete Yourself"
          : "Error Deleting, Please Try Again"
      );
      setErrorMessage(
        error.response?.status == 500 &&
          error.response?.data.detail ===
            "User with this username already exists, please Try with different username"
      );
      notification.error({
        message: errorMessage,
        description: error.response.data.detail,
      });
      // console.log("<>Error", errorMessage);
    }
  };

  return (
    <>
      <h1>Admin Table</h1>
      <Button type="dashed" onClick={() => navigate("addUser")}>
        Add User
      </Button>
      <Table columns={columns} dataSource={dataSource} />
      <Flex gap="small" wrap="wrap"></Flex>
    </>
  );
}

export default AdminUser;
