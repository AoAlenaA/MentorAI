from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware

from .schemas import LoginRequest, LoginResponse, UserResponse
from .security import FAKE_USER, create_access_token, get_current_user

app = FastAPI(title='MentorAI API', version='0.0.1')

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:5173'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)


@app.get('/api/health')
async def healthcheck() -> dict[str, str]:
    return {'status': 'ok'}


@app.post('/api/auth/login', response_model=LoginResponse)
async def login(payload: LoginRequest) -> LoginResponse:
    if payload.email != FAKE_USER['email'] or payload.password != FAKE_USER['password']:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Неверный e-mail или пароль'
        )

    access_token = create_access_token(FAKE_USER['email'])
    user = UserResponse(
        id=FAKE_USER['id'],
        email=FAKE_USER['email'],
        name=FAKE_USER['name'],
        role=FAKE_USER['role']
    )

    return LoginResponse(access_token=access_token, user=user)


@app.get('/api/me', response_model=UserResponse)
async def me(current_user: dict = Depends(get_current_user)) -> UserResponse:
    return UserResponse(
        id=current_user['id'],
        email=current_user['email'],
        name=current_user['name'],
        role=current_user['role']
    )
