package com.longnd.vn.controller;

import com.longnd.vn.entity.AttendeeEntity;
import com.longnd.vn.repository.AttendeeRepository;
import lombok.extern.slf4j.Slf4j;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping(value = "/api/attendees")
@CrossOrigin("*")
@Slf4j
public class AttendeeController {
    private final AttendeeRepository attendeeRepository;

    public AttendeeController(AttendeeRepository attendeeRepository) {
        this.attendeeRepository = attendeeRepository;
    }

    @GetMapping("/all")
    public List<AttendeeEntity> getAll() {
        log.info("Call getAll()");
        List<AttendeeEntity> result = attendeeRepository.findAll();
        return result;
    }

    @GetMapping("/{id}")
    public AttendeeEntity getById(@PathVariable("id") Long id) {
        log.info("Call getById()");
        return attendeeRepository.findById(id).get();
    }

    @PutMapping
    public AttendeeEntity update(@RequestBody AttendeeEntity attendee) {
        log.info("Call update()");
        return attendeeRepository.save(attendee);
    }

    @PostMapping
    public AttendeeEntity create(@RequestBody AttendeeEntity attendee) {
        log.info("Call create()");
        return attendeeRepository.save(attendee);
    }

    @DeleteMapping("/{id}")
    public Boolean deleteById(@PathVariable("id") Long id) {
        log.info("Call deleteById()");
        attendeeRepository.deleteById(id);
        return true;
    }
}
