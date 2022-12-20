package com.example.demo;

import org.junit.jupiter.api.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.context.ApplicationContext;
import org.springframework.test.context.junit4.SpringRunner;

@RunWith(SpringRunner.class)
@SpringBootTest
class Chapter07ApplicationTests {
	
	@Autowired
    private ApplicationContext applicationContext;

	@Test
    public void testIoc() {
        User user = (User) applicationContext.getBean("user1");
        System.out.println(user);
    }

}
