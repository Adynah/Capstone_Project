# Capital Swift Logistics Web App
## Project Overview

Capital Swift Logistics is a web application built with React. The app allows users to:

- View company information and services
- Book deliveries
- Track delivery status (Dashboard)
- Register and login for personalized services
- Contact the company easily

The project uses JSX structure, with Tailwind CSS styling.

## Pages / Components
### Pages

- Home – Landing page with logo, navigation, welcome message, and call-to-action buttons (Register / Login).

- About – Company description, value proposition, and vision.

- Services – Displays services offered with service cards and key features (Reliable, Fast, Affordable).

- Contact – Contact form with Email, Full Name, Subject, Message, and action buttons (Submit, WhatsApp, Call).

- Register – Registration form for new users (Username/Full Name, Password, Phone Number).

- Login – User login page (Username/Email, Password).

- Booking – Delivery booking form with Name, Email, Phone Number, Pickup & Delivery Address, Estimated Delivery Time & Cost.

- Dashboard – Displays orders and delivery status; designed to fetch dynamic data from backend.

### Components

- Navbar – Logo and navigation links, visible on all pages.

- Footer – Company info, quick links, contact info, and copyright, visible on all pages.

## Project Structure

src/
├─ components/
│  ├─ Navbar.jsx
│  └─ Footer.jsx
├─ pages/
│  ├─ Home.jsx
│  ├─ About.jsx
│  ├─ Services.jsx
│  ├─ Contact.jsx
│  ├─ Register.jsx
│  ├─ Login.jsx
│  ├─ Booking.jsx
│  └─ Dashboard.jsx
├─ App.jsx
└─ index.jsx

## Features

- React Router for seamless navigation between pages
- Reusable Navbar and Footer components
- Forms ready for backend integration
- Dashboard ready to display dynamic delivery/order data