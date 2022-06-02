import threading
lock = threading.Lock()

class HttpRequestMethodInspectSingleton():

    __instance: object = None
    __isFirstInit: bool = False

    def __new__(cls):
        if not cls.__instance:
            with lock:
                if not cls.__instance:
                    HttpRequestMethodInspectSingleton.__instance = super().__new__(cls)
        return cls.__instance
    
    def __init__(self):
        if not self.__isFirstInit:
            HttpRequestMethodInspectSingleton.__isFirstInit = True

    def inspect(self, request) -> bool:
        # 檢查是否為 POST
        if request.method != "POST":
            return False

        # Making sure a request is AJAX
        if request.headers.get('x-requested-with') != 'XMLHttpRequest':
            return False

        return True
