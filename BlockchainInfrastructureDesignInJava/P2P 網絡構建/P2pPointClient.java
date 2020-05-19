/**
 * 
 * @author ChiangWei
 * @date 2020/5/19
 *
 */

// Represents a Uniform Resource Identifier (URI) reference.
import java.net.URI;
// Checked exception thrown to indicate that a string could not be parsed as a URI reference.
import java.net.URISyntaxException;
import java.util.ArrayList;
import java.util.List;

// The PostConstruct annotation is used on a method that needs to be executed after dependency injection is done to perform any initialization.
import javax.annotation.PostConstruct;

// Interface WebSocket
import org.java_websocket.WebSocket;
// A subclass must implement at least onOpen, onClose, and onMessage to be useful.
import org.java_websocket.client.WebSocketClient;
// Interface ServerHandshake
import org.java_websocket.handshake.ServerHandshake;

//The org.slf4j.Logger interface is the main user entry point of SLF4J API. It is expected that logging takes place through concrete implementations of this interface.
import org.slf4j.Logger;
//The LoggerFactory is a utility class producing Loggers for various logging APIs, most notably for log4j, logback and JDK 1.4 logging.
import org.slf4j.LoggerFactory;

//@Order defines the sort order for an annotated component.
import org.springframework.core.annotation.Order;
//Indicates that an annotated class is a "component".
import org.springframework.stereotype.Component;

//Testing framework for Java
import org.testng.util.Strings;

// 基於 Spring Boot 2.0 的 WebSocket 客戶端
@Component
public class P2pPointClient {
	
	// 日誌紀錄
	private Logger logger = LoggerFactory.getLogger(P2pPointClient.class);
	
	// P2P 網絡中的節點既是服務端，又是客戶端。作為服務端運行在 7001 端口(P2pPointServer 的 port 字段)，同時作為客戶通過 ws://localhost:7001 連接到服務端
	private String wsUrl = "ws://localhost:7001/";
	
	// 所有客戶端 WebSocket 的連接池緩存
	private List<WebSocket> localSockets = new ArrayList<>();
	
	public List<WebSocket> getLocalSockets() {
		return localSockets;
	}
	
	public void setLocalSockets(List<WebSocket> localSockets) {
		this.localSockets = localSockets;
	}
	
	/**
	 * 連接到服務端
	 */
	@PostConstruct
	@Order(2)
	public void connectPeer() {
		try {
			// 創建 WebSocket 的客戶端
			final WebSocketClient socketClient = new WebSocketClient(new URI(wsUrl)) {

				@Override
				public void onClose(int arg0, String arg1, boolean arg2) {
					logger.info("北京客戶端關閉");
					localSockets.remove(this);
				}

				@Override
				public void onError(Exception arg0) {
					logger.info("北京客戶端報錯");
					localSockets.remove(this);
				}

				@Override
				public void onMessage(String msg) {
					logger.info("北京客戶端收到北京服務端發送的消息: " + msg);
				}

				@Override
				public void onOpen(ServerHandshake serverHandshake) {
					sendMessage(this, "北京客戶端成功創建客戶端");
					
					localSockets.add(this);
				}
				
			};
			
			// 客戶端開始連接服務器
			socketClient.connect();
		} catch (URISyntaxException e) {
			logger.info("北京連接錯誤: " + e.getMessage());
		}
	}
	
	/**
	 * 向服務端發送消息，當前 WebSocket 的遠程 Socket 地址就是服務端
	 * 
	 * @param ws
	 * @param message
	 */
	public void sendMessage(WebSocket ws, String message) {
		logger.info("發送給" + ws.getRemoteSocketAddress().getPort() + "的 p2p 消息: " + message);
		ws.send(message);
	}
	
	/**
	 * 向所有連接過的服務端廣播消息
	 * 
	 * @param message: 待廣播的消息
	 */
	public void broadcast(String message) {
		if (localSockets.size() == 0 || Strings.isNullOrEmpty(message)) {
			return;
		}
		logger.info("Glad to say broadcast to servers being startted!");
		for (WebSocket socket : localSockets) {
			this.sendMessage(socket, message);
		}
		logger.info("Glad to say broadcast to servers has overred!");
	}
	
}
