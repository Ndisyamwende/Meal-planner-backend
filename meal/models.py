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
    
class User(Base):
    
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    
class Preferences(Base):
    
    __tablename__ = "preferences"
    
    id = Column(Integer, primary_key=True, index=True)
    allergens = Column(String)
    dietary_type = Column(String)