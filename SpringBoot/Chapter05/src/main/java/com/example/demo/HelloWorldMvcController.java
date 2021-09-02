package com.example.demo;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;

// 定義一個控制器類別
@Controller
public class HelloWorldMvcController {
	
	// URL 對應
	@RequestMapping("/helloworld")
	public String helloWorld(Model model) throws Exception {
        model.addAttribute("mav", "HelloWorldController ,Spring Boot!");
        return "hello";
    }
	
}
