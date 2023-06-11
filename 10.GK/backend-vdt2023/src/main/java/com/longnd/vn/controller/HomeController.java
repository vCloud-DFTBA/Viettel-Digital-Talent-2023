package com.longnd.vn.controller;

import com.longnd.vn.dto.ApiResponse;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping(value = "")
@CrossOrigin("*")
@Slf4j
public class HomeController {
    @GetMapping
    public ResponseEntity<ApiResponse<String>> ping() {
        log.info("Call ping()");
        return ResponseEntity.ok(ApiResponse.ok("Application Started (v.0.0)"));
    }
}
