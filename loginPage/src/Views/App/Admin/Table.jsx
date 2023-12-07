import React from 'react'
import AdminProducts from './AdminProducts'
import AdminUser from "./AdminUsers"
import { Button } from 'antd'
import { useNavigate } from 'react-router-dom'


function Table() {
  const navigate=useNavigate()
  return (
    <>
    <div><Button name='Logout' onClick={()=>{
      localStorage.removeItem("token")
navigate("/login")
    }}>Logout</Button></div>
    <div style={{display:"flex",flexDirection:"row",marginLeft:"40px"}}>
<div><AdminProducts/></div>
<div style={{marginLeft:"40px"}}><AdminUser/></div>

    </div>
    </>
  )
}

export default Table