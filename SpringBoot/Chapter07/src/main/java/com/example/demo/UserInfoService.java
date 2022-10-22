package com.example.demo;

import org.springframework.stereotype.Service;

@Service
public class UserInfoService {

	public UserInfo getUserInfo(){
		UserInfo userInfo = new UserInfo();
		userInfo.setName("zhonghua");
		userInfo.setAge(18);
        return userInfo;
    }
	
}
