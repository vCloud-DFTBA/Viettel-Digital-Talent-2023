package com.longnd.vn.entity;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import javax.persistence.*;

@Entity(name = "Attendee")
@Table(name = "attendee")
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
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

}
