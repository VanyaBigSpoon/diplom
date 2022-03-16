from fastapi import Depends

from src.controllers.controller_user import controller_get_current_user
from src.scheme.scheme_user import SchemeUser


class RolesChecker:
    def __init__(self, roles: list[int]):
        self.roles = roles

    def __call__(self, user: SchemeUser = Depends(controller_get_current_user)):
        if user.role_id not in self.roles:
            return False
        return True
