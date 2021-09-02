package com.example.demo;

import java.io.Serializable;

import javax.validation.constraints.Email;
import javax.validation.constraints.Max;
import javax.validation.constraints.Min;
import javax.validation.constraints.NotBlank;
import javax.validation.constraints.NotNull;

import org.hibernate.validator.constraints.Length;
import lombok.Data;

@Data
public class User2 implements Serializable {
	
	private Long id;
	
	@NotBlank(message = "用戶名稱不能為空")
    @Length(min = 5, max = 20, message = "用戶名長度為 5-20 個字符")
    private String name;
	
    @NotNull(message = "年齡不能為空")
    @Min(value = 18, message = "最小 18 歲")
    @Max(value = 60, message = "最大 60 歲")
    private Integer age;
    
    @Email(message = "請輸入 email")
    @NotBlank(message = "email 不能為空")
    private String email;
    
    @MyConstraint
    private String answer;
    
}
