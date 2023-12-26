from datetime import timedelta, datetime
from jose import jwt

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from starlette import status

from database import get_db
from domain.user import user_crud, user_schema
from domain.user.user_crud import pwd_context

ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24
SECRET_KEY = "fd190a8214902f1d72934049b896e04cb039aa52a252f3e1f32d40b5a82f79e2"
ALGORITHM = "HS256"

router = APIRouter(
    prefix="/api/user",
)


@router.post(
    "/login",
    response_model=user_schema.Token,
)
def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    user = user_crud.get_user(db, form_data.username)
    if not user or not pwd_context.verify(form_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    data = {
        "sub": user.username,
        "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
    }
    access_token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "username": user.username,
    }


@router.post(
    "/create",
    status_code=status.HTTP_204_NO_CONTENT,
)
def user_create(
    _user_create: user_schema.UserCreate,
    db: Session = Depends(get_db),
):
    user = user_crud.get_existing_user(db, _user_create)
    if user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="이미 존재하는 사용자입니다.",
        )
    user_crud.create_user(db, _user_create)
