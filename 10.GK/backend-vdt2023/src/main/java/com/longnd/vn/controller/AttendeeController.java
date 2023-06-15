package com.longnd.vn.controller;

import com.longnd.vn.common.error.ErrorConstants;
import com.longnd.vn.common.exception.CommonException;
import com.longnd.vn.dto.ApiResponse;
import com.longnd.vn.dto.AttendeeDTO;
import com.longnd.vn.service.AttendeeService;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping(value = "/api/attendees")
@CrossOrigin("*")
@Slf4j
public class AttendeeController {

    //    @Autowired
    //    private AttendeeService attendeeService;
    private final AttendeeService attendeeService;

    public AttendeeController(AttendeeService attendeeService) {
        this.attendeeService = attendeeService;
    }

    @GetMapping("/all")
    public ResponseEntity<ApiResponse<List<AttendeeDTO>>> getAll() {
        log.info("Call getAll()");
        return ResponseEntity.ok(ApiResponse.ok(attendeeService.getAll()));
    }

    @GetMapping("/{id}")
    public ResponseEntity<ApiResponse<AttendeeDTO>> getById(@PathVariable("id") Long id) {
        log.info("Call getById()");
        return ResponseEntity.ok(ApiResponse.ok(attendeeService.getById(id)));
    }

    @PutMapping
    public ResponseEntity<ApiResponse<AttendeeDTO>> update(@RequestBody AttendeeDTO attendee) {
        log.info("Call update()");
        return ResponseEntity.ok(ApiResponse.ok(attendeeService.save(attendee)));
    }


    @PostMapping
    public ResponseEntity<ApiResponse<AttendeeDTO>> create(@RequestBody AttendeeDTO attendee) {
        log.info("Call create()");
        return ResponseEntity.ok(ApiResponse.ok(attendeeService.save(attendee)));
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<ApiResponse<Boolean>> deleteById(@PathVariable("id") Long id) {
        log.info("Call deleteById()");
        return ResponseEntity.ok(ApiResponse.ok(attendeeService.deleteById(id)));
    }

    @GetMapping("/ping")
    public ResponseEntity<ApiResponse<String>> ping() {
        log.info("Call ping()");
        return ResponseEntity.ok(ApiResponse.ok("Application Started (v2)!!!"));
    }
}
