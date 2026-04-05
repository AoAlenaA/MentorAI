from datetime import datetime, timedelta, timezone
from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import JWTError, jwt

SECRET_KEY = 'mentorai-dev-secret-key'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 60
security = HTTPBearer()

FAKE_USER = {
    'id': 1,
    'email': 'aoanuchina@hse.edu.ru',
    'password': 'password123',
    'name': 'Алёна',
    'role': 'trainee'
}


def create_access_token(subject: str) -> str:
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    payload = {'sub': subject, 'exp': expire}
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


async def get_current_user(
    credentials: Annotated[HTTPAuthorizationCredentials, Depends(security)]
) -> dict:
    token = credentials.credentials

    try:
      payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError as exc:
      raise HTTPException(
          status_code=status.HTTP_401_UNAUTHORIZED,
          detail='Невалидный токен'
      ) from exc

    if payload.get('sub') != FAKE_USER['email']:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Пользователь не найден'
        )

    return FAKE_USER
