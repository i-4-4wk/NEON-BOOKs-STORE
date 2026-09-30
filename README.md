# 📚 NeonBooks - Online Bookstore

A modern online bookstore built with **Flask**, **SQLAlchemy**, and **SQLite**.

## ✨ Features

- 📚 **Browse Books** — View all books in a beautiful grid layout
- 📖 **Book Details** — Click any book to see full details with big cover
- 🛒 **Shopping Cart** — Add books with quantity selection
- 📝 **Place Orders** — Enter client info to confirm order
- 🔐 **Admin Panel** — Add, delete books, and view orders
- 🖼️ **Cover Upload** — Upload book covers
- 🗄️ **Two Databases** — Separate databases for books and orders

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| **Python** | Backend language |
| **Flask** | Web framework |
| **SQLAlchemy** | ORM for database |
| **SQLite** | Database (books.db, clients.db) |
| **HTML/CSS** | Frontend |
| **Jinja2** | Template engine |

## 📁 Project Structure

```
neonbooks/
│
├── app.py                 # Main Flask application
├── dbconfig.py            # Database configuration
├── requirements.txt       # Python dependencies
│
├── templates/             # HTML files
│   ├── client.html        # Homepage
│   ├── admin.html         # Admin panel
│   ├── adminpanel.html    # Orders view
│   ├── add_book.html      # Add book form
│   ├── buybook.html       # Book details
│   └── cart.html          # Shopping cart
│
├── static/                # Static files
│   ├── style.css          # Main styles
│   ├── admin.css          # Admin styles
│   ├── buy.css            # Buy page styles
│   └── uploads/           # Book covers
│
└── instance/              # Databases (auto-created)
    ├── books.db           # Books data
    └── clients.db         # Orders data
```
