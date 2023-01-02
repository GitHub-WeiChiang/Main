Chapter18 Spring 框架導論
=====
* ### DI (dependency injection): 關聯注入。
* ### Spring DI
    * ### XML-based: 使用 XML 檔案設定類別間的關聯性。
    * ### Java-based: 使用 Java 類別搭配 annotation 設定類別間的關聯性。
    * ### 以上都必須建立一個實作 ApplicationContext 介面的 Spring 框架物件，等同於 Spring 執行時期環境，再由該物件取得其它物件，通常稱為 Bean 元件。
* ### AOP (aspect-oriented programming): 面向導向程式開發，建構在 DI 上。
* ### \@Aspect: 標注類別為 Aspect 元件。
* ### \@Before: 標注方法應在何方法被調用前調用。
* ### \@After: 標注方法應在何方法被調用後調用。
* ### \@Configuration: 宣告為 Spring 的設定類別。
* ### \@EnableAspectJAutoProxy: 宣告啟用 AOP。
* ### \@Bean: 建立 Bean 元件。
* ### Spring 容器的分類
    * ### Bean Factory: 由 org.springframework.beans.factory.BeanFactory 定義，非常得純，支援基本 DI 功能。
    * ### Application Context: org.springframework.context.ApplicationContext 定義，建立在 Bean Factory 之上，提供其它服務，如發布事件 (event) 給有興趣的傾聽者 (listener)。
* ### Application Contexts 種類
    * ### AnnotationConfigApplicationContext: 藉由一個或多個 Java 設定類別載入。
    * ### AnnotationConfigWebApplicationContext: 同上，但 Spring 容器用於 web 應用程式如 Tomcat 內。
    * ### ClassPathXmlApplicationContext: 載入時指定位於 classpath 上的 XML 設定檔。
    * ### FileSystemXmlApplicationContext: 載入時指定位於作業系統上的 XML 設定檔。
    * ### XmlWebApplicationContext: 同上，但載入時指定位於 web 應用程式內的 XML 設定檔。
* ### Spring 元件生命週期
    * ### Spring 建構物件實例
    * ### Spring 注入欄位值
    * ### setBeanName()
    * ### setBeanFactory()
    * ### setApplicationContext()
    * ### postProcessBeforeInitialization()
    * ### afterPropertiesSet() / init-method
    * ### postProcessAfterInitialization()
    * ### 可以使用嘍！！
    * ### destory() / destory-method
<br />
