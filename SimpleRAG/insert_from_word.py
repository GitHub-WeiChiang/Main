import requests
import psycopg2

from docx import Document


# PGVector 連接配置
DB_CONFIG = {
    "dbname": "postgres",            # 資料庫名稱
    "user": "postgres",              # 資料庫用戶名
    "password": "Aa123456",          # 資料庫密碼
    "host": "localhost",             # 資料庫主機地址
    "port": 5432,                    # 資料庫連接埠
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


def split_into_chunks(text, chunk_size):
    """
    將文本按指定大小分割為多個段
    :param text: 文本
    :param chunk_size: 每個段的最大字符數
    :return: 分割後的文本段列表
    """

    chunks = []

    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i + chunk_size])
    
    return chunks


def insert_documents_from_word(file_path, chunk_size=500):
    """
    從 Word 文件讀取內容，分段後插入 PGVector
    :param file_path: Word 文件的路徑
    :param chunk_size: 每個文本段的最大字符數
    """

    # 打開 Word 文件並讀取段落內容
    doc = Document(file_path)
    paragraphs = [paragraph.text for paragraph in doc.paragraphs if paragraph.text.strip()]  # 過濾掉空段落

    # 連接到 PGVector 資料庫
    connection = psycopg2.connect(**DB_CONFIG)
    cursor = connection.cursor()

    for paragraph in paragraphs:
        chunks = split_into_chunks(paragraph, chunk_size)  # 將段落按 chunk_size 分段

        for chunk in chunks:
            embedding = get_embedding_ollama(chunk)  # 為每個段生成嵌入

            cursor.execute(
                "INSERT INTO documents (content, embedding) VALUES (%s, %s)",
                (chunk, embedding)
            )

    # 提交更改並關閉連接
    connection.commit()
    cursor.close()
    connection.close()


# 插入文檔數據
word_file_path = "documents.docx"  # 替換為你的 Word 文件路徑
insert_documents_from_word(word_file_path, chunk_size=300)
print("Documents inserted successfully with chunks.")
