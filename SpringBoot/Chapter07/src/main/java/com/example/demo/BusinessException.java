package com.example.demo;

public class BusinessException extends RuntimeException {
    // 自定錯誤碼
    private Integer code;
    // 自定建構子
    public BusinessException(int code,String msg) {
        super(msg);
        this.code = code;
    }

    public Integer getCode() {
        return code;
    }

    public void setCode(Integer code) {
        this.code = code;
    }
}
