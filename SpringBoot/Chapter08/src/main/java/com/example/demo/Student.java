package com.example.demo;

import javax.persistence.*;
import lombok.Data;

@Entity
@Data
@Table(name = "stdu")
public class Student {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private long id;
    private String name;
    @Column(columnDefinition = "enum('male','female')")
    private String sex;
    @OneToOne(cascade = CascadeType.ALL)
    @JoinColumn(name = "card_id")
	private Card card;
}
