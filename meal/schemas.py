from pydantic import BaseModel
from typing import List, Dict, Union

class Meal(BaseModel):
    image: str
    title: str
    ingredients: List[Union[str, int]]
    recipe: List[Union[str, int]]
    nutrition: Dict[str, Union[str, int]]
