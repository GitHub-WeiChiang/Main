package com.example.demo;

import org.springframework.stereotype.Component;
import java.lang.annotation.*;

// 標記作用範圍
@Target({ElementType.METHOD, ElementType.TYPE})
// 標記生命週期
@Retention(RetentionPolicy.RUNTIME)
// 將註釋資訊增加在 Java 文件中
@Documented
@Component
public @interface MyTestAnnotation {
	String value();
}
