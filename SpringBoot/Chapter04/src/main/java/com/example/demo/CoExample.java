package com.example.demo;

import java.util.List;
import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.stereotype.Component;
import lombok.Data;

@Data
@Component
@ConfigurationProperties(prefix ="com.example")
public class CoExample{
    private String name;
    private int age;
    private List<String> address;
}