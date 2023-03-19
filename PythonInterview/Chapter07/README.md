Chapter07 異常處理
=====
* ### 如何自訂義異常 ?
    ```
    class CustomException(Exception):
        def __init__(self):
            self.msg = "這是一個客製化的例外"

        def __str__(self):
            return self.msg


    if __name__ == '__main__':
        try:
            raise CustomException()
        except CustomException as ce:
            print(ce)
    ```
<br />
