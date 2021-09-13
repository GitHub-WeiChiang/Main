package com.example.demo;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.web.servlet.ServletComponentScan;

// 元件掃描，自動發現與裝配 Bean
@ServletComponentScan
// 入口類別啟動註釋
@SpringBootApplication
public class Chapter07Application {

	public static void main(String[] args) {
		SpringApplication.run(Chapter07Application.class, args);
	}

}
