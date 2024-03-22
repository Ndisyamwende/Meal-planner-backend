from pydantic import BaseModel
from typing import List, Dict, Union

class Meal(BaseModel):
    image: str
    title: str
    ingredients: List[Union[str, int]]
    recipe: List[Union[str, int]]
    nutrition: Dict[str, Union[str, int]]
    
    
class ShowMeal(BaseModel):
    class Config:
        orm_mode = True
        
class User(BaseModel):
    name: str
    email: str
    password: str
    
class ShowUser(BaseModel):
    name: str
    email: str
    
    class Config:
        orm_mode = True
        
class Preferences(BaseModel):
    allergens: str
    dietary_type: str
