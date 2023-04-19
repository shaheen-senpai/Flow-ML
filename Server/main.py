# Main Imports
from fastapi import FastAPI

#Development Imports
from icecream import ic

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}