import psycopg2
import requests

import json


# PGVector 連接配置
DB_CONFIG = {
    "dbname": "postgres",
    "user": "postgres",
    "password": "Aa123456",
    "host": "localhost",
    "port": 5432,
}


# Ollama 嵌入 API
OLLAMA_EMBEDDING_API = "http://localhost:11434/api/embeddings"


def get_embedding_ollama(text):
    """
    使用 Ollama 的嵌入模型生成文本的向量嵌入
    :param text: 待生成嵌入的文本
    :return: 嵌入向量
    """

    response = requests.post(
        OLLAMA_EMBEDDING_API,
        json={"model": "nomic-embed-text:latest", "prompt": text}
    )

    response.raise_for_status()  # 如果請求失敗則引發錯誤
    return response.json()["embedding"]  # 提取嵌入向量


def search_documents(query, top_k=3):
    """
    使用向量檢索方法查找與用戶查詢最相關的文檔
    :param query: 用戶的查詢
    :param top_k: 返回最相關的文檔數量
    :return: 包含文檔內容和距離的列表
    """
    
    connection = psycopg2.connect(**DB_CONFIG)  # 連接到資料庫
    cursor = connection.cursor()

    # 為用戶查詢生成嵌入向量
    query_embedding = get_embedding_ollama(query)

    # 使用 SQL 查詢語句進行向量檢索，強制轉換類型為 VECTOR
    cursor.execute(
        """
        SELECT content, embedding <-> %s::vector AS distance
        FROM documents
        ORDER BY distance ASC
        LIMIT %s;
        """,
        (query_embedding, top_k)
    )

    # 提取結果並關閉連接
    results = cursor.fetchall()
    cursor.close()
    connection.close()

    # 返回檢索結果的字典列表
    return [{"content": result[0], "distance": result[1]} for result in results]


# 檢索並保存結果
query = "What happened to OpenAI's CEO?"  # 用戶的查詢
results = search_documents(query)


# 保存檢索結果到檔案
with open("search_results.json", "w") as f:
    json.dump(results, f, indent=4)


print("Search results saved to search_results.json")
