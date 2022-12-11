import java.util.HashMap;
import java.util.Map;

public class ServletMapping {

    private final Map<String, SimpleServlet> servletMapping = new HashMap<>();

    public ServletMapping() {
        servletMapping.put("/java", new JavaServlet());
        servletMapping.put("/scala", new ScalaServlet());
    }

    public SimpleServlet getServlet(String url) {
        return servletMapping.get(url);
    }

}
