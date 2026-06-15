# Todo List API

A RESTful API built with FastAPI and SQLite that allows users to register, log in, and manage their personal to-do lists. The API includes authentication, authorization, CRUD operations, and pagination.

## Features

* User Registration
* User Login
* Password Hashing with Passlib and Bcrypt
* Token-Based Authentication
* Create Todo
* Get All Todos
* Get Single Todo
* Update Todo
* Delete Todo
* Authorization (Users can only manage their own todos)
* Pagination Support
* SQLite Database

## Technologies Used

* Python
* FastAPI
* SQLite
* Pydantic
* Passlib
* Bcrypt
* Uvicorn

## Installation

### Clone the Repository

```bash
git clone <your-repository-url>
cd todo-api
```

### Create Virtual Environment

```bash
python3 -m venv venv
```

### Activate Virtual Environment

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
pip install fastapi uvicorn passlib bcrypt
```

### Run the Application

```bash
uvicorn main:app --reload
```

The API will be available at:

http://127.0.0.1:8000

Swagger Documentation:

http://127.0.0.1:8000/docs

## Database Schema

### Users Table

| Column   | Type    |
| -------- | ------- |
| id       | INTEGER |
| email    | TEXT    |
| name     | TEXT    |
| password | TEXT    |
| token    | TEXT    |

### Todos Table

| Column      | Type    |
| ----------- | ------- |
| id          | INTEGER |
| title       | TEXT    |
| description | TEXT    |
| user_id     | INTEGER |
| created_at  | TEXT    |
| updated_at  | TEXT    |

## API Endpoints

### Register User

POST /register

Request:

```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "password": "password123"
}
```

Response:

```json
{
  "token": "generated_token"
}
```

### Login User

POST /login

Request:

```json
{
  "email": "john@example.com",
  "password": "password123"
}
```

Response:

```json
{
  "token": "generated_token"
}
```

### Create Todo

POST /todos

Header:

```text
Authorization: your_token
```

Request:

```json
{
  "title": "Buy groceries",
  "description": "Milk, eggs and bread"
}
```

### Get All Todos

GET /todos

Header:

```text
Authorization: your_token
```

### Get Single Todo

GET /todos/{id}

Header:

```text
Authorization: your_token
```

### Update Todo

PUT /todos/{id}

Header:

```text
Authorization: your_token
```

Request:

```json
{
  "title": "Updated title",
  "description": "Updated description"
}
```

### Delete Todo

DELETE /todos/{id}

Header:

```text
Authorization: your_token
```

## Pagination

Get paginated todos:

```http
GET /todos?page=1&limit=10
```

Example Response:

```json
{
  "data": [],
  "page": 1,
  "limit": 10,
  "total": 0
}
```

## Future Improvements

* JWT Authentication
* Refresh Tokens
* Filtering
* Sorting
* SQLAlchemy ORM
* PostgreSQL Support
* Unit Testing
* Docker Deployment

## Author

Sneha Agrawal
