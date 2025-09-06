import React from "react";
import { Link } from "react-router-dom";

function Dashboard() {
  return (
    <div>
      <div>
        <img src="/assets/CSLogo.jpg" alt="Logo" />
      </div>

      <nav>
        <Link to="/">Home</Link>
        <Link to="/about">About</Link>
        <Link to="/services">Services</Link>
        <Link to="/contact">Contact</Link>
      </nav>

      <h1>Dashboard</h1>

      <table>
        <thead>
          <tr>
            <th>Order ID</th>
            <th>Customer</th>
            <th>Item</th>
            <th>Status</th>
          </tr>
        </thead>
        <tbody>
          {/* Orders will be dynamically rendered here */}
        </tbody>
      </table>
    </div>
  );
}

export default Dashboard