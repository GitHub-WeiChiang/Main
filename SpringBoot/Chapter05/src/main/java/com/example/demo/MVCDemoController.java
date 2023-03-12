package com.example.demo;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.servlet.ModelAndView;

@Controller
public class MVCDemoController {
	
    @GetMapping("/mvcdemo")
    public ModelAndView hello() {
        User user = new User();
        
        user.setName("zhonghua");
        user.setAge(28);
        
        // 定義 MVC 中的視圖範本
        ModelAndView modelAndView = new ModelAndView("mvcdemo0");
        
        // 傳遞 user 實體物件給視圖
        modelAndView.addObject("user", user);
        
        return modelAndView;
    }
    
}
