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


# 定義一個回調函數，用於處理接收到的消息
def callback(ch, method, properties, body):
    # 使用 body.decode() 解碼接收到的 bytes 類型消息並輸出內容
    print(f" [x] Received {body.decode()}")


# 設定通道來消費 'hello' 佇列中的消息，
# 自動確認接收到的消息，RabbitMQ 將會從佇列中移除這些消息，
# 設定處理接收到的消息的回調函數為上面定義的 callback 函數。
channel.basic_consume(queue='hello', auto_ack=True, on_message_callback=callback)

print(' [*] Waiting for messages. To exit press CTRL+C')

try:
    # 開始持續消費 'hello' 佇列中的消息，一旦有消息到達，會調用 callback 函數進行處理
    channel.start_consuming()
except KeyboardInterrupt:
    # 如果收到 CTRL+C，停止持續消費消息
    channel.stop_consuming()

# 關閉與 RabbitMQ 服務器的連接
connection.close()
