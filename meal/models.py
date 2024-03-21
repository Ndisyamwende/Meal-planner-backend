from sqlalchemy import Column, Integer, String
from .database import Base

class Meal(Base):
    
    __tablename__ = "meals"
    
    id = Column(Integer, primary_key=True, index=True)
    image = Column(String)
    title = Column(String)
    ingredients = Column(String)
    recipe = Column(String)
    nutrition = Column(String)