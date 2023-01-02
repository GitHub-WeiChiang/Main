Chapter14 深入 Controller
=====
* ### Servlet 物件實例生命週期由容器管控。
    * ### 載入 Class: 根據 web.xml 或 annotation 定義載入，並給予 URL 供客戶端呼叫。
    * ### 產生 Object: 每一個 Servlet Class 只會生成一個 Instance (2.4 版之後)，供客戶端的多個 thread 進行執行 (需注意多執行緒問題)。
    * ### 呼叫 init(ServletConfig) 方法 (只會呼叫一次): 容器將主動呼叫 Servlet Instance 的 init 方法傳遞 web.xml 上的參數 (可透過下述方式取得)，此方法可以拋出兩種例外，分別為 ServletException 與 UnavailableException (表示暫時無法使用)。
    ```
    super.getServletConfig().getInitParameter("paramName");
	super.getInitParameter("paramName");
    ```
    * ### 呼叫 service() 方法: 當收到客戶端請求時會被呼叫，並同時傳入 request 與 response 物件，每一個客戶端請求都是一個獨立的 thread，所以需要注意多執行緒安全問題。
    * ### 呼叫 destory() 方法: 當容器要被關閉時，會呼叫每一個 Servlet 的 destory 方法，可以透過覆寫進行特殊資源 (resources) 的釋放 (release)。
* ### Java EE 5 導入 Annotation 用於標註被容器管理的元件 (Servlet, Filter, Listener)，也可用於依賴注入 (dependency injection)。
* ### 依賴注入: 依賴注入是指「被依賴物件透過外部注入至依賴物件的程式中使用」，也就是被依賴物件並不是在依賴物件的程式中使用 new 產生，而是從外部「注入(inject)」至依賴物件。
* ### CDI (Contexts and Dependency Injection 上下文依賴注入)，是 Java 官方提供的依賴注入實現。
* ### 依賴注入與CDI
    * ### \@Inject 注解
    ```
    // 字段依賴注入
    public class Simple {
        @Inject
        private Demo demo;
    }

    // 構造函數依賴注入
    public class Simple {
        private Demo demo;

        @Inject
        public Simple(Demo demo) {
            this.demo = demo;
        }
    }

    // 通過 setter 方法進行依賴注入
    public class Simple {
        private Demo demo;

        @Inject
        public void setDemo(Demo demo) {
            this.demo = demo;
        }
    }
    ```
    * ### \@Named 注解
    ```
	public interface DemoService{
		public void demoTest();
	}
	
	@Named("demoService_A_impl")
	public class DemoService_A_impl implements DemoService{
		@Override
		public void demoTest(){}
	}
	
	@Named("demoService_B_impl")
	public class DemoService_B_impl implements DemoService{
		@Override
		public void demoTest(){}
	}
	
	public class UseDemo{
		@Inject
		@Named("demoService_B_impl")
		private DemoService demoService;
		
		public void doSomething(){
			demoService.demoTest();
		}
	}
    ```
* ### Java EE 5 導入 annotation 用於標註被容器管理的元件，主要是 Servlet, Filter 和 Listener。
* ### 生命週期相關 annotation
    * ### @PostConstruct: 在 init() 前被調用。
    * ### @PreDestroy: 在 destroy() 後被調用。
* ### 過濾器 (Filter): 容器的 Servlet 框架可以在 service() 方法中攔截 (intercept) 請求 (request) 與回應 (response)，也就是說 Filter 在正常流程外進行預先處理 (pre-processing) 與事後處理 (post-processing)。
* ### Filter 作業程序 (當容器收到前端請求後)
    * ### 啟動 request 預先處理。
    * ### 檢查 URL 是否滿足 Filter 的設定。
    * ### 找出符合的 Filter 並執行。
    * ### 若有其它符合的 Filter 將一併發動。
    * ### 若沒有發生錯誤則將 request 送到相應 Servlet。
    * ### Servlet 將 response 回傳給前端。
    * ### 按處理 request 的 Filter 順序相反處理 response。
    * ### 回傳 response。
* ### Filter 用途
    * ### 決定資源是否可以被存取。
    * ### 稽核 request。
    * ### 壓縮 response 資料串流。
    * ### 修改與轉換 response 內容。
    * ### 測量與記錄個別 Servlet 效能。
* ### 針對分派的 request 與 response 套用過濾。
```
RequestDispatcher rd = request.getRequestDispatcher(path);
rd.include(request, response);
rd.forward(request, response);
```
* ### FilterChain 接口的 doFilter 方法用於通知 Web 容器把請求交給 Filter 鏈中的下一個 Filter 去處理，如果當前調用此方法的 Filter 對像是Filter 鏈中的最後一個 Filter，那麼將把請求交給目標 Servlet 程序去處理。
* ### 使用 web.xml 宣告過濾器
```
<filter>
    <filter-name>perfFilter</filter-name>
    <filter-class>course.c09.PerformanceFilter</filter-class>
    <async-supported>true</async-supported>
    <init-param>
        <param-name>Log Entry Prefix</param-name>
        <param-value>Performance: </param-value>
    </init-param>
</filter>
<filter-mapping>
    <filter-name>perfFilter</filter-name>
    <url-pattern>/*</url-pattern>
</filter-mapping>
```
* ### <url-pattern> 優先序大於 <servlet-name>，其餘按照宣告順序決定。
* ### Java EE 6 使用新機制簡化使用 multipart 表單上傳資料的不便。
    * ### 新增 getPart(String) 方法，以集合形式取得所有內容，支援迭代取出。
    * ### 新增 javax.servlet.annotation.MultipartConfig，提供多種設定 (檔案儲存位置 location、檔案大小上限 maxFileSize)。
    * ### 新增 getInputStream() 取得輸入串流後再轉化為字串或檔案。
    ```
    <%@page contentType="text/html;charset=UTF-8"%>
    <form action="${pageContext.request.contextPath}/upload" enctype="multipart/form-data" method="post">
        <p>
            Description: <input type="text" name="desc" />
        </p>
        <p>
            File: <input type="file" name="data" size="50" />
        </p>
        <input type="submit" value="Upload" />
    </form>


    @WebServlet(name = "Upload", urlPatterns = { "/upload" })
    @MultipartConfig(location = "D:/uploaded", maxFileSize = 1024 * 1024 * 100)
    public class UploadServlet extends HttpServlet {
        private static final long serialVersionUID = 1L;

        @Override
        protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
            // deal with input text
            Part p1 = request.getPart("desc");
            BufferedReader r = new BufferedReader(new InputStreamReader(p1.getInputStream()));
            String desc = r.readLine();

            ...

            // deal with uploaded file
            Part p2 = request.getPart("data");
            // 將檔案寫入 MultipartConfig 的 location 所定義位置
            p2.write(getFileName(p2));
            
            ...
        }

        private String getFileName(final Part part) {
            ...
        }
    }
    ```
<br />
