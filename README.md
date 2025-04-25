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
   
2. Create virtual environment:
   python -m venv env
   env\Scripts\activate
   
3. Install dependencies:
   pip install -r requirements.txt
   
4. Run migrations:
   python manage.py migrate
   
5. Start development server:
   python manage.py runserver
   
6. Build & start containers:
   docker-compose up --build

7. Run migrations:
   docker-compose run web python manage.py migrate

8. Visit app:
   http://localhost:8000

![Screenshot 2025-04-25 124451](https://github.com/user-attachments/assets/17888eaa-79b0-4e5c-85c7-4dbbd3fab29c)
![Screenshot 2025-04-25 124439](https://github.com/user-attachments/assets/82026d70-1047-4b74-bfd4-434406100aaa)
![Screenshot 2025-04-25 124412](https://github.com/user-attachments/assets/58c87eef-d50d-4595-8e38-74bbdcb470ca)
![Screenshot 2025-04-25 124323](https://github.com/user-attachments/assets/34972350-c6cf-4645-a728-335a0644640a)
