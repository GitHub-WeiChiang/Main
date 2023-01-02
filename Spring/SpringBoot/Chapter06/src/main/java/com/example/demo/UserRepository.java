package com.example.demo;

import org.springframework.data.mongodb.repository.ReactiveMongoRepository;

//@Repository
public interface UserRepository extends ReactiveMongoRepository<User,String> {

}
