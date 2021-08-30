package com.example.demo;

import org.junit.jupiter.api.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;

// 用於測試的註釋
@SpringBootTest
// 在 Spring 環境中進行測試
@RunWith(SpringRunner.class)
class Chapter04ApplicationTests {

    @Value("${age}")
    private int age;

    @Value("${name}")
    private String name;

    @Test
    public void getAge() {
        System.out.println(age);
    }

    @Test
    public void getName() {
        System.out.println(name);
    }
    
    @Autowired
    private GetPersonInfoProperties getPersonInfoProperties;
    
    @Test
    public void getpersonproperties() {
    	System.out.println(getPersonInfoProperties.getName() + getPersonInfoProperties.getAge());
    }
    
    @Autowired
    private CoExample coExample;
    
    @Test
    public void getName2() {
        System.out.println(coExample.getName());
    }

    @Test
    public void getAge2() {
        System.out.println(coExample.getAge());
    }

    @Test
    public void getAddress() {
        System.out.println(coExample.getAddress());
    }

	@Value("${var.env}")
    private String env;

    @Test
    public void getMyEnvironment() {
    	System.out.println(env);
    }
    
}
