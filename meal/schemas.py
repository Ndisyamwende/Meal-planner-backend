from pydantic import BaseModel

class Meal(BaseModel):
    image: str
    title: str
    ingredients: str
    recipe: str
    nutrition: str