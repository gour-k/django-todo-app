
# Django Todo App

## Introduction

This is a simple yet powerful to-do application built with Django. It allows users to manage their daily tasks efficiently. The application supports basic CRUD (Create, Read, Update, Delete) operations for to-do items.

## Features

- Create new to-do items
- View the list of all to-do items
- Update existing to-do items
- Delete to-do items
- Responsive design using Bootstrap

## Installation

Before installation, ensure you have Python and pip installed on your system.

1. Clone the repository:
   ```
   git clone https://github.com/gour-k/django-todo-app.git
   ```
2. Navigate to the project directory:
   ```
   cd django-todo-app
   ```
3. Create a Virtual environment
   ```
   python3 -m venv env
   ```
4. Activate a Virtual environment
   ```
   source env/bin/activate
   ```
5. Install the requirements:
   ```
   pip install -r requirements.txt
   ```
6. Run migrations:
   ```
   python manage.py makemigrations && python manage.py migrate
   ```
7. Start the server:
   ```
   python manage.py runserver
   ```

## Usage

After starting the server, visit `http://localhost:8000/` in your browser to start using the application.