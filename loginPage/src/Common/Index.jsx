import React from 'react'
import { Route, Routes } from 'react-router-dom'
import AddProduct from "./AddProduct"
import AddUser from "./AddUser"
import EditProduct from '../Views/App/Table/EditProduct'
import EditUser from '../Views/App/Table/EditUser'
function Addproducts() {
  return (
    <Routes>
        <Route path="addProduct" element={<AddProduct/>}/>
        <Route path="adduser" element={<AddUser/>}/>
        <Route path="EditProduct/:id" element={<EditProduct/>}/>
        <Route path="EditUser/:id" element={<EditUser/>}/>
    </Routes>
  )
}

export default Addproducts