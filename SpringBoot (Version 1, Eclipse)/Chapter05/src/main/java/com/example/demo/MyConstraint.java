package com.example.demo;

import java.lang.annotation.Target;

import javax.validation.Constraint;
import javax.validation.Payload;

import java.lang.annotation.ElementType;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;

// 表示该注解用于什么地方: 字段声明（包括枚举常量）
@Target({ElementType.FIELD})
// 定义该注解的生命周期: 始终不会丢弃，运行期也保留该注解，因此可以使用反射机制读取该注解的信息。我们自定义的注解通常使用这种方式
@Retention(RetentionPolicy.RUNTIME)
// 指定該註解的校驗器
@Constraint(validatedBy = MyConstraintValidator.class)
// @interface 是用来自定义 JAVA Annotation 的语法，@interface 是用来自定义注释类型的。
public @interface MyConstraint {
	
	String message() default "請輸入天龍國城市名稱";
    Class<?>[] groups() default {};
    Class<? extends Payload>[] payload() default {};
    
}
