import React from 'react';
import { BrowserRouter as Router, Route, Routes, Navigate } from 'react-router-dom';
import CustomerDashboard from './components/CustomerDashboard';

function App() {
  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/" element={<Navigate replace to="/customer-dashboard" />} />
          <Route path="/customer-dashboard" element={<CustomerDashboard />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
