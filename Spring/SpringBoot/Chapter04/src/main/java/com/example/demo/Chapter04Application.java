package com.example.demo;

//import org.springframework.boot.Banner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

// 標記為 Spring Boot 專案的入口類別
@SpringBootApplication
public class Chapter04Application {

	public static void main(String[] args) {
//		SpringApplication springApplication= new SpringApplication(Chapter04Application.class);
//		springApplication.setBannerMode(Banner.Mode.OFF);
//		springApplication.run(args);
		
		SpringApplication.run(Chapter04Application.class, args);
	}

}
