# 🛒 Django E-Commerce Backend (Dockerized)

A production-style Django backend for an e-commerce platform built to practice real-world backend architecture, authentication systems, and scalable API design.

---

## 🚀 Project Overview

This project is a backend-only e-commerce system built with Django, focusing on:

- Authentication & Authorization
- Scalable project structure
- Clean architecture principles
- Real-world backend patterns (signals, CBVs, modular apps)
- Dockerized development environment

The goal of this project is to simulate a **production-ready backend system**, not just a tutorial project.

---

## 🧱 Tech Stack

- Python 3.x
- Django
- Django REST Framework (future expansion)
- PostgreSQL
- Docker & Docker Compose
- Redis (planned for async tasks)
- Celery (planned for background jobs)

---

## 🔐 Features Implemented

### Authentication System
- Custom User model (AbstractUser)
- Login / Logout / Register system
- Session-based authentication
- Django messages integration

### Profile System
- One-to-One Profile model
- Automatic profile creation using signals

### Access Control
- Protected views using LoginRequiredMixin
- Separation of authenticated/unauthenticated flows

### Architecture
- Modular Django app structure
- Separation of concerns (views, models, forms)
- CBV + FBV hybrid approach based on use-case

---

## 🐳 Docker Setup

### Build and run project:

```bash
docker-compose up --build
````

### Run migrations:

```bash
docker-compose exec web python manage.py migrate
```

### Create superuser:

```bash
docker-compose exec web python manage.py createsuperuser
```

---

## 📁 Project Structure (simplified)

```text
django-ecommerce-backend/
│
├── apps/
│   └── accounts/
│       ├── models.py
│       ├── views.py
│       ├── forms.py
│       ├── signals.py
│       └── urls.py
│
├── config/
│   ├── settings.py
│   ├── urls.py
│
├── templates/
├── static/
├── docker-compose.yml
├── Dockerfile
└── manage.py
```

---

## 🧠 What I Learned

* Django authentication internals
* Custom user model design
* Signals and lifecycle hooks
* Class-Based vs Function-Based views
* Dockerized development workflow
* Git branching and PR-based development

---

## 🔜 Roadmap

* [ ] Role-Based Access Control (RBAC)
* [ ] Django REST Framework API layer
* [ ] JWT Authentication
* [ ] Product & Order system
* [ ] Cart & Checkout flow
* [ ] Celery + Redis background tasks
* [ ] Email system (password reset, notifications)
* [ ] Payment integration (Stripe or similar)

---

## 📌 Purpose

This project is part of my journey to become a **professional Python/Django backend developer**, focusing on real-world architecture and scalable systems.

---

## 👨‍💻 Author

Esmael Hoosini
GitHub: [https://github.com/esmael1997](https://github.com/esmael1997)
LinkedIn: [https://www.linkedin.com/in/esmael-hoosini-58683b1b1](https://www.linkedin.com/in/esmael-hoosini-58683b1b1)

```
