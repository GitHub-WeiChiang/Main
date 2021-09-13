package com.example.demo;

import org.junit.Assert;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.http.MediaType;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.web.servlet.MockMvc;
import org.springframework.test.web.servlet.MvcResult;
import org.springframework.test.web.servlet.request.MockMvcRequestBuilders;
import org.springframework.web.context.WebApplicationContext;
import org.springframework.test.web.servlet.setup.MockMvcBuilders;
import org.springframework.test.web.servlet.result.MockMvcResultHandlers;
import org.springframework.test.web.servlet.result.MockMvcResultMatchers;

@RunWith(SpringRunner.class)
@SpringBootTest
class HelloControllerTest {

	@Autowired
    private WebApplicationContext webApplicationContext;
    private MockMvc mockMvc;
    
    @BeforeEach
    public void setUp() throws Exception{
    	System.out.println("setUp()");
        mockMvc = MockMvcBuilders.webAppContextSetup(webApplicationContext).build();
    }
    
    @Test
    public void hello() throws Exception {
    	// 得到MvcResult自定义验证
    	// 执行请求
    	MvcResult mvcResult= mockMvc.perform(MockMvcRequestBuilders.get("/hello")
    			.contentType(MediaType.APPLICATION_JSON_UTF8)
                //传入参数
                .param("name","longzhonghua")
                //接收的类型
                .accept(MediaType.APPLICATION_JSON_UTF8))
                //判断接收到的状态是否是200
                .andExpect(MockMvcResultMatchers.status().isOk())
                .andExpect(MockMvcResultMatchers.content().string("hello longzhonghua"))
                .andDo(MockMvcResultHandlers.print())
        //返回MvcResult
        .andReturn();
        //得到返回代码
        int status=mvcResult.getResponse().getStatus();
        //得到返回结果
        String content=mvcResult.getResponse().getContentAsString();
        //断言，判断返回代码是否正确
        Assert.assertEquals(200,status);
        //断言，判断返回的值是否正确
        Assert.assertEquals("hello longzhonghua", content);
    }
	
}
