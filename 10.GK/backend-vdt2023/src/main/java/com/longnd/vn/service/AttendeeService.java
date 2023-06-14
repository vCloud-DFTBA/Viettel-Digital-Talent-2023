package com.longnd.vn.service;

import com.longnd.vn.dto.AttendeeDTO;
import com.longnd.vn.entity.AttendeeEntity;

import java.util.List;

public interface AttendeeService {
    List<AttendeeDTO> getAll();

    AttendeeDTO getById(Long id);

    AttendeeDTO save(AttendeeDTO dto);

    Boolean deleteById(Long id);
}
