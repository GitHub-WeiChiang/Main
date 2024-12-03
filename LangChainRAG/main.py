import os

from langchain_community.document_loaders import Docx2txtLoader  # 用於讀取 Word 文件
from langchain.text_splitter import RecursiveCharacterTextSplitter  # 用於將文本分割為小塊
from langchain.embeddings import OllamaEmbeddings  # 使用 Ollama 提供的嵌入模型
from langchain.vectorstores import PGVector  # 向量資料庫操作
from langchain.chains import RetrievalQA  # 構建檢索問答 (RAG) 鏈
from langchain.llms import Ollama  # 使用 Ollama LLM (大語言模型)


# 設定 pgvector 連接資料庫的參數
PGVECTOR_DB_CONFIG = {
    "driver": "postgresql",         # 資料庫驅動類型
    "host": "localhost",            # pgvector 資料庫伺服器地址
    "port": 5432,                   # pgvector 預設埠
    "user": "postgres",             # 資料庫用戶名
    "password": "postgres",         # 資料庫密碼
    "database": "postgres"         # pgvector 資料庫名稱
}


# Step 1: 讀取 Word 檔案並轉換為文本
def load_documents(file_path):
    """
    讀取 Word 文件並將其分割為小段文本
    :param file_path: Word 文件的路徑
    :return: 分割後的小段文本列表
    """

    loader = Docx2txtLoader(file_path)  # 使用 Docx2txtLoader 讀取 Word 文件

    documents = loader.load()  # 將 Word 文件內容讀取為文本

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)  # 設置文本分塊大小和重疊
    
    return text_splitter.split_documents(documents)  # 分割並返回文本塊


# Step 2: 建立向量資料庫
def create_vector_store(documents):
    """
    將文本嵌入並存入向量資料庫
    :param documents: 文本分塊列表
    :return: 向量資料庫實例
    """

    embeddings = OllamaEmbeddings(model="nomic-embed-text:latest")  # 使用 nomic-embed-text 生成文本嵌入

    vector_store = PGVector.from_documents(
        documents,                      # 傳入需要存儲的文檔
        embeddings,                     # 使用的嵌入模型
        connection_string=os.getenv("PGVECTOR_DB_URL")  # 透過環境變數獲取資料庫連接 URL
    )

    return vector_store  # 返回向量資料庫實例


# Step 3: 啟動問答流程
def start_qa_system(vector_store, top_k=5, temperature=0.7):
    """
    建立檢索問答系統
    :param vector_store: 向量資料庫實例
    :param top_k: 控制生成模型選擇的最有可能的前 k 個詞語
    :param temperature: 控制生成文本的隨機性
    :return: 問答系統實例
    """

    retriever = vector_store.as_retriever()  # 將向量資料庫設置為檢索器

    # 使用 gemma2:2b 模型，並設定 top_k 和 temperature 參數
    llm = Ollama(
        model="gemma2:2b",
        top_k=top_k,  # 設定 top_k
        temperature=temperature  # 設定 temperature
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm,                            # 啟用的大語言模型
        retriever=retriever             # 設置檢索器
    )

    return qa_chain  # 返回問答系統


if __name__ == "__main__":
    # 指定 Word 文件路徑
    doc_path = "documents.docx"  # 替換為您的 Word 文件實際路徑
    documents = load_documents(doc_path)  # 讀取並分割 Word 文件內容

    # 設定 pgvector 資料庫的 URL，並設為環境變數
    os.environ["PGVECTOR_DB_URL"] = (
        f"postgresql://{PGVECTOR_DB_CONFIG['user']}:{PGVECTOR_DB_CONFIG['password']}"
        f"@{PGVECTOR_DB_CONFIG['host']}:{PGVECTOR_DB_CONFIG['port']}/{PGVECTOR_DB_CONFIG['database']}"
    )

    # 建立向量資料庫並存入文本嵌入
    vector_store = create_vector_store(documents)

    # 啟動檢索問答系統，設定 top_k 和 temperature
    qa_chain = start_qa_system(vector_store, top_k=5, temperature=0.7)

    # 測試問答系統
    query = "What happened to OpenAI's CEO?"  # 測試問題
    answer = qa_chain.run(query)  # 問答系統返回答案
    print(f"Answer: {answer}")  # 打印答案
