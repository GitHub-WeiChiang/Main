package com.example.demo;

import org.springframework.data.annotation.Id;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
// 生成一個包含所有參數的 constructor
@AllArgsConstructor
// 生成一個沒有參數的constructor
@NoArgsConstructor
public class User {
	@Id
    private long id;
    private String name;
    private int age;
}
