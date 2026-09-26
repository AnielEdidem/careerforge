# CareerForge AI — Django MVP

A beginner-friendly AI CV generator.

## Features
- CV information form
- AI-assisted professional summary/experience rewriting
- CV preview
- PDF download
- SQLite database
- Django admin

## Setup

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

pip install -r requirements.txt
```

Copy `.env.example` to `.env` and add your OpenAI API key.

Then:

```bash
python manage.py migrate
python manage.py runserver
```

Open http://127.0.0.1:8000/

## Important
The MVP deliberately keeps authentication, payments, multiple templates, portfolio pages, and production deployment out of version 1. Add those after validating that people actually use/pay for the core CV workflow.
