import React from "react";
import { Link } from "react-router-dom";

function Contact() {
  return (
    <div>
      <h1>Contact Us</h1>

      <form>
        <div>
          <label>Email</label>
          <input type="email" name="email" />
        </div>

        <div>
          <label>Full Name</label>
          <input type="text" name="fullname" />
        </div>

        <div>
          <label>Subject</label>
          <input type="text" name="subject" />
        </div>

        <div>
          <label>Enter your message</label>
          <textarea name="message"></textarea>
        </div>

        <button type="submit">Submit</button>
        <a href="https://wa.me/your-number" target="_blank" rel="noopener noreferrer">
          <img src="/assets/whatsapp-logo.jpg" alt="WhatsApp" /> WhatsApp
        </a>
        <a href="tel:+1234567890">
          <img src="/assets/call-logo.jpg" alt="Call" /> Call
        </a>
      </form>
    </div>
  );
}

export default Contact;