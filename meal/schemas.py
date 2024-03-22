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
    
class Preferences(BaseModel):
    allergens: str
    dietary_type: str
    
    class Config:
        orm_mode = True
    
class ShowUser(BaseModel):
    name: str
    email: str
    preferences : List[Preferences] = []
    
    class Config:
        orm_mode = True
        
class ShowPreferences(BaseModel):
    allergens: str
    dietary_type: str
    owner: ShowUser
    
    class Config:
        orm_mode = True