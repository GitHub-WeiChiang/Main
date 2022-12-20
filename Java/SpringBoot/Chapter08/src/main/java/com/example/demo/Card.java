package com.example.demo;

import javax.persistence.*;
import lombok.Data;

@Entity
@Table(name = "card")
@Data
public class Card {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private long id;
    private Integer num;
}
