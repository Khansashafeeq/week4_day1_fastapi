from fastapi import FastAPI

app = FastAPI(title="Week4 Day1 FastAPI Demo")

@app.get("/")
def read_root():
    return {"message": "FastAPI is working!"}

@app.get("/hello/{name}")
def say_hello(name: str):
    return {"hello": name}

