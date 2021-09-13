package com.example.demo;

import java.util.HashMap;
import java.util.Map;

import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.ResponseBody;

// 用來攔截並處理應用程式中全部 Controller 所拋出的 Exception 例外錯誤。
// 其也是 @Component，所以會被 Spring scan 為 Bean。
@ControllerAdvice
public class CustomerBusinessExceptionHandler {
	@ResponseBody
    @ExceptionHandler(BusinessException.class)
    public Map<String, Object> businessExceptionHandler(BusinessException e) {
        Map<String, Object> map = new HashMap<String, Object>();
        map.put("code", e.getCode());
        map.put("message", e.getMessage());
        
        // 此處可以增加紀錄程式
        
        return map;
    }
}
