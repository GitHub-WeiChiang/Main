package com.example.demo;

import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.stereotype.Component;

// 將 POJO 實體化到 Spring 容器中，當類別不屬於 @Controller 和 @Service 時可使用
@Component
// 獲取配置在 application.properties 或 application.yml 文件中的參數
@ConfigurationProperties(prefix = "personinfo")
public class GetPersonInfoProperties {
	private String name;
    private int age;
    
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }
}
