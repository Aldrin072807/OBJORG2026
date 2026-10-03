# Personal Portfolio & Management System (OBJORG2026)

Dynamic web application built with Django for managing personal portfolio entries, project showcases, technology stacks, and visitor feedback.

## Description

This project serves as a full-stack dynamic portfolio platform designed for computer engineering students and web developers. Built using Django and Bootstrap 4, the system allows visitors to explore completed projects with direct tech-stack tags, view client testimonials, and send contact inquiries.

The platform features a superuser-restricted administration dashboard (`/dashboard/`) requiring dedicated authentication (`/login/`). Through this dashboard, administrators can create and manage project entries and technology stacks using a dynamic Many-to-Many relational mapping system.

The project is structured for easy setup in both local development environments and cloud hosting platforms like PythonAnywhere.

## Getting Started

### Dependencies

- **Operating System:** Windows 10/11, macOS, or Linux
- **Python:** Version 3.10 or higher (`python --version` or `python3 --version`)
- **Git:** Version Control System (`git --version`)
- **Virtual Environment:** `venv` (standard Python library) or `virtualenvwrapper`

### Installing

#### 1. Clone the Repository

Open your terminal and clone the project repository from GitHub:

```bash
git clone https://github.com/Aldrin072807/OBJORG2026.git
cd OBJORG2026
```

#### 2. Set Up a Virtual Environment

Create and activate an isolated environment to prevent dependency conflicts.

**Windows (PowerShell / Command Prompt):**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**macOS / Linux / Bash:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

#### 3. Install Dependencies

Install all required libraries specified in `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Executing the Program

Follow these steps to initialize the database and launch the development server.

### 1. Apply Database Migrations

Initialize the SQLite database schema:

```bash
python manage.py migrate
```

### 2. Create Administrative Superuser Account

Create an administrative superuser required to access the restricted routes (`/login/` and `/dashboard/`):

```bash
python manage.py createsuperuser
```

Follow the terminal prompts to set your username, email, and password.

### 3. Run the Development Server

Start the Django local development server:

```bash
python manage.py runserver
```

### 4. Access Application Routes

Open your web browser and navigate through the following paths:

| Page | URL |
|---|---|
| Home Page | `http://127.0.0.1:8000/` |
| Projects Showcase | `http://127.0.0.1:8000/projects/` |
| Testimonials | `http://127.0.0.1:8000/testimonies/` |
| Superuser Login | `http://127.0.0.1:8000/login/` |
| Management Dashboard | `http://127.0.0.1:8000/dashboard/` |

## Common Issues & Troubleshooting

### DisallowedHost Error on Cloud/PythonAnywhere Deployment

Ensure `portfolio_project/settings.py` includes your domain in `ALLOWED_HOSTS`:

```python
ALLOWED_HOSTS = [
    'aldrin0728.pythonanywhere.com',
    '127.0.0.1',
    'localhost',
]
```

### NoReverseMatch Template Error

Verify that your template URL tags match the route names defined in `portfolio/urls.py`.

For project creation, use:

```django
{% url 'portfolio:create_project' %}
```

### Missing Package or Incompatible Django Version

If running Python 3.10 in a hosted environment, install a compatible Django 5.x release:

```bash
pip install "Django>=5.0,<6.0"
```

## Authors

**Aldrin Marquez Desepeda**

- GitHub: [@Aldrin072807](https://github.com/Aldrin072807)
- Role: Computer Engineering Student & Project Lead
- Institution: Holy Angel University

## Version History

### 0.2 — Current Release (Quiz 5 & 6)

- Added superuser authentication gate at `/login/`
- Integrated tabular management dashboard at `/dashboard/`
- Implemented dynamic Many-to-Many Tech Stack mapping across projects
- Deployed live cloud application to PythonAnywhere
- Updated template URL routes and view logic

### 0.1 — Initial Release

- Added static templates
- Added Bootstrap styling
- Added basic model structure
- Added public portfolio pages

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments

- **Holy Angel University — Department of Computer Engineering** for academic coursework guidelines
- **Bootstrap 4 & Font Awesome** for responsive component libraries and icons
- **PythonAnywhere** for cloud hosting services