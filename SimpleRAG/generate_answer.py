import requests  # 用於發送 HTTP 請求到 Ollama 的 API
import json  # 用於讀取檢索結果檔案


# Ollama Completion API
OLLAMA_COMPLETION_API = "http://localhost:11434/api/generate"


def generate_answer_with_ollama(query, context_docs, temperature=0.7):
    """
    使用 Ollama 結合上下文生成回答
    :param query: 用戶的查詢
    :param context_docs: 檢索到的文檔上下文
    :param temperature: 生成模型的隨機性參數
    :return: 生成的回答
    """

    # 拼接上下文內容
    context = "\n\n".join([doc["content"] for doc in context_docs])
    prompt = f"Context:\n{context}\n\nQuestion:\n{query}\n\nAnswer:"

    # 發送請求到 Ollama 的生成 API
    response = requests.post(
        OLLAMA_COMPLETION_API,
        json={
            "model": "gemma2:2b",       # 使用的生成模型
            "prompt": prompt,          # 提示文本
            "temperature": temperature,  # 隨機性參數
            "stream": False
        }
    )

    response.raise_for_status()  # 如果請求失敗則引發 HTTP 錯誤

    return response.json()["response"]  # 返回生成的回答


# 從檔案讀取檢索結果
with open("search_results.json", "r") as f:
    search_results = json.load(f)


# 用戶查詢
query = "What happened to OpenAI's CEO?"


# 生成回答
answer = generate_answer_with_ollama(query, search_results, temperature=0.5)
print("Answer:", answer)  # 輸出生成的回答
