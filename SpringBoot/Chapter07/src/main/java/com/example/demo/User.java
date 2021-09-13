package com.example.demo;

import java.io.Serializable;
import lombok.Data;

@Data
public class User implements Serializable {
    private int id;
    private String name;
}
