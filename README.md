# Personal Portfolio & Management System (Django)

A full-stack dynamic personal portfolio web application built using Django, Python, and Bootstrap 4. This system features dynamic project showcasing, tech stack management, user testimonials, contact inquiry forms, and a superuser-restricted administrative dashboard.

---

## Key Features

- **Dynamic Project Showcase (`/projects/`):** Renders project cards dynamically from the SQLite database, including descriptions, live links, and assigned tech stack badges[cite: 10].
- **Testimonial Management (`/testimonies/`):** Public feedback form submission and dynamic listing of recommendations[cite: 10].
- **Contact Inquiries (`/contact/`):** Custom form capturing user messages saved directly into the `Inquiry` model[cite: 10].
- **Superuser Authentication (`/login/`):** Secure login view restricted specifically to accounts with `is_superuser` privileges[cite: 10].
- **Management Dashboard (`/dashboard/`):** Tabular interface displaying existing projects and tech stacks with direct creation controls[cite: 10].
- **Many-to-Many Tech Stack Mapping:** Relational mapping linking reusable `TechStack` items across multiple projects seamlessly[cite: 10].

---

## Tech Stack & Design System

- **Framework:** Python 3.10+ / Django 5.x
- **Frontend:** HTML5, CSS3, JavaScript, Bootstrap 4, Font Awesome
- **Database:** SQLite3 (Development & Cloud)[cite: 10]
- **Typography:** Cinzel (Headings), Plus Jakarta Sans (Body Text)
- **Color Palette:**
  - Dark Forest Green: `#013328`
  - Charcoal Background: `#100C0D`
  - Terracotta Highlight: `#CC8B65`
  - Sand Off-White: `#E3DCD2`

---

## Detailed Setup & Local Installation Guide

Follow these exact sequential steps to configure, install, and run the project environment on your local machine.

---

### Step 1: System Prerequisites
Ensure the following software is installed on your computer before proceeding:
- **Python:** Version 3.10 or higher (`python --version` or `python3 --version`)
- **Git:** Version Control System (`git --version`)

---

### Step 2: Clone the Project Repository
Open your terminal (PowerShell, Command Prompt, or Terminal) and clone the repository:

```bash
git clone [https://github.com/Aldrin072807/OBJORG2026.git](https://github.com/Aldrin072807/OBJORG2026.git)
cd OBJORG2026

## Repository Structure

```text
OBJORG2026/
├── portfolio/                  # Core Django Application
│   ├── templates/portfolio/    # HTML Templates
│   │   ├── dashboard.html      # Admin dashboard view
│   │   ├── projects.html       # Dynamic project list
│   │   ├── create_project.html # Project creation form
│   │   └── ...                 # Additional template views
│   ├── models.py               # Project, TechStack, Testimony, Inquiry models
│   ├── views.py                # View handling & superuser protection logic
│   ├── forms.py                # ModelForms for project & tech stack forms
│   └── urls.py                 # Application route definitions
├── portfolio_project/          # Django Project Configuration
│   ├── settings.py             # App configurations, middleware, ALLOWED_HOSTS
│   ├── urls.py                 # Root URL patterns
│   └── wsgi.py                 # WSGI web server interface
├── manage.py                   # Django CLI utility
├── requirements.txt            # Python dependencies
└── README.md                   # Complete project documentation

## Detailed Setup & Local Installation Guide

Follow these exact sequential steps to configure, install, and run the project environment on your local machine.

---

### Step 1: System Prerequisites
Ensure the following software is installed on your computer before proceeding:
- **Python:** Version 3.10 or higher (`python --version` or `python3 --version`)
- **Git:** Version Control System (`git --version`)

---

### Step 2: Clone the Project Repository
Open your terminal (PowerShell, Command Prompt, or Terminal) and clone the repository:

```bash
git clone [https://github.com/Aldrin072807/OBJORG2026.git](https://github.com/Aldrin072807/OBJORG2026.git)
cd OBJORG2026