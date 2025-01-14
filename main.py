import uvicorn
from fastapi import FastAPI, Depends
from sqlmodel import Session, select
from db import get_session

app = FastAPI()

@app.get("/")
def root():
    return {"message" : "Hello World"}



if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)

