# 📚 Django Bookstore Management System

A web application built using Django that allows users to register, log in, browse books, add them to a cart, and manage bookings. Admins can manage the book inventory using a custom admin panel.

---

## 🚀 Features

- User Registration & Login
- Browse and search books
- Add books to cart and calculate total
- View and cancel bookings
- Admin panel to add/edit/delete books
- Payment simulation
- Fully Dockerized + Jenkins CI/CD support

---

## 🛠️ Tech Stack

- Python 3.11
- Django 5.2
- SQLite (default) / PostgreSQL (Docker)
- Bootstrap 5
- Docker + Docker Compose
- Jenkins (CI/CD)

---

## 🖥️ Setup Instructions 

1. Clone the repo:
   git clone https://github.com/Chaitanya-G15/Ticket-Booking-Management-System.git
   cd Django-Bookstore
   
3. Create virtual environment:
   python -m venv env
   env\Scripts\activate
   
5. Install dependencies:
   pip install -r requirements.txt
   
7. Run migrations:
   python manage.py migrate
   
9. Start development server:
   python manage.py runserver
   
11. Build & start containers:
   docker-compose up --build

13. Run migrations:
   docker-compose run web python manage.py migrate

15. Visit app:
   http://localhost:8000
