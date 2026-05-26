from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.user_model import User
from app.schemas.user_schema import UserCreate
from app.utils.auth import hash_password

from app.schemas.login_schema import Login
from app.utils.auth import verify_password, create_access_token
from fastapi.security import OAuth2PasswordRequestForm

router=APIRouter()

@router.post("/signup")
def signup(user:UserCreate,db:Session=Depends(get_db)):
    
    existing_user=db.query(User).filter(User.email==user.email).first()

    if existing_user:
        return{"message":"User already exists"}
    
    hashed_password=hash_password(user.password)
    
    new_user=User(
        email=user.email,
        username=user.username,
        password=hashed_password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return {
        "message": "User created successfully",
        "data":{ 
            "id": new_user.id,
            "username": new_user.username,
            "email":new_user.email
        }
    }

@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    existing_user = db.query(User).filter(
        User.email == form_data.username
    ).first()

    if not existing_user:
        return {
            "message": "User not found"
        }

    if not verify_password(
        form_data.password,
        existing_user.password
    ):
        return {
            "message": "Invalid password"
        }

    access_token = create_access_token(
        data={
            "sub": existing_user.email
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }

