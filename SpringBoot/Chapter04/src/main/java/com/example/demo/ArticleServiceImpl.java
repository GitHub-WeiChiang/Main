package com.example.demo;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;
import org.springframework.stereotype.Service;

interface ArticleService {
	public abstract Article findArticleById(long id);
	public abstract Article findById(long id);
}

class Article {
	// 資料庫存取類別 (實現一非介面類別)
	// @Repository
	Article(long id) {
		
	}
}

// 標記為服務類別，主要為業務處裡類別，實現一非介面類別 (服務層)
@Service
public class ArticleServiceImpl implements ArticleService {
	
	// 讓 Spring 自動的把屬性需要的對象從 Spring 容器找出並注入
	@Autowired
	private ArticleServiceImpl articleRepository;

	@Override
	public Article findArticleById(long id) {
		return articleRepository.findById(id);
	}
	
	@Override
	public Article findById(long id) {
		return new Article(id);
	}

}
