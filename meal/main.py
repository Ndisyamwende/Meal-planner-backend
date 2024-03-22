from fastapi import FastAPI
from . import models
from .database import engine
from .routers import meal, user, preference, authentication

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(authentication.router)
app.include_router(user.router)
app.include_router(preference.router)
app.include_router(meal.router)