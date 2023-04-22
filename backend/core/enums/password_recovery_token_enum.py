from datetime import timedelta
from enum import Enum


class PasswordRecoveryEnum(Enum):
    PASSWORD_RECOVERY = ('password_recovery',timedelta(days=1))

    def __init__(self, token_type, exp_time):
        self.exp_time = exp_time
        self.token_type = token_type
        