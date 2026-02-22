# TatiraLearning — Modern LMS Platform

TatiraLearning is a modern full-stack Learning Management System (LMS) built with Django REST Framework and a custom frontend.

The goal of this project is to create a scalable online learning platform where instructors can create courses and students can enroll, access lessons, and manage their learning experience.

This project is designed as a production-ready SaaS foundation.

---

# Features

## Authentication System
- User registration
- Secure login with JWT authentication
- Instructor and student roles
- Profile system

## Course Management
- Instructors can create courses
- Courses have title, description, price, and lessons
- Courses are stored in a PostgreSQL-ready database structure

## Lesson System
- Each course contains multiple lessons
- Lessons support video URLs
- Lessons are accessible only to enrolled students

## Enrollment System
- Students can enroll in courses
- Access control ensures only enrolled users can view course content

## API Architecture
- Built with Django REST Framework
- Fully API-driven backend
- Ready for frontend integration (React, Next.js, or custom frontend)

## Frontend Integration
- Custom frontend connected via REST API
- Dynamic course loading from backend
- Ready for login, signup, and dashboard UI

---

# Tech Stack

Backend:
- Python
- Django
- Django REST Framework
- JWT Authentication
- SQLite (development)
- PostgreSQL (production ready)

Frontend:
- HTML
- CSS
- JavaScript
- API integration with Django backend

Version Control:
- Git
- GitHub

---

# Project Structure
tatiralearning/
backend/
courses/
users/
config/
frontend/
index.html


---

# Current Status

Core LMS functionality is implemented:

- Authentication system
- Course creation
- Lesson system
- Enrollment system
- API integration
- Frontend-backend connection

Next steps include:

- Full frontend implementation
- Instructor dashboard
- Student dashboard
- Payment integration (Stripe)
- Production deployment

---

# Purpose of the Project

TatiraLearning is being developed as a scalable SaaS platform for online education.

It serves as:

- A real LMS platform foundation
- A production-ready backend architecture
- A scalable course platform
- A base for future commercial deployment

---

# Author

Created and developed by Tatatirac.
