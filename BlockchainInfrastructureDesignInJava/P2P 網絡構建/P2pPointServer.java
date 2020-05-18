/**
 * 
 * @author ChiangWei
 * @date 2020/5/13
 *
 */

// This class implements an IP Socket Address (IP address + port number) It can also be a pair (hostname + port number), in which case an attempt will be made to resolve the hostname. If resolution fails then the address is said to be unresolved but can still be used on some circumstances like connecting through a proxy.
import java.net.InetSocketAddress;
import java.util.ArrayList;
import java.util.List;

// The PostConstruct annotation is used on a method that needs to be executed after dependency injection is done to perform any initialization.
import javax.annotation.PostConstruct;

// Interface WebSocket
import org.java_websocket.WebSocket;
// Interface ClientHandshake
import org.java_websocket.handshake.ClientHandshake;
// WebSocketServer is an abstract class that only takes care of the HTTP handshake portion of WebSockets. It's up to a subclass to add functionality/purpose to the server.
import org.java_websocket.server.WebSocketServer;

// The org.slf4j.Logger interface is the main user entry point of SLF4J API. It is expected that logging takes place through concrete implementations of this interface.
import org.slf4j.Logger;
// The LoggerFactory is a utility class producing Loggers for various logging APIs, most notably for log4j, logback and JDK 1.4 logging.
import org.slf4j.LoggerFactory;

// @Order defines the sort order for an annotated component.
import org.springframework.core.annotation.Order;
// Indicates that an annotated class is a "component".
import org.springframework.stereotype.Component;

//Testing framework for Java
import org.testng.util.Strings;

// 基於 Spring Boot 的 WebSocket 服務端
@Component
public class P2pPointServer {
	
	// 日誌紀錄
	private Logger logger = LoggerFactory.getLogger(P2pPointServer.class);
	
	// 本機 Server 的 WebSocket 端口
	// 多機測試時可以改變該值
	private int port = 7001;
	
	// 所有連接到服務端的 WebSocket 緩存器
	private List<WebSocket> localSockets = new ArrayList<>();
	
	public List<WebSocket> getLocalSockets() {
		return localSockets;
	}
	
	public void setLocalSockets(List<WebSocket> localSockets) {
		this.localSockets = localSockets;
	}
	
	/**
	 * 初始化 P2P Server 端
	 * 
	 * @param Server 端的端口號 port
	 */
	// 為保證 initServer() 在服務啟動時就能加載，用 @PostConstruct 標記使其在服務器加載 bean 的時候運行，並且只會被服務器執行一次。
	@PostConstruct
	// 為保證服務端先於客戶端加載，用 @Order(1) 標示 initServer()
	@Order(1)
	public void initServer() {
		/**
		 * 初始化 WebSocket 的服務端定義內部類對象 socketServer, 源於 WebSocketServer
		 * InetSocketAddress(port) 是 WebSocketServer 構造器的參數，InetSocketAddress 是(IP 地址 + 端口號)類型，即端口地址類型。
		 */
		final WebSocketServer socketServer = new WebSocketServer(new InetSocketAddress(port)) {
			/**
			 * 重寫 5 個事件方法，事件發生時觸發對應的方法
			 */
			
			@Override
			// 斷開連接時候觸發
			public void onClose(WebSocket webSocket, int i, String s, boolean b) {
				logger.info(webSocket.getRemoteSocketAddress() + "客戶端與服務器斷開連接!");
				
				// 當客戶端斷開連接時，WebSocket 連接池刪除該連接
				localSockets.remove(webSocket);
			}

			@Override
			// 連接發生錯誤時調用，緊接著觸發 onClose 方法
			public void onError(WebSocket webSocket, Exception e) {
				logger.info(webSocket.getRemoteSocketAddress() + "客戶端鏈接錯誤!");
				localSockets.remove(webSocket);
			}

			@Override
			// 收到客戶端發來的消息時觸發
			public void onMessage(WebSocket webSocket, String msg) {
				logger.info("北京服務端接收到客戶端消息: " + msg);
				sendMessage(webSocket, "收到消息");
			}

			@Override
			// 創建連接成功時觸發
			public void onOpen(WebSocket webSocket, ClientHandshake clientHandshake) {
				sendMessage(webSocket, "北京服務端成功連接");
				
				// 當成功創建一個 WebSocket 連接時，將該連接加入連接池
				localSockets.add(webSocket);
			}

			@Override
			// 服務端啟用時調用
			public void onStart() {
				logger.info("北京的 WebSocket Server 端啟動...");
			}
			
		};
		
		socketServer.onStart();
		logger.info("北京服務端監聽 socketServer 端口: " + port);
	}
	
	/**
	 * 向連接到本機的某個客戶端發送消息
	 * 
	 * @param ws
	 * @param message
	 */
	public void sendMessage(WebSocket ws, String message) {
		logger.info("發送給" + ws.getRemoteSocketAddress().getPort() + "的 p2p 消息是: " + message);
		ws.send(message);
	}
	
	/**
	 * 向所有連接到本機的客戶端廣播消息
	 * 
	 * @param message: 待廣播內容
	 */
	public void broadcast(String message) {
		if (localSockets.size() == 0 || Strings.isNullOrEmpty(message)) {
			return;
		}
		
		logger.info("Glad to say broadcast to clients being startted!");
		for (WebSocket socket : localSockets) {
			this.sendMessage(socket, message);
		}
		logger.info("Glad to say broadcast to clients has overred!");
	}
	
}
