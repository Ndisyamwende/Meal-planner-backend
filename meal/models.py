from sqlalchemy import Column, Integer, String, JSON
from .database import Base

class Meal(Base):
    
    __tablename__ = "meals"
    
    id = Column(Integer, primary_key=True, index=True)
    image = Column(String)
    title = Column(String)
    ingredients = Column(JSON)
    recipe = Column(JSON)
    nutrition = Column(JSON)