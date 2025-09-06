import React from "react";
import { Link } from "react-router-dom";

function Services() {
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

      <h1>Our Services</h1>
      <ul>
        <li>Personal Errands</li>
        <li>Corporate Logistics</li>
        <li>Airport Pickup</li>
        <li>Document & Parcel Delivery</li>
      </ul>

      <img src="/assets/CS delivery bike.png" alt="Delivery Bike" />

      <ul>
        <li>RELIABLE</li>
        <li>FAST</li>
        <li>AFFORDABLE</li>
      </ul>
    </div>
  );
}

export default Services