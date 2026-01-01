# Django Blog API

A RESTful Blog API built with **Django** and **Django REST Framework (DRF)**.  
This project supports authenticated post creation, draft/published workflows, categories, tags, comments, and JWT-based/Token authentication.

It is designed to demonstrate **clean backend architecture** and proper **ORM relationships**.

---

## Features

- JWT Authentication (Login / Refresh / Verify)
- User registration
- Blog posts with:
  - Draft & published states
  - Slug-based URLs
  - Author ownership
- Categories (One-to-Many)
- Tags (Many-to-Many)
- Comments on posts
- Object-level permissions (author-only edits)
- Search & filtering
- Clean app-based project structure
- Ready for testing & extension

---

## Tech Stack

- Python
- Django
- Django REST Framework
- Simple JWT
- SQLite (development)

---
