
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
const setupAxiosInterceptors = () => {
    const navigate = useNavigate()
  axios.interceptors.response.use(
    (response) => response,
    (error) => {
      if (error.response && error.response.status === 401) {
        localStorage.removeItem('token');
        navigate('/')
        // You might want to navigate to the login page or handle it based on your application flow
        // Example: window.location.href = '/login';
      }
      return Promise.reject(error);
    }
  );
};

export default setupAxiosInterceptors;
