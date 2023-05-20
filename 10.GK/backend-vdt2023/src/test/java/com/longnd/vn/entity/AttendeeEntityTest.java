package com.longnd.vn.entity;

import com.longnd.vn.entity.AttendeeEntity;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

public class AttendeeEntityTest {

    @Test
    public void testAttendeeEntity() {
        Long id = 1L;
        String username = "john.doe";
        String name = "John Doe";
        Long yearOfBirth = 1990L;
        String sex = "Male";
        String school = "Example School";
        String major = "Computer Science";

        AttendeeEntity attendee = new AttendeeEntity(id, username, name, yearOfBirth, sex, school, major);

        // Assert the values of the AttendeeEntity object
        Assertions.assertEquals(id, attendee.getId());
        Assertions.assertEquals(username, attendee.getUsername());
        Assertions.assertEquals(name, attendee.getName());
        Assertions.assertEquals(yearOfBirth, attendee.getYearOfBirth());
        Assertions.assertEquals(sex, attendee.getSex());
        Assertions.assertEquals(school, attendee.getSchool());
        Assertions.assertEquals(major, attendee.getMajor());
    }
}