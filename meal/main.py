from fastapi import FastAPI, Depends, status, Response, HTTPException
from . import schemas, models
from .database import engine, SessionLocal
from sqlalchemy.orm import Session
from .encryption import Encryption

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
# Meals
@app.post("/meal", status_code=status.HTTP_201_CREATED, tags=['meals'])
def create_meal(request: schemas.Meal, db: Session = Depends(get_db)):
    new_meal = models.Meal(image=request.image, title=request.title, ingredients=request.ingredients, recipe=request.recipe, nutrition=request.nutrition)
    db.add(new_meal)
    db.commit()
    db.refresh(new_meal)
    return new_meal

@app.delete("/meal/{meal_id}", status_code=status.HTTP_204_NO_CONTENT, tags=['meals'])
def delete_meal(meal_id: int, db: Session = Depends(get_db)):
    meal = db.query(models.Meal).filter(models.Meal.id == meal_id)
    if not meal.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Meal with id {meal_id} not found")
    meal.delete(synchronize_session=False)
    db.commit()
    return "done"

@app.put("/meal/{meal_id}", status_code=status.HTTP_202_ACCEPTED, tags=['meals'])
def update_meal(meal_id: int, request: schemas.Meal, db: Session = Depends(get_db)):
    meal = db.query(models.Meal).filter(models.Meal.id == meal_id)
    if not meal.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Meal with id {meal_id} not found")
    meal.update(request.model_dump())
    db.commit()
    return "updated"

@app.get("/meal", tags=['meals'])
def get_meals(db: Session = Depends(get_db)):
    meals = db.query(models.Meal).all()
    return meals

@app.get("/meal/{meal_id}", status_code=status.HTTP_200_OK, tags=['meals'])
def get_meal(meal_id: int,response: Response, db: Session = Depends(get_db)):
    meal = db.query(models.Meal).filter(models.Meal.id == meal_id).first()
    if not meal:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Meal with id {meal_id} not available")
    return meal

# User
@app.post("/user", status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser, tags=['users'])
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    
    new_user = models.User(name=request.name, email=request.email, password=Encryption.encrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.get("/user/{user_id}", response_model=schemas.ShowUser, tags=['users'])
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {user_id} not found")
    return user