import React from "react";
import { Link } from "react-router-dom";

function Login() {
  return (
    <div>
      <h1>Login</h1>

      <form>
        <div>
          <label>Username</label>
          <input type="text" name="username" />
        </div>

        <div>
          <label>Password</label>
          <input type="password" name="password" />
        </div>

        <button type="submit">Continue</button>
      </form>

      <span>
        New here? <Link to="/register">Register</Link>.
      </span>
    </div>
  );
}

export default Login;