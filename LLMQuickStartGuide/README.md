LLMQuickStartGuide
=====
* ### This is a Quick Start Guide that documents how to deploy a Knowledge Based QA (KBQA, Knowledge Base Question Answering) system based on the LLM (Large Language Model) in an offline environment using Docker.
* ### Architecture: MaxKB -> Ollama -> Meta Llama 3 (8B)。
* ### Basic commands for Ollama
    ```
    # Pull a model.

    ollama pull llama3:8b
    ```
    ```
    # Run a model (interactive mode).

    ollama run llama3:8b
    ```
    ```
    # Remove a model.

    ollama rm llama3:8b
    ```
    ```
    # Copy a model.

    ollama cp llama3:8b my-llama3:8b
    ```
    ```
    # List models currently hosted.

    ollama list
    ```
    ```
    # Start a server.

    ollama serve
    ```
* ### Other commands for Ollama
    ```
    # Start the server.

    ./ollama serve
    ```
    ```
    # In a separate shell.

    ./ollama run llama3
    ```
* ### REST API for Ollama
    ```
    # Generate a response.

    curl http://localhost:11434/api/generate -d '{
        "model": "llama3",
        "prompt":"Why is the sky blue?"
    }'
    ```
    ```
    # Chat with a model.

    curl http://localhost:11434/api/chat -d '{
        "model": "llama3",
        "messages": [
            { "role": "user", "content": "why is the sky blue?" }
        ]
    }'
    ```
* ### Ollama Docker Image
    ```
    # CPU only.

    docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
    ```
    ```
    # Run model locally.

    docker exec -it ollama ollama run llama3:8b
    ```
    * ### Note: To execute basic commands targeting the Ollama container running in Docker, need to prepend it with the prefix ```docker exec -it ollama ...``` ("..." stands for Basic commands for Ollama).
* ### MaxKB Quick Start
    ```
    docker run -d --name=maxkb -p 8080:8080 -v ~/.maxkb:/var/lib/postgresql/data 1panel/maxkb

    # Account: admin
    # Password: MaxKB@123..
    # Access Ollama: http://host.docker.internal:11434
    ```
* ### Migration of Images in Docker
    ```
    # Save.

    docker save IMAGE_NAME -o IMAGE_NAME.tar
    ```
    ```
    # Load.

    docker load -i IMAGE_NAME.tar
    ```
* ### Migration of Volumes in Docker
    ```
    # Backup.

    docker run --rm -v VOLUME_NAME:/volume busybox sh -c 'tar -cOzf - /volume' > volume-export.tgz
    ```
    ```
    # Restore.

    docker run --rm -i -v VOLUME_NAME:/volume busybox sh -c "tar -xzvf - -C /" < volume-export.tgz
    ```
    * ### Note: Busybox is merely an intermediary image and container, theoretically replaceable with any similarly lightweight Docker application.
    * ### Note: Can achieve Volume Migration more conveniently using Volumes Backup & Share, refer to the reference below for more information.
<br />

Steps for Offline Deployment by Docker
=====
* ### On a computer with internet access:
    * ### Download and install Docker Desktop.
    * ### Run the Ollama application in Docker and download an appropriate LLM model.
    * ### Run the MaxKB application in Docker and attempt to access Ollama.
    * ### Prepare the ```Image``` of busybox in Docker.
    * ### Save the ```Image(s)``` of the Ollama and MaxKB applications.
    * ### Backup the ```Volume``` of the Ollama application through busybox.
* ### Find a way to bring the following files into a computer that cannot access the internet:
    * ### Docker Desktop installer
    * ### ```Image``` of Ollama
    * ### ```Image``` of MaxKB
    * ### ```Image``` of busybox
    * ### ```Volume``` of Ollama (which is the LLM model)
* ### In a computer that cannot access the Internet:
    * ### Install Docker Desktop (Pay attention to WSL update issues).
    * ### Load the ```Image``` of the Ollama application.
    * ### Load the ```Image``` of the MaxKB application.
    * ### Load the ```Image``` of the busybox application.
    * ### Run the ```Image``` of Ollama as a ```Container```.
    * ### Run the ```Image``` of MaxKB as a ```Container```.
    * ### Restore the ```Volume``` of Ollama.
    * ### Enjoy using it !
<br />

Reference
=====
* ### Ollama -> [click me](https://ollama.com/)
* ### Ollama GitHub -> [click me](https://github.com/ollama/ollama)
* ### Ollama Docker -> [click me](https://hub.docker.com/r/ollama/ollama)
* ### MaxKB GitHub -> [click me](https://github.com/1Panel-dev/MaxKB)
* ### Volumes Backup & Share -> [click me](https://hub.docker.com/extensions/docker/volumes-backup-extension)
<br />
