from fastapi import FastAPI,Request
import sqlite3
from pydantic import BaseModel
from datetime import datetime
import json

app = FastAPI()

conn = sqlite3.connect(
    "blog.db",
    check_same_thread=False
)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    content TEXT,
    category TEXT,
    tags TEXT,
    created_at TEXT,
    updated_at TEXT
)
""")

conn.commit()

class Post(BaseModel):
    title: str
    content: str
    category:str
    tags:list[str]

@app.post("/posts")
def create_post(post: Post):
    current_time = datetime.now().isoformat()
    tags_text = json.dumps(post.tags)
    cursor.execute("""
        INSERT INTO posts (
            title,
            content,
            category,
            tags,
            created_at,
            updated_at
        )
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        post.title,
        post.content,
        post.category,
        tags_text,
        current_time,
        current_time
    ))
    conn.commit()
    post_id = cursor.lastrowid
    return {
        "id": post_id,
        "title": post.title,
        "content": post.content,
        "category": post.category,
        "tags": post.tags,
        "created_at": current_time,
        "updated_at": current_time
    }

@app.get("/posts")
def read_post():
    cursor.execute(" SELECT * from posts")
    rows=cursor.fetchall()
    post=[]
    for row in rows:
        col={
            "id": row[0],
            "title": row[1],
            "content": row[2],
            "category": row[3],
            "tags": json.loads(row[4]),
            "created_at": row[5],
            "updated_at": row[6],
        }
        post.append(col)
    return post

@app.get("/posts/{id}")
def get_post(id: int):
    cursor.execute("SELECT * FROM posts WHERE id = ?",(id,))
    row = cursor.fetchone()
    if row is None:
        return {"message": "Post not found"}
    col = {
        "id": row[0],
        "title": row[1],
        "content": row[2],
        "category": row[3],
        "tags": json.loads(row[4]),
        "created_at": row[5],
        "updated_at": row[6]
    }
    return col

@app.put("/posts/{id}")
def update_post(id:int,post:Post):
    cursor.execute("SELECT * FROM posts WHERE id=?",(id,))
    row=cursor.fetchone()
    if row is None:
        return {"message":"Post not found"}
    update_time=datetime.now().isoformat()
    cursor.execute("""
    UPDATE posts
    SET
        title = ?,
        content = ?,
        category = ?,
        tags = ?,
        updated_at = ?
    WHERE id = ?
    """, (
        post.title,
        post.content,
        post.category,
        json.dumps(post.tags),
        update_time,
        id
    ))
    conn.commit()
    return{
        "id": row[0],
        "title": post.title,
        "content": post.content,
        "category": post.category,
        "tags": post.tags,
        "created_at": row[5],
        "updated_at": update_time
    }

@app.delete("/posts/{id}")
def delete_post(id:int):
    cursor.execute("SELECT * FROM posts WHERE id=?",(id,))
    row=cursor.fetchone()
    if row is None:
        return {"message":"Post not found"}
    cursor.execute("DELETE FROM posts WHERE id=?",(id,))
    conn.commit()
    return{
        "message":"Post deleted succesfully"
    }

@app.get("/posts")
def read_post(term: str = None):
    if term:
        search_term = f"%{term}%"
        cursor.execute("""
            SELECT * FROM posts
            WHERE title LIKE ?
            OR content LIKE ?
            OR category LIKE ?
        """, (
            search_term,
            search_term,
            search_term
        ))
    else:
        cursor.execute("SELECT * FROM posts")
    rows = cursor.fetchall()
    posts = []
    for row in rows:
        posts.append({
            "id": row[0],
            "title": row[1],
            "content": row[2],
            "category": row[3],
            "tags": json.loads(row[4]),
            "created_at": row[5],
            "updated_at": row[6]
        })
    return posts