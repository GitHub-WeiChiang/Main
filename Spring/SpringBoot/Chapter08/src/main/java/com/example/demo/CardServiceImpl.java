package com.example.demo;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;

public class CardServiceImpl implements CardService {
    @Autowired
    private CardRepository cardRepository;

    @Override
    public List<Card> getCardList() {
        return cardRepository.findAll();
    }

    @Override
    public Card findCardById(long id) {
        return cardRepository.findById(id);
    }
}
