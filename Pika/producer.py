"""
Producer 發佈 100 則訊息 (字串 0 ~ 99) 至名稱叫 hello 的 Queue。
"""

# 匯入 pika 庫，用於與 RabbitMQ 消息代理進行交互
import pika

# 設定用戶認證資訊
credentials = pika.PlainCredentials('root', '1234')

# 設定連接 RabbitMQ 所需的參數，
# RabbitMQ 服務器的主機地址，這裡設為本地主機，
# RabbitMQ 服務器的連接端口，默認為 5672，
# 使用之前設定的用戶認證。
parameters = pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials)

# 建立與 RabbitMQ 服務器的連接
connection = pika.BlockingConnection(parameters)

# 創建一個通道
channel = connection.channel()

# 宣告一個名為 'hello' 的消息佇列
channel.queue_declare(queue='hello')

# 發布 100 個消息到 'hello' 佇列
for i in range(100):
    # 將數字轉換為字串，作為消息內容
    msg = str(i).encode('utf-8')
    # 使用 channel.basic_publish 方法發布消息，
    # exchange 參數為空字串，表示直接將消息發布到指定的 queue (佇列)，
    # routing_key 參數為 'hello'，表示指定消息的路由鍵為 'hello'，這裡直接將消息發送到 'hello' 佇列，
    # body 參數為消息的內容。
    channel.basic_publish(exchange='', routing_key='hello', body=msg)
    # 輸出已發布的消息內容
    print(f" [x] Sent '{msg}'")

# 關閉與 RabbitMQ 服務器的連接
connection.close()
