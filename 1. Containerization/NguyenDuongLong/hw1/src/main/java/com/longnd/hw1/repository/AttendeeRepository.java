package com.longnd.hw1.repository;

import com.longnd.hw1.entity.AttendeeEntity;
import org.springframework.data.jpa.repository.JpaRepository;

public interface AttendeeRepository extends JpaRepository<AttendeeEntity, Long> {
}
