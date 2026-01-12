# 🍋 Little Lemon Restaurant

A Django-based restaurant website with online booking and menu management.

## Features
- Online table reservation
- Dynamic menu display
- REST API

## Tech Stack
- Python 3.10+
- Django 5.x
- Django REST Framework

## Quick Start
```bash
git clone https://github.com/kelsonbrito50/littlelemon.git
cd littlelemon
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
Visit http://127.0.0.1:8000/

## Installation (Detailed)

### Step 1: Clone the repository
```bash
git clone https://github.com/kelsonbrito50/littlelemon.git
cd littlelemon
```

### Step 2: Create virtual environment

**Linux (Fedora/Ubuntu) & macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows (Command Prompt):**
```cmd
python -m venv venv
venv\Scripts\activate
```

**Windows (PowerShell):**
```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

### Step 3: Install dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run migrations
```bash
python manage.py migrate
```

### Step 5: Start server
```bash
python manage.py runserver
```

### Step 6: Open browser
Visit http://127.0.0.1:8000/

## Pages
| Page | URL |
|------|-----|
| Home | / |
| Menu | /menu/ |
| Booking | /book/ |
| About | /about/ |
| Admin | /admin/ |

## Create Admin User (Superuser)

To access the admin panel at http://127.0.0.1:8000/admin/, you need to create a superuser:
```bash
python manage.py createsuperuser
```

You will be prompted to enter:
- **Username:** Choose any username (e.g., admin)
- **Email:** Your email address (optional, press Enter to skip)
- **Password:** Choose a strong password (min 8 characters)
- **Password (again):** Confirm your password

Example:
```
Username: admin
Email address: admin@example.com
Password: ********
Password (again): ********
Superuser created successfully.
```

Now you can log in at http://127.0.0.1:8000/admin/ with your credentials.

### What you can do in Admin Panel:
- Add/Edit/Delete menu items
- View and manage bookings
- Manage users

## Running in Visual Studio Code

1. Open folder in VS Code: `code .`
2. Install extensions: Python, Pylance, Django
3. Select interpreter: Ctrl+Shift+P > "Python: Select Interpreter" > select venv
4. Open terminal: Ctrl+`
5. Run: `python manage.py runserver`

## License
This project is for educational purposes.
