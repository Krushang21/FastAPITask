
import { BrowserRouter, Route, Routes } from 'react-router-dom'

import Table from './Admin/Table'
import Addproducts from "../../Common/Index"
import CustomerTable from './Customer/CustomerTable'

function Index() {
  return (
  
        <Routes>
            <Route path='table' element={<Table/>}/>

            <Route path="table/*" element={<Addproducts/>}/>
        </Routes>
  
  )
}

export default Index