package com.example.demo;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.reactive.function.server.RouterFunction;
import org.springframework.web.reactive.function.server.ServerResponse;

import static org.springframework.web.reactive.function.server.RequestPredicates.GET;
import static org.springframework.web.reactive.function.server.RouterFunctions.route;

@Configuration
public class Router {

	@Autowired
    private HelloWorldHandler helloWorldHandler;
	
	// 在配置類中掛有 @Bean 的方法所回傳的實例即為被 Spring IoC 容器管理的 bean
    @Bean
    public RouterFunction<ServerResponse> getString(){
        return route(GET("/helloworld"), req->helloWorldHandler.sayHelloWorld(req));
    }
	
}
