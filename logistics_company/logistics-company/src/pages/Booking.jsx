import React from "react";
import { Link } from "react-router-dom";

function Booking() {
  return (
    <div>
      <h1>Book Our Service</h1>

      <form>
        <div>
          <label>Name</label>
          <input type="text" name="name" />
        </div>

        <div>
          <label>Email</label>
          <input type="email" name="email" />
        </div>

        <div>
          <label>Phone Number</label>
          <input type="tel" name="phone" />
        </div>

        <div>
          <label>Delivery Address</label>
          <input type="text" name="deliveryAddress" />
        </div>

        <div>
          <label>Pickup Address</label>
          <input type="text" name="pickupAddress" />
        </div>

        <div>
          <label>Estimated Delivery Time & Cost</label>
          <input type="text" name="estimatedTimeCost" />
        </div>

        <button type="submit">Submit</button>
      </form>
    </div>
  );
}

export default Booking