package com.example.demo;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class ExceptionController {
    @RequestMapping("/BusinessException")
    public String testResponseStatusExceptionResolver(@RequestParam("i") int i){
    	if (i == 0) {
        	throw new BusinessException(600, "自訂錯誤");
        }
        return "success";
    }

}
