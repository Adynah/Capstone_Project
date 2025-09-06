import React from "react";
import { Link } from "react-router-dom";

function Register() {
  return (
    <div>
      <h1>Register</h1>

      <form>
        <div>
          <label>Username</label>
          <input type="text" name="username" />
        </div>

        <div>
          <label>Full Name</label>
          <input type="text" name="name" />
        </div>

        <div>
          <label>Password</label>
          <input type="password" name="password" />
        </div>

        <div>
          <label>Phone Number</label>
          <input type="phone" name="phone" />
        </div>

        <button type="submit">Continue</button>
      </form>

      <span>
        Already a user? <Link to="/login">Login</Link>.
      </span>
    </div>
  );
}

export default Register;