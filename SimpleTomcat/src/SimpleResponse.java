import java.io.IOException;
import java.io.OutputStream;
import java.io.PrintWriter;

public class SimpleResponse {

    private final OutputStream outputStream;

    public SimpleResponse(OutputStream outputStream) {
        this.outputStream = outputStream;
    }

    public void write(String content) throws IOException {
//        String httpResponse = "HTTP/1.1 200 OK\n" +
//                "Content-Type: text/html\n" +
//                "\r\n" +
//                "<html><body>" +
//                content +
//                "</body></html>";
//
//        outputStream.write(httpResponse.getBytes());
//        outputStream.flush();
//        outputStream.close();

        // 高級字符流
        PrintWriter printWriter = new PrintWriter(outputStream);

        printWriter.write("HTTP/1.1 200 OK\r\n");
        printWriter.write("Content-Type:text/html;charset=UTF-8\r\n");
        printWriter.write("\r\n");
        printWriter.write("<html>\r\n");
        printWriter.write("    <body>\r\n");
        printWriter.write("        " + content + "\r\n");
        printWriter.write("    </body>\r\n");
        printWriter.write("</html>\r\n");

        // 衝呀！ (清空流管道)
        printWriter.flush();

        printWriter.close();
    }

}
