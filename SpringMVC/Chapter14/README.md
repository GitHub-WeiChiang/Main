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
<br />
