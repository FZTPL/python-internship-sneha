# Blogging Platform API

A RESTful Blog API built using FastAPI and SQLite. This project allows users to create, read, update, delete, and search blog posts through HTTP endpoints.

## Features

* Create a new blog post
* Get all blog posts
* Get a single blog post by ID
* Update an existing blog post
* Delete a blog post
* Search blog posts by title, content, or category
* Automatic API documentation with Swagger UI

## Tech Stack

* Python
* FastAPI
* SQLite
* Pydantic
* Uvicorn

## Project Structure

```text
Blog-API/
│
├── main.py
├── blog.db
├── requirements.txt
└── README.md
```

## Installation

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd Blog-API
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

Mac/Linux:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install fastapi uvicorn pydantic
```

## Running the Application

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

ReDoc Documentation:

```text
http://127.0.0.1:8000/redoc
```

## API Endpoints

### Create Blog Post

```http
POST /posts
```

Request Body:

```json
{
  "title": "My First Blog",
  "content": "This is my first blog post.",
  "category": "Technology",
  "tags": ["Python", "FastAPI"]
}
```

### Get All Posts

```http
GET /posts
```

### Get Single Post

```http
GET /posts/{id}
```

Example:

```http
GET /posts/1
```

### Update Post

```http
PUT /posts/{id}
```

Example:

```http
PUT /posts/1
```

### Delete Post

```http
DELETE /posts/{id}
```

Example:

```http
DELETE /posts/1
```

### Search Posts

```http
GET /posts?term=python
```

Searches across:

* Title
* Content
* Category

## Database Schema

### posts

| Column     | Type    |
| ---------- | ------- |
| id         | INTEGER |
| title      | TEXT    |
| content    | TEXT    |
| category   | TEXT    |
| tags       | TEXT    |
| created_at | TEXT    |
| updated_at | TEXT    |

## Learning Outcomes

This project helped in understanding:

* RESTful API design
* CRUD operations
* HTTP methods
* Request validation using Pydantic
* SQLite database integration
* SQL queries (SELECT, INSERT, UPDATE, DELETE)
* Path parameters
* Query parameters
* JSON serialization and deserialization
* API testing using Swagger UI

## Author

Sneha Agrawal
