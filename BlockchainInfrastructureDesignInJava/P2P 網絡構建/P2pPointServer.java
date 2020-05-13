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

}
