import React from "react";
import { Link } from "react-router-dom";

function Footer() {
  return (
    <footer>
      <div>
        <img src="/assets/CSLogo.jpg" alt="Logo" />
        <span>Capital Swift Logistics</span>
      </div>

      <div>
        <p>© 2025 Capital Swift Logistics. All rights reserved.</p>
      </div>

      <div>
        <a href="https://wa.me/your-number" target="_blank" rel="noopener noreferrer">
          <img src="/assets/whatsapp-logo.jpg" alt="WhatsApp" /> WhatsApp
        </a>
        <a href="tel:+1234567890">
          <img src="/assets/call-logo.jpg" alt="Call" /> Call
        </a>
      </div>
    </footer>
  );
}

export default Footer