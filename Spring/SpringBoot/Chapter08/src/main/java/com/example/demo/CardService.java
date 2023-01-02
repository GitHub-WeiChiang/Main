package com.example.demo;

import java.util.List;

public interface CardService {
	public List<Card> getCardList();
    public Card findCardById(long id);
}
