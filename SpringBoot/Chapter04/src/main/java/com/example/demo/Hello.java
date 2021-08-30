package com.example.demo;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;

// 註釋式程式設計

// 定義 Rest 風格控制器
// 傳回 Json 或 XML 等，不能傳回 HTML
// 相當於 @Controller + @ResponseBody
//@RestController

@Controller
public class Hello {

	@ResponseBody
	// 定義造訪路徑
	@RequestMapping("/hello")
	public String hello() throws Exception {
		return "Hello, Spring Boot!";
	}
}
