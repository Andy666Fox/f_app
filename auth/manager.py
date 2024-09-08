from typing import Optional

from fastapi import Depends, Request
from fastapi_users import BaseUserManager, IntegerIDMixin

from auth.database import User, get_user_db

from config import USER_MANAGER_SECRET

class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    reset_password_token_secret = USER_MANAGER_SECRET
    verification_token_secret = USER_MANAGER_SECRET
    
    async def on_after_register(self, user: User, request: Optional[Request] = None) -> None:
        return await super().on_after_register(user, request)
    
    
async def get_user_manager(user_db = Depends(get_user_db)):
    yield UserManager(user_db)