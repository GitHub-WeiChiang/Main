package com.example.demo;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

// 標記設定類別，讓 Spring 載入該類別設定作為 Bean 載體
@Configuration
public class UserConfig {
	
	// 產生一個 Bean 交由 Spring 管理，目的為封裝使用者資料庫中數據
    @Bean("user1")
    public User user() {
        User user = new User();
        user.setId(1);
        user.setName("longzhiran");
        return user;
    }
    
}
