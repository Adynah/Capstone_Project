import React from "react";
import { Link } from "react-router-dom";

function Home() {
  return (
    <div>
      <nav>
        <div>
          <img src="/assets/CSLogo.jpg" alt="Logo" />
        </div>

        {/* Navigation links */}
        <div>
          <Link to="/">Home</Link>
          <Link to="/about">About</Link>
          <Link to="/services">Services</Link>
          <Link to="/contact">Contact</Link>
        </div>

        {/* Buttons */}
        <div>
          <Link to="/register">Register</Link>
          <Link to="/login">Login</Link>
        </div>
      </nav>

      {/* Hero Section */}
      <section>
        <h1>Welcome</h1>
        <img src="/assets/CS-motto" alt="Brand name and motto" />
      </section>
    </div>
  );
}

export default Home