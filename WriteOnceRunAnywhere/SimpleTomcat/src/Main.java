import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;

public class Main {

    public static void main(String[] args) {
        // 自己的小服務器
        try (ServerSocket serverSocket = new ServerSocket(48763)){
            System.out.println("小服務器來摟");

            // 等待客戶端訪問
            Socket socket = serverSocket.accept();
            System.out.println("有人連接我摟");

            /* ----- 讀取請求 ----- */
            // 低級字節流 (輸入流)
            InputStream inputStream = socket.getInputStream();
            // 高級字符流
            BufferedReader bufferedReader = new BufferedReader(
                    // 字節字符轉換流
                    new InputStreamReader(inputStream)
            );
            // 讀取資源
            String string = bufferedReader.readLine();
            System.out.println(string);

            /* ----- 回寫響應 ----- */
            // 低級字節流 (輸出流)
            OutputStream outputStream = socket.getOutputStream();
            // 高級字符流
            PrintWriter printWriter = new PrintWriter(outputStream);

            printWriter.write("HTTP1.1 200 OK\r\n");
            printWriter.write("Content-Type:text/html;charset=UTF-8\r\n");
            printWriter.write("\r\n");
            printWriter.write("<html>\r\n");
            printWriter.write("    <body>\r\n");
            printWriter.write("        <input type='button' value='點我！'>\r\n");
            printWriter.write("    </body>\r\n");
            printWriter.write("</html>\r\n");

            // 衝呀！ (清空流管道)
            printWriter.flush();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

}
