# Personal Blog Application

A simple personal blog built with Flask that allows visitors to read articles and an admin to manage articles through a protected dashboard.

## Features

### Guest Section

* View all published articles on the home page
* Read individual articles
* View article publication dates

### Admin Section

* Secure login system
* Dashboard to manage articles
* Add new articles
* Edit existing articles
* Delete articles
* Logout functionality

## Technologies Used

* Python
* Flask
* HTML
* CSS
* JSON
* Sessions for Authentication

## Project Structure

```text
personalblog/
│
├── app.py
├── articles/
│   ├── 1.json
│   ├── 2.json
│   └── ...
│
├── templates/
│   ├── home.html
│   ├── article.html
│   ├── dashboard.html
│   ├── add_article.html
│   ├── edit_article.html
│   └── login.html
│
├── static/
│   └── style.css
│
├── README.md
└── requirements.txt
```

## Installation

### Clone the Repository

```bash
git clone <repository-url>
cd personalblog
```

### Create a Virtual Environment

```bash
python3 -m venv venv
```

### Activate the Virtual Environment

macOS/Linux:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install flask
```

## Running the Application

Start the Flask development server:

```bash
python3 app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

## Admin Login

Default credentials:

```text
Username: admin
Password: password123
```

## Data Storage

Articles are stored as JSON files inside the `articles` directory.

Example:

```json
{
    "id": 1,
    "title": "My First Blog",
    "content": "This is my first blog post.",
    "date": "2026-06-09"
}
```

## Learning Outcomes

This project demonstrates:

* Flask routing
* Template rendering with Jinja2
* Form handling
* File operations
* JSON data storage
* Session-based authentication
* CRUD operations
* Basic web application structure

## Future Improvements

* SQLite database integration
* User registration
* Password hashing
* Categories and tags
* Search functionality
* Responsive design
* Rich text editor
* Comments system

## Author

Sneha Agrawal
