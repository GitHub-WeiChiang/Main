import java.io.IOException;

public class JavaServlet extends SimpleServlet{

    @Override
    public void doGet(SimpleRequest simpleRequest, SimpleResponse simpleResponse) {
        try {
            simpleResponse.write("GET: Java...");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    @Override
    public void doPost(SimpleRequest simpleRequest, SimpleResponse simpleResponse) {
        try {
            simpleResponse.write("POST: Java...");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

}
