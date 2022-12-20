package com.example.demo;

import org.springframework.context.annotation.EnableAspectJAutoProxy;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@EnableAspectJAutoProxy
public class TestController {
	
    @RequestMapping("/TestController")
    @MyTestAnnotation("测试 Annotation")
    public void testAnnotation() {
        System.err.println("測試自定義註釋");
    }

}
