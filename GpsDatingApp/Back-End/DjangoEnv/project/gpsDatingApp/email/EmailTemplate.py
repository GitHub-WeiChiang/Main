from enum import IntEnum, unique

@unique
class EmailTemplate(IntEnum):
    RESERVATION_SUCCESS = 0,
    RESERVATION_VERIFY = 1,
    REGISTER_VERIFY = 2,
    LOGIN_VERIFY = 3
