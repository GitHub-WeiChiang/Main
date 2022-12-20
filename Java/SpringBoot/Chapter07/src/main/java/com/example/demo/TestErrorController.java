package com.example.demo;

import java.util.HashMap;
import java.util.Map;

import org.springframework.boot.web.servlet.error.ErrorController;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
// springboot 提供了預設的錯誤對應位址 error
@RequestMapping("/error")
// 繼承 springboot 提供的 ErrorController
public class TestErrorController implements ErrorController {

    public String getErrorPath() {
        return null;
    }
    
    // 一定要添加 url 映射，指向error
    // 可以根據請求傳回對應資料格式
    // @RequestMapping(value = "", produces = "text/html;charset=UTF-8")
    // @RequestMapping(value = "", consumes = "application/json;charset=UTF-8", produces = "application/html;charset=UTF-8")
    @RequestMapping
    public Map<String, Object> handleError() {
        //用Map容器返回信息
        Map<String, Object> map = new HashMap<String, Object>();
        map.put("code", 404);
        map.put("msg", "不存在");
        return map;
    }
    
    @RequestMapping("/ok")
    @ResponseBody
    public Map<String, Object> noError() {
        //用Map容器返回信息
        Map<String, Object> map = new HashMap<String, Object>();
        map.put("code ", 200);
        map.put("msg", "正常，这是测试页面");

        return map;
    }
	
}
