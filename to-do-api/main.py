from fastapi import FastAPI,Header
import sqlite3
from pydantic import BaseModel
from passlib.context import CryptContext
import secrets
from datetime import datetime

app = FastAPI()

conn = sqlite3.connect(
    "blog.db",
    check_same_thread=False
)
cursor = conn.cursor()

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
               email TEXT,
               name TEXT,
               password TEXT,
               token TEXT
               )""")

conn.commit()

cursor.execute("""
            CREATE TABLE IF NOT EXISTS todos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
               title TEXT,
               description TEXT,
               user_id INTEGER,
               created_at TEXT,
               updated_at TEXT
               )""")

conn.commit()

class Register(BaseModel):
    name: str
    email: str
    password:str

class Login(BaseModel):
    email:str
    password:str

class Todo(BaseModel):
    title: str
    description:str

@app.post("/register")
def register(user:Register):
    cursor.execute("SELECT * FROM users WHERE email=?",(user.email,))
    row=cursor.fetchone()
    if row:
        return {
            "message": "Email already exists"
        }
    hashed_password = pwd_context.hash(user.password)
    token = secrets.token_hex(16)
    cursor.execute("""INSERT INTO users(
               email,
               name ,
               password ,
               token 
                    ) VALUES(?,?,?,?)""",(
                        user.email,
                        user.name,
                        hashed_password,
                        token
                    ))
    conn.commit()
    return{
    "token": token
}

@app.post("/login")
def login(user: Login):
    cursor.execute(
        "SELECT * FROM users WHERE email=?",
        (user.email,)
    )
    row = cursor.fetchone()
    if not row:
        return {
            "message": "Invalid email or password"
        }

    if not pwd_context.verify(user.password, row[3]):
        return {
            "message": "Invalid email or password"
        }
    return {
        "token": row[4]
    }

@app.post("/todos")
def create_todo(
    todo: Todo,
    authorization: str = Header(None)
):
    if not authorization:
        return {
            "message": "Unauthorized"
        }

    cursor.execute(
        "SELECT * FROM users WHERE token=?",
        (authorization,)
    )
    user = cursor.fetchone()
    if not user:
        return {
            "message": "Unauthorized"
        }
    current_time = datetime.now().isoformat()
    cursor.execute("""
        INSERT INTO todos (
            title,
            description,
            user_id,
            created_at,
            updated_at
        )
        VALUES (?, ?, ?, ?, ?)
    """, (
        todo.title,
        todo.description,
        user[0],
        current_time,
        current_time
    ))
    conn.commit()
    todo_id = cursor.lastrowid
    return {
        "id": todo_id,
        "title": todo.title,
        "description": todo.description,
        "user_id": user[0],
        "created_at": current_time,
        "updated_at": current_time
    }

@app.get("/todos")
def get_todos(authorization: str = Header(None)):
    if not authorization:
        return {
            "message": "Unauthorized"
        }
    cursor.execute("SELECT * FROM users WHERE token=?", (authorization,))
    user = cursor.fetchone()
    if not user:
        return {
            "message": "Unauthorized"
        }
    cursor.execute("""SELECT * FROM todos WHERE user_id=?""",(user[0],))
    rows = cursor.fetchall()
    todos = []
    for row in rows:
        todos.append({
            "id": row[0],
            "title": row[1],
            "description": row[2],
            "user_id": row[3],
            "created_at": row[4],
            "updated_at": row[5]
        })
    return todos

@app.get("/todos/{id}")
def get_todo(id: int, authorization: str = Header(None)):
    if not authorization:
        return {"message": "Unauthorized"}
    cursor.execute(
        "SELECT * FROM users WHERE token=?",
        (authorization,)
    )
    user = cursor.fetchone()
    if not user:
        return {"message": "Unauthorized"}
    cursor.execute(
        "SELECT * FROM todos WHERE id=? AND user_id=?",
        (id, user[0])
    )
    row = cursor.fetchone()
    if not row:
        return {"message": "Todo not found"}
    return {
        "id": row[0],
        "title": row[1],
        "description": row[2],
        "user_id": row[3],
        "created_at": row[4],
        "updated_at": row[5]
    }

@app.put("/todos/{id}")
def update_todo(
    id: int,
    todo: Todo,
    authorization: str = Header(None)
):
    if not authorization:
        return {"message": "Unauthorized"}
    cursor.execute(
        "SELECT * FROM users WHERE token=?",
        (authorization,)
    )
    user = cursor.fetchone()
    if not user:
        return {"message": "Unauthorized"}

    cursor.execute(
        "SELECT * FROM todos WHERE id=?",
        (id,)
    )
    row = cursor.fetchone()
    if not row:
        return {"message": "Todo not found"}

    if row[3] != user[0]:
        return {"message": "Forbidden"}
    updated_at = datetime.now().isoformat()
    cursor.execute("""
        UPDATE todos
        SET
            title=?,
            description=?,
            updated_at=?
        WHERE id=?
    """, (
        todo.title,
        todo.description,
        updated_at,
        id
    ))
    conn.commit()
    return {
        "id": id,
        "title": todo.title,
        "description": todo.description,
        "user_id": user[0],
        "created_at": row[4],
        "updated_at": updated_at
    }

@app.delete("/todos/{id}")
def delete_todo(
    id: int,
    authorization: str = Header(None)
):
    if not authorization:
        return {"message": "Unauthorized"}
    cursor.execute(
        "SELECT * FROM users WHERE token=?",
        (authorization,)
    )
    user = cursor.fetchone()
    if not user:
        return {"message": "Unauthorized"}
    cursor.execute(
        "SELECT * FROM todos WHERE id=?",
        (id,)
    )
    row = cursor.fetchone()
    if not row:
        return {"message": "Todo not found"}
    if row[3] != user[0]:
        return {"message": "Forbidden"}
    cursor.execute(
        "DELETE FROM todos WHERE id=?",
        (id,)
    )
    conn.commit()
    return {
        "message": "Todo deleted successfully"
    }

@app.get("/todos")
def get_todos(
    page: int = 1,
    limit: int = 10,
    authorization: str = Header(None)
):
    offset = (page - 1) * limit
    cursor.execute(
        "SELECT * FROM todos LIMIT ? OFFSET ?",
        (limit, offset)
    )
    rows = cursor.fetchall()
    return rows