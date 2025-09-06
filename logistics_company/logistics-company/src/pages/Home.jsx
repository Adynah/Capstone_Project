import React from "react";
import { Link } from "react-router-dom";

function Home() {
  return (
    <div>
      {/* Hero Section */}
      <section>
        <h1>Welcome</h1>
        <img src="/assets/CS-motto" alt="Brand name and motto" />
      </section>

      {/* Buttons */}
        <div>
          <Link to="/register">Register</Link>
          <Link to="/login">Login</Link>
        </div>
    </div>
  );
}

export default Home;