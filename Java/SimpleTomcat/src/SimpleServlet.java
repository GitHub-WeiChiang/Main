public abstract class SimpleServlet {

    public abstract void doGet(SimpleRequest simpleRequest, SimpleResponse simpleResponse);

    public abstract void doPost(SimpleRequest simpleRequest, SimpleResponse simpleResponse);

    public void service(SimpleRequest simpleRequest, SimpleResponse simpleResponse) {
        if (simpleRequest.getMethod().equalsIgnoreCase("POST")) {
            doPost(simpleRequest, simpleResponse);
        } else if (simpleRequest.getMethod().equalsIgnoreCase("GET")) {
            doGet(simpleRequest, simpleResponse);
        }
    }

}
