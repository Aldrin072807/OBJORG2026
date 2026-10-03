# Personal Portfolio Web Application (Django)

A full-stack, dynamic personal portfolio application built with Django and Bootstrap 4, featuring dynamic database binding, testimonial management, inquiry forms, and a superuser-only administration dashboard with tech stack tracking.

---

## Features

- **Home & Personal Info Pages:** Dynamic context rendering personal details, educational background, and experience.
- **Projects Showcase:** Displays projects with descriptions, direct links, and linked tech stack badges.
- **Testimonials System:** Form submission and listing views for user feedback and recommendations.
- **Contact & Inquiries:** Processing raw HTML form submissions stored in the `Inquiry` model.
- **Superuser Dashboard (`/login/` & `/dashboard/`):** Restricted authentication for superusers to manage and create projects and tech stacks in clean tabular formats.
- **Tech Stack Mapping:** `ManyToManyField` mapping allowing reusable tech stack objects across multiple projects without duplication.

---

## Tech Stack & Color Palette

- **Framework:** Python 3.10+ / Django 5.x / 6.x
- **Frontend:** HTML5, CSS3, Bootstrap 4, Font Awesome
- **Typography:** Cinzel (Headings), Plus Jakarta Sans (Body Text)
- **Palette:**
  - Primary Background: `#013328` (Forest Green)
  - Secondary Background: `#100C0D` (Dark Charcoal)
  - Accent Color: `#CC8B65` (Terracotta / Tan)
  - Text Color: `#E3DCD2` (Sand / Off-white)

---

## Getting Started / Local Setup Instructions

Follow these steps to clone, set up, and run the project locally.

### 1. Prerequisites

Ensure you have Python 3.10 or higher installed on your machine.

### 2. Clone the Repository

```bash
git clone [https://github.com/Aldrin072807/OBJORG2026.git](https://github.com/Aldrin072807/OBJORG2026.git)
cd OBJORG2026/OBJORG2026