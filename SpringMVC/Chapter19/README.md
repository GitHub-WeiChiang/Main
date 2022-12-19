Chapter19 Spring DI
=====
* ### Spring 允許開發者使用 3 種方式定義 bean 縫合方式。
    * ### 自動搜尋 (automatic discovery) 與自動縫合 (automatic wiring)。
    * ### 使用 XML 設定檔明確定義。
    * ### 使用 Java annotation 明確定義。
* ### 自動化 DI 原理與核心標註。
    * ### 元件掃描 (component scanning): Spring 自動發現 ApplicationContext 內的 bean 元件。
    * ### 自動縫合 (auto wiring): Spring 自動建立 bean 元件間的關聯性 (dependency)。
* ### 使用標註類別
    * ### \@Component: 需要被 Spring 建立為 bean 物件。
    * ### \@Autowired: 執行時期自動以需要的 bean 元件縫合至建構子參數。
    * ### \@Configuration: Spring 設定檔，將建立所有 bean 物件及其關聯性。
    * ### \@ComponentScan: 自動搜尋和被標註類別在同一路徑或是所有子路徑的所有 bean 類別，建立物件並注入關聯性。
<br />
