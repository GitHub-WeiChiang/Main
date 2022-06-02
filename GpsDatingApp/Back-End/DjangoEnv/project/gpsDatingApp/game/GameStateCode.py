from enum import IntEnum, unique

@unique
class GameStateCode(IntEnum):
    # GameState
    READY_STATE = 0,
    JOIN_STATE = 1,
    PAIR_STATE = 2,
    BROADCAST_STATE = 3,
    FINISH_STATE = 4,

    # Successful responses
    # state code, 200
    SUCCESS = 200,

    # Client errors
    # state code, 400–451
    PARAMETER_ERROR = 400,

    VERIFY_CODE_NOT_EXIST = 401,

    VERIFY_CODE_ERROR = 403,

    # customize state code, 460-499
    JOIN_GAME_ERROR = 460,

    # Server errors
    # state code, 500-511

    # customize state code, 520-599
