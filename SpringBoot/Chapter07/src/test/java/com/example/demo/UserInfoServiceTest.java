package com.example.demo;

import static org.hamcrest.CoreMatchers.is;

import org.junit.Assert;
import org.junit.jupiter.api.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.context.ApplicationContext;
import org.springframework.test.context.junit4.SpringRunner;

@RunWith(SpringRunner.class)
@SpringBootTest
public class UserInfoServiceTest {

	@Autowired
	private UserInfoService userInfoService;
	
	@Test
	public void getUserInfo() {
		UserInfo user = userInfoService.getUserInfo();

	    Assert.assertEquals(18, user.getAge());
	    Assert.assertThat(user.getName(), is("zhonghua"));
	}
	
}
