Chapter15 深入 Model
=====
* ### 在 Servlet API 中有一个 ServletContextListener 接口，它能够监听 ServletContext 对象的生命周期，实际上就是监听 Web 应用的生命周期。
* ### 当 Servlet 容器启动或终止 Web 应用时，会触发 ServletContextEvent 事件，该事件由 ServletContextListener 来处理。在 ServletContextListener 接口中定义了处理 ServletContextEvent 事件的两个方法。
    * ### contextInitialized(ServletContextEvent sce)
    * ### contextDestroyed(ServletContextEvent sce)
    ```
    <listener>
        <listener-class>xxx</listener-class>
    </listener>


    ServletContext servletContext = event.getServletContext();
    servletContext.setAttribute(key, value);
    servletContext.getAttribute(key);
    ```
* ### 什么是连接池 (connection poll): 用池来管理 Connection，这样可以重复使用 Connection。有了池，就不用自己来创建 Connection，而是通过池来获取 Connection 对象。当使用完 Connection 后，调用 Connection 的 close() 方法也不会真的关闭 Connection，而是把 Connection “歸還” 给池。池就可以再利用这个 Connection 对象了。
* ### DBCP (DataBase Connection Pool) 也是一个开源的连接池，是 Apache Commons 成员之一，在企业开发中也比较常见，tomcat 内置的连接池。
```
import org.apache.commons.dbcp.BasicDataSource;

// 创建 DataSource 接口的实现类对象
BasicDataSource dataSource = new BasicDataSource();

// 链接数据库的 4 个最基本信息，通过对象的 set 方法进行设置如下：
// 设置数据库驱动
dataSource.setDriverClassName(DRIVERNAME);
// 设置访问数据库的路径
dataSource.setUrl(URL);
// 设置登录数据库的用户名
dataSource.setUsername(USERNAME);
// 设置登录数据库的密码
dataSource.setPassword(PASSWORD);

// 对象连接池中的常见配置项，以下的四个配置可以不配置 (因为有默认配置)，但是上面的四个是必须要配置的！
// 指定初始化的连接数
dataSource.setInitialSize(INITIALSIZE);
// 指定最大链接数量
dataSource.setMaxActive(MAXIDLE);
// 指定最大空闲数
dataSource.setMaxIdle(MINLDEL);
// 指定最小空闲数
dataSource.setMinIdle(MAXACTIVE);

Connection conn = dataSource.getConnection();
PreparedStatement pstmt = conn.prepareStatement(sql);
```
* ### DBUtils 是 java 编程中的数据库操作实用工具，小巧简单实用。DBUtils 封装了对 JDBC 的操作，简化了 JDBC 操作。
    * ### QueryRunner 中提供对 sql 语句操作的 API (insert, update, delete)。
    * ### ResultSetHandler 接口，用于定义 select 操作后，怎样封装结果集。
    * ### DbUtils 类，它就是一个工具类，定义了关闭资源与事务处理的方法。
```
Connection conn = DriverManager.getConnection(url, username, password);

QueryRunner qr = new QueryRunner();

String sql = "DELETE FROM classmate WHERE id<=?";
int row = qr.update(conn, sql, x);
DbUtils.closeQuietly(conn);

String sql = "UPDATE classmate SET age=? WHERE name=?";
Object[] params = {x, x};
int row = qr.update(conn, sql, params);
DbUtils.closeQuietly(conn);

String sql = "INSERT INTO classmate VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)";
Object[] params = {x, x, x, x, x, x, x};
int row = qr.update(conn, sql, params);
DbUtils.closeQuietly(conn);
```
* ### QueryRunnerd 的 query 方法实现查 (select)
    * ### ArrayHandler: 将结果集中的第一条记录封装到一个 Object[] 数组中，数组中的每一个元素就是这条记录中的每一个字段的值。
    * ### ArrayListHandler: 将结果集中的每一条记录都封装到一个 Object[] 数组中，将这些数组在封装到 List 集合中。
    * ### BeanHandler: 将结果集中第一条记录封装到一个指定的 javaBean 中。
    * ### BeanListHandler: 将结果集中每一条记录封装到指定的 javaBean 中，将这些 javaBean 在封装到 List 集合中。
    * ### ColumnListHandler: 将结果集中指定的列的字段值，封装到一个 List 集合中。
    * ### ScalarHandler: 它是用于单数据。例如 select count(*) from 表操作。
    * ### MapHandler: 将结果集第一行封装到 Map 集合中, Key = 列名, Value = 该列数据。
    * ### MapListHandler: 将结果集第一行封装到 Map 集合中, Key = 列名, Value = 该列数据, Map 集合存储到 List 集合。
```
String sql = "SELECT * FROM classmate";
Object[] result = qr.query(con, sql, new ArrayHandler());
for(Object obj : result){
    System.out.print(obj);
}

String sql = "SELECT * FROM classmate";        
List<Object[]> result=  qr.query(con, sql, new ArrayListHandler());
for( Object[] objs  : result){
    for(Object obj : objs){
        System.out.print(obj + ", ");
    }
    System.out.println();
}

String sql = "SELECT * FROM classmate";
Student s = qr.query(con, sql, new BeanHandler<Student>(Student.class));

String sql = "SELECT * FROM classmate ";
List<Student> list = qr.query(con, sql, new BeanListHandler<Student>(Student.class));
for(Student s : list){
    System.out.println(s);
}

String sql = "SELECT * FROM classmate ";
List<Object> list = qr.query(con, sql, new ColumnListHandler<Object>("name"));
for(Object obj : list){
    System.out.println(obj);
}

String sql = "SELECT COUNT(*) FROM classmate";
long count = qr.query(con, sql, new ScalarHandler<Long>());
System.out.println(count);

String sql = "SELECT  * FROM classmate where id = ?";
Map<String,Object> map = qr.query(con, sql, new MapHandler(), x);
for(String key : map.keySet()){
    System.out.println(key + ".." + map.get(key));
}

String sql = "SELECT  * FROM classmate";
List<Map<String,Object>> list = qr.query(con, sql, new MapListHandler());
for(Map<String, Object> map : list){
    for(String key : map.keySet()){
        System.out.print(key + "..." + map.get(key) + ", ");
    }
    System.out.println();
}
```
* ### JNDI: 在 J2EE 容器中配置 JNDI 参数，定义一个数据源，也就是 JDBC 引用参数，给这个数据源设置一个名称，然后，在程序中，通过数据源名称引用数据源从而访问后台数据库。
* ### ORM: JPA, Java Persistence API.
    * ### Entity Class
    ```
    @Entity
    @Table(name = "tableName")
    public class TableName {
        @Id
        @Column(name="ID")
        private long id;

        @Column(name=...)
        ...
    }
    ```
    * ### Persistence Unit: 相關設定資訊，包含 JPA 所管理的 entity。
    * ### Entuty Manager: 管理 entity object 生命週期，也負責查詢、新增、刪除、修改 (可以透過注入生成)。
    ```
    @PersistenceContext
    EntityManager em;

    Query query = em.createNativeQuery(sql, TableName.class);
    TableName tableName = (TableName) query.getResultList().get(0);
    List<TableName> result = query.getResultList();


    /* 更新資料使用 UserTransaction。 */
    UserTransaction utx = em.getTransaction();
    // 开启事务
    utx.begin();
    // 做一些事
    em...
    // 提交事务
    utx.commit();
    ```
    * ### Persistence Context: 可視為 Persistence Unit 載入 JVM 的複製版。
    * ### Persistence Identity: 每一個 entity object 都會有一個 Persistence Identity 對應表中每一筆資料。
<br />
