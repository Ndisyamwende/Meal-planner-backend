from fastapi import FastAPI
from . import schemas

app = FastAPI()



@app.post("/meal")
def create_meal(request: schemas.Meal):
    return request