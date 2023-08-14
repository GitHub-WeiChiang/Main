02 - 安裝與啟動
=====
* ### MongoDB Server
    ```
    brew tap mongodb/brew

    brew update

    brew install mongodb-community@6.0
    ```
    ```
    brew services list
    ```
    ```
    brew services start mongodb-community@6.0

    brew services stop mongodb-community@6.0
    ```
    ```
    mongosh
    ```
* ### MongoDB Compass
    ```
    brew install --cask mongodb-compass
    ```
* ### PyMongo
    ```
    pip install pymongo
    ```
<br />
