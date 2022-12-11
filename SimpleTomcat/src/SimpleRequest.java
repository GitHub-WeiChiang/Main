import java.io.IOException;
import java.io.InputStream;

public class SimpleRequest {

    private final String url;
    private final String method;

    public SimpleRequest(InputStream inputStream) throws IOException {
        String httpRequest = "";

        byte[] httpRequestBytes = new byte[1024];

        // Reads some number of bytes from the input stream and stores them into the buffer array "httpRequestBytes".
        // Variable "length" is the total number of bytes read into the buffer.
        int length = inputStream.read(httpRequestBytes);

        if (length > 0) {
            httpRequest = new String(httpRequestBytes, 0, length);
        }

        String httpHead = httpRequest.split("\n")[0];

        // The string "\s" is a regular expression that means "whitespace".
        this.method = httpHead.split("\\s")[0];
        this.url = httpHead.split("\\s")[1];
    }

    public String getMethod() {
        return this.method;
    }

    public String getUrl() {
        return this.url;
    }

}
