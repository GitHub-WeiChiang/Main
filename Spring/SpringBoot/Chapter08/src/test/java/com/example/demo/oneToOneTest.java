package com.example.demo;

import org.junit.jupiter.api.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;

@SpringBootTest
@RunWith(SpringRunner.class)
public class oneToOneTest {
	@Autowired
    private StudentRepository studentRepository;
    @Autowired
    private CardRepository cardRepository;
    
    @Test
    public void testOneToOne() {
        Student student1 = new Student();
        student1.setName("赵大伟");
        student1.setSex("male");
        Student student2 = new Student();
        student2.setName("赵大宝");
        student2.setSex("male");

        Card card1 = new Card();
        card1.setNum(422802);
        student1.setCard(card1);
        studentRepository.save(student1);
        studentRepository.save(student2);
        Card card2 = new Card();
        card2.setNum(422803);
        cardRepository.save(card2);
        Long id = student1.getId();
        studentRepository.deleteById(id);
    }
}
