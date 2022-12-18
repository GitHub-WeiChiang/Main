Question005 Bean 的生命週期
=====
* ### Bean 必需被設定在配置文件 applicationContext.xml 中，並透過以下方式取得。
```
ApplicationContext context = new ClassPathXmlApplicationContext("applicationContext.xml");
```
* ### 在 Spring 中，從 BeanFactory 或A pplicationContext 取得的實例為 Singleton，預設是每一個 Bean 別名維持一個實例。
* ### 亦可透過設定每次取得 Bean 時都產生一個新的實例 (singleton 屬性預設是 true)。
```
<bean id="" class="" singleton="false">
```
* ### 一個 Bean 從建立到銷毀，會歷經幾個執行階段，如果是使用 BeanFactory 來管理 Bean 的話
    * ### Bean 的建立: 由 BeanFactory 讀取 Bean 定義檔，並生成各個 Bean 實例。
    * ### 屬性注入: 執行相關的 Bean 屬性依賴注入。
    * ### BeanNameAware 的 setBeanName(): 如果 Bean 類別有實作 org.springframework.beans.factory.BeanNameAware 介面，則執行它的 setBeanName() 方法。
    * ### BeanFactoryAware 的 setBeanFactory(): 如果 Bean 類別有實作 org.springframework.beans.factory.BeanFactoryAware 介面，則執行它的 setBeanFactory() 方法。
    * ### BeanPostProcessors 的 processBeforeInitialization(): 如果有任何的 BeanPostProcessors 實例與 Bean 實例關聯，則執行 BeanPostProcessors 實例的 processBeforeInitialization() 方法。
    * ### InitializingBean 的 afterPropertiesSet(): 如果 Bean 類別有實作 org.springframework.beans.factory.InitializingBean，則執行它的 afterPropertiesSet() 方法。
    * ### Bean 定義檔中定義 init-method: 可以在 Bean 定義檔使用 init-method 屬性設定方法名稱，如果有以下設定的話，則進行至這個階段時，就會執行 initBean() 方法。
    ```
    <bean id="" class="" init-method="initBean">
    ```
    * ### BeanPostProcessors 的 processaAfterInitialization(): 如果有任何的 BeanPostProcessors 實例與 Bean 實例關聯，則執行 BeanPostProcessors 實例的 processaAfterInitialization() 方法。
    * ### DisposableBean 的 destroy(): 在容器關閉時，如果 Bean 類別有實作 org.springframework.beans.factory.DisposableBean，則執行它的 destroy() 方法。
    * ### Bean 定義檔中定義 destroy-method: 在容器關閉時，可以在 Bean 定義檔使用 destroy-method 屬性設定方法名稱，如果有以下設定的話，則進行至這個階段時，就會執行 destroyBean() 方法。
    ```
    <bean id="" class="" destroy-method="destroyBean">
    ```
* ### 如果是使用 ApplicationContext 來管理 Bean 的話，則在執行 BeanFactoryAware的setBeanFactory() 階段之後，若 Bean 有實作 org.springframework.context.ApplicationContextAware 介面，則執行其 setApplicationContext() 方法，接著才繼續進行 BeanPostProcessors 的 processBeforeInitialization() 及之後的流程。
<br />
