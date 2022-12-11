import java.io.IOException;

public class ScalaServlet extends SimpleServlet {

    @Override
    public void doGet(SimpleRequest simpleRequest, SimpleResponse simpleResponse) {
        try {
            simpleResponse.write("GET: Scala...");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    @Override
    public void doPost(SimpleRequest simpleRequest, SimpleResponse simpleResponse) {
        try {
            simpleResponse.write("GET: Scala...");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

}
