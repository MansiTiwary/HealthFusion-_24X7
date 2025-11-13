🏥 Hospital Management System (HMS)
MAD-1 Project November 2025 [@MansiTiwary]/Hospital-Management-System
<div align="center">
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://www.google.com/search?q=https://img.shields.com/badge/Flask-000000%3Fstyle%3Dfor-the-badge%26logo%3Dflask%26logoColor%3Dwhite"/>
<img src="https://www.google.com/search?q=https://img.shields.com/badge/Jinja2-000000%3Fstyle%3Dfor-the-badge%26logo%3Djinja%26logoColor%3Dwhite"/>
<img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white"/> 
<img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white"/>
<img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white"/>
<img src="https://img.shields.io/badge/Bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white"/>
</div>

<br>
<h2>📝 Table of Contents</h2>
<br>
 * 📖 Overview
 * 🛠 Tech Stack
 * ✨ Core Features
   * 🧑‍💼 Admin (Hospital Staff)
   * 👨‍⚕ Doctor
   * 🧑‍ Patient
 * 🔑 Key Terminologies & Data Models
 * 🚀 Getting Started
 * 🌱 Recommended Enhancements
 * 📜 License
<br>
<br>

<h2>📖 Overview</h2>
<br>
The Hospital Management System (HMS) is a web-based application designed to streamline operations for modern healthcare facilities. It provides a centralized, role-based platform for managing patients, doctors, appointments, and treatment records. The system replaces manual processes and disconnected software with an integrated solution, ensuring efficient record-keeping, conflict-free scheduling, and comprehensive patient history tracking for Admins, Doctors, and Patients.
<br>
<br>
<h3>🛠 Tech Stack</h3>
<br>
 * 🐍 Python (Backend Logic)
 * ⚗ Flask (Web Application Framework)
 * 💾 SQLite (Mandatory Database for data persistence)
 * 🧩 HTML5, CSS3, Jinja2 (Frontend Templating and Structure)
 * 🅱 Bootstrap (Responsive and Aesthetic Design)
 <br>
 <br>
<h3>✨ Core Features</h3>
<br>
The application provides distinct functionalities for each user role: Admin, Doctor, and Patient.
<br>
🧑‍💼 Admin (Hospital Staff)
The Admin serves as the superuser with full management control. Admin access is pre-existing and created programmatically upon application setup.
 * Dashboard & Analytics: View quick stats like total doctors, patients, and appointments.
 * Doctor Management: Add, update, and delete doctor profiles (name, specialization, availability).
 * Appointment Management: View and manage all upcoming and past appointments.
 * User Search: Search for patients or doctors by name/specialization/ID/contact.
 * Data Oversight: Edit doctor and patient details; remove/blacklist doctors and patients from the system.
 <br>
👨‍⚕ Doctor
The Doctor's interface focuses on managing their schedule and patient care.
 * Dashboard: Displays upcoming appointments for the day/week and a list of assigned patients.
 * Availability Management: Provide and update availability for the next 7 days.
 * Appointment Status: Option to mark appointments as Completed or Cancelled.
 * Treatment History: View full patient history (previous diagnoses & prescriptions) for informed consultation.
 * Treatment Update: Enter diagnosis, prescription, and treatment notes after a visit is completed.
 <br>
🧑‍ Patient
The Patient interface allows users to manage their medical care from registration to appointment history.
 * Secure Access: Register and log in to the application.
 * Profile Management: Edit personal details.
 * Doctor Search & View: Display available specializations/departments and doctor profiles. View doctor availability for the coming 7 days.
 <br>
 * Appointment Management:
   * Book appointments based on doctor specialization and availability.
   * Reschedule or cancel existing appointments.
   * Prevent multiple appointments at the same date and time for the same doctor.
   <br>
 * History: View upcoming appointments and their status, as well as past appointment history with diagnosis and prescriptions.
 <br>
 <br>
<h3>🔑 Key Terminologies & Data Models</h3>
<br>
The system is built around several core entities, with relationships defined to ensure data integrity.
Core Entities
| Entity | Description | Key Attributes (Non-Exhaustive) |
|---|---|---|
| Admin (Hospital Staff) | Superuser with system-wide access. | User ID, Username, Password, Role ('Admin') |
| Doctor | Medical professional in the system. | Doctor ID, Name, Specialization, Contact, Availability |
| Patient | User seeking medical care. | Patient ID, Name, Contact, Email, Password |
| Appointment | Scheduled meeting between Patient and Doctor. | Appointment ID, Patient ID (FK), Doctor ID (FK), Date, Time, Status (Booked/Completed/Cancelled) |
| Treatment | Record of medical care provided during an appointment. | Appointment ID (FK), Diagnosis, Prescription, Notes |
| Specialization | Field of medical science. | Department ID, Department Name, Description |
> ⚠ Note: The final database schema must be documented in the Project Report via an ER Diagram detailing all tables and their relations.
> 
<h3>🚀 Getting Started</h3>
<br>
Prerequisites
 * Python 3.x
 * pip (Python package installer)
 * virtualenv (Recommended for environment isolation)
Installation and Setup
 * Clone the Repository:
   git clone https://github.com/[Your GitHub Username]/Hospital-Management-System.git
cd Hospital-Management-System

 * Set up Virtual Environment (Recommended):
   python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

 * Install Dependencies:
   pip install -r requirements.txt

   (Dependencies will include Flask, SQLAlchemy, etc.)
 * Run the Application:
   The database will be created programmatically on startup, including the pre-existing Admin user.
   python app.py

 * Access the Application:
   Open your web browser and navigate to http://localhost:5000.
🌱 Recommended Enhancements
These optional features are suggested to enhance the application's robustness and user experience.
 * API Resources: Create RESTful API endpoints (using Flask-RESTful or standard Flask JSON responses) for interacting with core resources like Users and Appointments (with at least 4 HTTP methods).
 * Data Visualization: Use external libraries like Chart JS to create charts for Admin dashboard analytics (e.g., appointment trends, doctor load).
 * Validation: Implement comprehensive frontend validation (HTML5/JavaScript) and robust backend validation in controllers.
 * Security: Incorporate a dedicated login system using extensions like Flask-Login or Flask-Security to manage user sessions and prevent unauthorized access.
 <br>
<h3>📜 License</h3>
<br>
This project is open source and available under the MIT License.
<br>
Developed with ❤️ by [@MansiTiwary] — November 2025