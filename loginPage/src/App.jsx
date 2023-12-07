import Loginpage from "./Views/User/Login/loginpage";
import Index from "./Views/App";
// import ProductTable from "./App/table"
// import AdminTable from "./App/tableAdmin"
import {BrowserRouter, Route, Routes, Navigate} from "react-router-dom";
import CustomerTable from "./Views/App/Customer/CustomerTable";
// import AdminProducts from "./App/Forms/AdminProducts";
// import AdminUser from "./App/Forms/AdminUsers";
// import AddProduct from './App/Forms/AddProduct'
// import EditProduct from './App/Forms/EditProduct.jsx'
// import setupAxiosInterceptors from './axiosConfig.js'
function App() {


  // const[authenticated, setAuthenticated] = useState(false);
  
  return (
    <>
    <div>
    <BrowserRouter>
      <Routes>
      <Route path="/" element={<Loginpage/>} />
      <Route path="/login" element={<Loginpage/>} />
      <Route path='customer' element={<CustomerTable/>}/>

      <Route path="/admin/*" element={<Index/>} />

      {/* <Route path="/pro" element={authenticated ? <AdminTable /> : <Navigate to="/" />}/> */}
      {/* <Route path="/home" element={authenticated ? <AdminTable /> : <Navigate to="/" />}/> */}
      {/* <Route path="/admin" element={<AdminProducts/>}/>
      <Route path="/users" element={<AdminUser/>}/>
      <Route path="/admin/addProduct" element={<AddProduct/>}/>
      <Route path="admin/EditProduct/:id" element={<EditProduct/>}/> */}

      </Routes>
    </BrowserRouter>
    </div>
    </>
  )
}

export default App