Chapter16 非同步的 Servlet 和 AJAX
=====
* ### acceptCount 和 maxThreads (配置於 server.xml)
    * ### acceptCount: tomcat 启动的线程数达到最大时，接受排队的请求个数，默认值为 100。
    * ### maxThreads: tomcat 启动的最大线程数，即同时处理的任务个数，默认值为 200。
    * ### 情况1: 接受一个请求，此时 tomcat 起动的线程数没有到达 maxThreads，tomcat 会起动一个线程来处理此请求。
    * ### 情况2: 接受一个请求，此时 tomcat 起动的线程数已经到达 maxThreads，tomcat 会把此请求放入等待队列，等待空闲线程。
    * ### 情况3: 接受一个请求，此时 tomcat 起动的线程数已经到达 maxThreads，等待队列中的请求个数也达到了 acceptCount，此时 tomcat 会直接拒绝此次请求，返回 connection refused。
* ### 如果因為某一個 request 耗費時間較長而綁定一個 thread，這樣不優啦。
* ### Servlet API 提供 AsyncContext 進行接力。
* ### 實作步驟
    * ### 撰寫一個實作 ServletContextListener 類別，取得實例化的 Executors.newCachedThreadPool() 並放入 ServletContext。
    * ### 在對應的 Servlet 宣告使用非同步技術
    ```
    @WebServlet(asyncSupported = true)

    // 开启异步组件
    AsyncContext asyncCtx = request.startAsync();
    // 添加 AsyncListener 的监听器，当超时、完成、出错会回调这里面的方法
    asyncCtx.addListener(new AppAsyncListener());
    // 设置超时时间
    asyncCtx.setTimeout(9000);

    ExecutorService es = (ExecutorService) request.getServletContext().getAttribute("threads");
    es.execute(new AsyncRequestProcessor(asyncCtx));
    ```
* ### AJAX, Asynchronous JavaScript and XML: 更新部分資訊。
* ### JsonObject
```
import com.google.gson.JsonArray;
import com.google.gson.JsonObject;
import com.google.gson.JsonPrimitive;

JsonObject json = new JsonObject();
json.add("teacher", new JsonPrimitive(teacher));
json.add("price", new JsonPrimitive(2000));
JsonArray courses = new JsonArray();
courses.add("OCAJP");
courses.add("OCPJP");
json.add("courses", courses);

System.out.println(JsonUtility.data("Jim"));

// {"teacher":"Jim","price":2000,"courses":["OCAJP","OCPJP"]}
```
<br />
