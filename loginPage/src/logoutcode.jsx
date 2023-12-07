import React from 'react';
import { useAuth } from './AuthContext'; // Import the useAuth hook

function SomeComponent() {
  const { logout } = useAuth();

  const handleLogout = () => {
    logout(); // Call the logout function
  };

  return (
    <button onClick={handleLogout}>Logout</button>
  );
}

export default SomeComponent;
