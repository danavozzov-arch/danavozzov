from fastapi import FastAPI
import uvicorn
from starlette.responses import FileResponse
import sqlite3

app = FastAPI()


@app.get("/")
def read_root():
    return FileResponse("работа 1.3.html")

def add_item():
    name = int(input())
    conn = sqlite3.connect("test.db")
    c = conn.cursor()
    c.execute("INSERT INTO test1 VALUES (?)", (name, ))
    conn.commit()
    print("Добавил")
add_item()