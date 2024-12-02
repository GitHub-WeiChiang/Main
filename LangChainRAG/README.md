LangChainRAG
=====
* ### 基於 Python 3.11.7
* ### 安裝步驟
    * ### 啟動 PGVector 容器
        1. #### 拉取並啟動 PGVector 容器
            ```
            docker pull pgvector/pgvector:pg17

            docker run --name pgvector -e POSTGRES_PASSWORD=Aa123456 -d -p 5432:5432 pgvector/pgvector:pg17
            ```
        2. ### 配置向量擴展
            ```
            docker exec -it pgvector psql -U postgres
            ```
            ```
            CREATE EXTENSION IF NOT EXISTS vector;
            CREATE TABLE documents (
                id SERIAL PRIMARY KEY,
                content TEXT,
                embedding VECTOR(768)
            );
            ```
    * ### 建立 Python venv 環境
        1. #### 建立虛擬環境
            ```
            python3 -m venv langchain_rag_env

            source langchain_rag_env/bin/activate
            ```
        2. ### 安裝必要的 Python 庫
            ```
            ...
            ```
    * ### 安裝和配置 Ollama
        ```
        ollama pull nomic-embed-text

        ollama run gemma2:2b
        ```
* ### 測試流程
    * ### 插入文檔
        ```
        python insert_from_word.py
        ```
    * ### 檢索文檔
        ```
        python search_documents.py
        ```
    * ### 生成回答
        ```
        python generate_answer.py
        ```
<br />
