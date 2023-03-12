package com.example.demo;

import javax.validation.ConstraintValidator;
import javax.validation.ConstraintValidatorContext;


public class MyConstraintValidator implements ConstraintValidator<MyConstraint, String> {

    @Override
    public void initialize(MyConstraint myConstraint) {}

    @Override
    public boolean isValid(String s, ConstraintValidatorContext validatorContext) {
        if (!(s.equals("台北") || s.equals("臺北"))) {
            return false;
        }

        return true;
    }
}