Question050 - Docker environment for python variables: How can I create a env variable for username & password and pass dynamic values while running containers ?
=====
* ### Sample 1
    ```
    import os

    username = os.environ['MY_USER']
    password = os.environ['MY_PASS']

    print("Running with user: %s" % username)
    ```
    ```
    docker run -e MY_USER=test -e MY_PASS=12345 ... <image-name> ...
    ```
* ### Sample 2
    ```
    username = os.getenv('USERNAME', 'test')
    ```
    ```
    # docker-compose.yml

    version: '2'
    services:
        python-container:
            image: python-image:latest
            environment:
                - USERNAME=test
                - PASSWORD=12345
    ```
<br />
