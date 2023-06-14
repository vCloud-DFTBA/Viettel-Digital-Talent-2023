package com.longnd.vn.repository;

import com.longnd.vn.dto.AttendeeDTO;
import com.longnd.vn.entity.AttendeeEntity;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;

import java.util.List;

public interface AttendeeRepository extends JpaRepository<AttendeeEntity, Long> {
    @Query(value = "SELECT NEW com.longnd.vn.dto.AttendeeDTO(e) FROM Attendee e")
    List<AttendeeDTO> findAllAttendees();
}
