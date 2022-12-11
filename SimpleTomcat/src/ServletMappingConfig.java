import java.util.HashMap;
import java.util.Map;

public class ServletMappingConfig {

    private final Map<String, SimpleServlet> servletMapping = new HashMap<>();

    public ServletMappingConfig() {
        servletMapping.put("/java", new JavaServlet());
        servletMapping.put("/scala", new ScalaServlet());
    }

    public SimpleServlet getServlet(String url) {
        return servletMapping.get(url);
    }

}
