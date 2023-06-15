package com.longnd.vn.dto;

import com.longnd.vn.entity.AttendeeEntity;
import lombok.Data;

@Data
public class AttendeeDTO {
    private Long id;

    private String username;

    private String name;

    private Long yearOfBirth;

    private String sex;

    private String school;

    private String major;

    public AttendeeDTO() {
    }

    public AttendeeDTO(Long id, String username, String name, Long yearOfBirth, String sex, String school, String major) {
        this.id = id;
        this.username = username;
        this.name = name;
        this.yearOfBirth = yearOfBirth;
        this.sex = sex;
        this.school = school;
        this.major = major;
    }

    public AttendeeDTO(AttendeeEntity entity) {
        if (entity != null) {
            this.id = entity.getId();
            this.username = entity.getUsername();
            this.name = entity.getName();
            this.yearOfBirth = entity.getYearOfBirth();
            this.sex = entity.getSex();
            this.school = entity.getSchool();
            this.major = entity.getMajor();
        }
    }
}
