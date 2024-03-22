from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from .. import database, schemas
from ..repository import preference

router = APIRouter(
    prefix="/preference",
    tags=['preferences']
)
get_db = database.get_db


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_preference(request: schemas.Preferences, db: Session = Depends(get_db)):
    return preference.create(request, db)

@router.get('/')
def get_preferences(db: Session = Depends(get_db)):
    return preference.get(db)

@router.get('/{preference_id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowPreferences)
def get_preference(preference_id: int, db: Session = Depends(get_db)):
    return preference.get_one(preference_id, db)

@router.put('/{preference_id}', status_code=status.HTTP_202_ACCEPTED)
def update_preference(preference_id: int, request: schemas.Preferences, db: Session = Depends(get_db)):
    return preference.update(preference_id, request, db)