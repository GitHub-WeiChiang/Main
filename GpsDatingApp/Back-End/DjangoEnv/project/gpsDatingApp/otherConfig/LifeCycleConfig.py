from enum import IntEnum

class LifeCycleConfig(IntEnum):
    # 3 times
    RESERVATION_VERIFY_TIMES_LIMIT = 3,
    # 5 min
    RESERVATION_VERIFY_CODE_TIME_LIMIT = 60 * 5,

    # 2 times
    CREATE_ACCOUNT_VERIFY_TIMES_LIMIT = 2,
    # 2 min
    CREATE_ACCOUNT_VERIFY_CODE_TIME_LIMIT = 60 * 2,

    # 2 times
    LOGIN_ACCOUNT_VERIFY_TIMES_LIMIT = 2,
    # 2 min
    LOGIN_ACCOUNT_VERIFY_CODE_TIME_LIMIT = 60 * 2,

    # 12 hr
    JWT_ACCESS_TOKEN_TIME_LIMIT = 60 * 60 * 12,
    # 30 day
    JWT_REFRESH_TOKEN_TIME_LIMIT = 60 * 60 * 24 * 30,

    # 12 s
    GAME_CONSUMER_RECEIVE_INR_TIME_LIMIT = 12,

    # 10 s
    CHAT_CONSUMER_RECEIVE_INR_TIME_LIMIT = 10,

    # 6 hr
    INFO_TYPE_REDIS_DATA_LIFE_CYCLE = 60 * 60 * 6,

    # 24 hr
    ENDURE_TYPE_REDIS_DATA_LIFE_CYCLE = 60 * 60 * 24,

    # 60 s
    WS_VERIFY_CODE_TIME_LIMIT = 60,