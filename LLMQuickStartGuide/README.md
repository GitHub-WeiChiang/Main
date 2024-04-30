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
    # Remove a model
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
* ### Migration of Images and Containers in Docker
    * ### Image
<br />
