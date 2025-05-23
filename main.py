# main.py

# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def read_root():
#     return {"message": "Welcome to my FastAPI app!"}

# @app.get("/hello/{name}")
# def read_item(name: str):
#     return {"message": f"Hello, {name}!"}

######

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI"}

