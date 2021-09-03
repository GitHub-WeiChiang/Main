package com.example.demo;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import reactor.core.publisher.Flux;
import reactor.core.publisher.Mono;

import javax.validation.Valid;
import java.time.Duration;

@RestController
@RequestMapping(path = "/user/mongodb")
public class UserMongodbController {
	
	@Autowired
    private UserRepository userRepository;
	
    @GetMapping(value = "/list")
    public Flux<User> getAll() {
        return userRepository.findAll();
    }
    
    @GetMapping(value = "/listdelay", produces = MediaType.APPLICATION_STREAM_JSON_VALUE)
    public Flux<User> getAlldelay() {
        return userRepository.findAll().delayElements(Duration.ofSeconds(1));
    }
    
    @GetMapping("/{id}")
    public Mono<ResponseEntity<User>> getUser(@PathVariable String id) {
        return userRepository.findById(id)
                .map(getUser -> ResponseEntity.ok(getUser))
                .defaultIfEmpty(ResponseEntity.notFound().build());
    }
    
    @PostMapping("")
    public Mono<User> createUser(@Valid User user) {
        return userRepository.save(user);
    }
    
    @PutMapping("/{id}")
    public Mono updateUser(@PathVariable(value = "id") String id, @Valid User user) {
        return userRepository.findById(id)
                .flatMap(existingUser -> {
                    existingUser.setName(user.getName());
                    return userRepository.save(existingUser);
                })
                .map(updateUser -> new ResponseEntity<>(updateUser, HttpStatus.OK))
                .defaultIfEmpty(new ResponseEntity<>(HttpStatus.NOT_FOUND));
    }
    
    @DeleteMapping("/{id}")
    public Mono<ResponseEntity<Void>> deleteUser(@PathVariable(value = "id") String id) {
        return userRepository.findById(id)
                .flatMap(existingUser ->
                        userRepository.delete(existingUser)
                                .then(Mono.just(new ResponseEntity<Void>(HttpStatus.OK)))
                )
                .defaultIfEmpty(new ResponseEntity<>(HttpStatus.NOT_FOUND));
    }
    
}
