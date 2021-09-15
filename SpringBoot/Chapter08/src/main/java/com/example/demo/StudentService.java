package com.example.demo;

import java.util.List;

public interface StudentService {
	public List<Student> getStudentlist();
    public Student findStudentById(long id);
}
