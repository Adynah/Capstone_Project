import React from "react";
import { Link } from "react-router-dom";

function NavBar() {
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
    </div>
  );
}

export default NavBar