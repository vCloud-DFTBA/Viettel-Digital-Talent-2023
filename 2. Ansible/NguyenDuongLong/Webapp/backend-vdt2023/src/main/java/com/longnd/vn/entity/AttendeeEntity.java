package com.longnd.vn.entity;

import javax.persistence.*;

@Entity(name = "Attendee")
@Table(name = "attendee")
public class AttendeeEntity {
    private static final long serialVersionUID = 1L;

    @Id
    @GeneratedValue(strategy= GenerationType.AUTO)
    @Column(name = "id")
    private Long id;

    @Column(name = "username", unique = true)
    private String username;
    @Column(name = "name")
    private String name;

    @Column(name = "year_of_bth")
    private Long yearOfBirth;

    @Column(name = "sex")
    private String sex;

    @Column(name = "school")
    private String school;

    @Column(name = "major")
    private String major;

    public AttendeeEntity() {
    }

    public AttendeeEntity(Long id, String username, String name, Long yearOfBirth, String sex, String school, String major) {
        this.id = id;
        this.username = username;
        this.name = name;
        this.yearOfBirth = yearOfBirth;
        this.sex = sex;
        this.school = school;
        this.major = major;
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Long getYearOfBirth() {
        return yearOfBirth;
    }

    public void setYearOfBirth(Long yearOfBirth) {
        this.yearOfBirth = yearOfBirth;
    }

    public String getSex() {
        return sex;
    }

    public void setSex(String sex) {
        this.sex = sex;
    }

    public String getSchool() {
        return school;
    }

    public void setSchool(String school) {
        this.school = school;
    }

    public String getMajor() {
        return major;
    }

    public void setMajor(String major) {
        this.major = major;
    }

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }
}
