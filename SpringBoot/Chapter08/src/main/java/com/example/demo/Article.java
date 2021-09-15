package com.example.demo;

import java.io.Serializable;
import java.util.Arrays;
import java.util.List;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.Transient;
import javax.validation.constraints.NotEmpty;
import javax.validation.constraints.Size;

import lombok.Data;

// 這是一個實體Bean
@Entity
@Data
public class Article implements Serializable {

	@Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private long id;
	
	@Column(nullable = false, unique = true)
    @NotEmpty(message = "标题不能为空")
    private String title;
	
	@Column(columnDefinition="enum('图','图文','文')")
    private String type;
	
	private Boolean available = Boolean.FALSE;
    @Size(min = 0, max = 20)
    private String keyword;
    @Size(max = 255)
    private String description;
    @Column(nullable = false)
    private String body;
    
    @Transient
    private List keywordlists;

    public List getKeywordlists() {
    	return Arrays.asList(this.keyword.trim().split("|"));
    }
    
    public void setKeywordlists(List keywordlists) {
        this.keywordlists = keywordlists;
    }
	
}
