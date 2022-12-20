import java.io.InputStream;
import java.io.OutputStream;
import java.net.ServerSocket;
import java.net.Socket;

public class SimpleTomcat {

    private final int port;

    private final ServletMapping servletMapping;

    public SimpleTomcat(int port) {
        this.port = port;
        this.servletMapping = new ServletMapping();
    }

    public void start() {
        try (ServerSocket serverSocket = new ServerSocket(this.port)){
            System.out.println("SimpleTomcat is start ...");

            while (true) {
                Socket socket = serverSocket.accept();

                // 低級字節流 (輸入流)
                InputStream inputStream = socket.getInputStream();
                // 低級字節流 (輸出流)
                OutputStream outputStream = socket.getOutputStream();

                SimpleRequest simpleRequest = new SimpleRequest(inputStream);
                SimpleResponse simpleResponse = new SimpleResponse(outputStream);

                this.dispatch(simpleRequest, simpleResponse);

                socket.close();
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private void dispatch(SimpleRequest simpleRequest, SimpleResponse simpleResponse) {
        String url = simpleRequest.getUrl();

        if (url.equals("/favicon.ico")) return;

        SimpleServlet simpleServlet = this.servletMapping.getServlet(url);
        simpleServlet.service(simpleRequest, simpleResponse);
    }

    public static void main(String[] args) {
        new SimpleTomcat(48763).start();
    }

}