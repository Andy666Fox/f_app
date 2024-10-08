from fastapi import FastAPI, Request, status, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import ValidationError
from fastapi.responses import JSONResponse
from fastapi_users import FastAPIUsers


from auth.auth import auth_backend
from auth.schemas import UserCreate, UserRead
from auth.database import User
from auth.manager import get_user_manager

app = FastAPI(
    title='Fucking Slave'
)

@app.exception_handler(ValidationError)
async def validation_exception_handler(request: Request, exc: ValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({'detail': exc.errors()})
    )
    
fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend]
)


app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix='/auth/jwt',
    tags=['auth']
)


app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix='/auth',
    tags=['auth']
)






