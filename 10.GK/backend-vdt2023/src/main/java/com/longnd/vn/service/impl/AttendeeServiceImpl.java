package com.longnd.vn.service.impl;

import com.longnd.vn.common.error.ErrorConstants;
import com.longnd.vn.common.exception.CommonException;
import com.longnd.vn.dto.AttendeeDTO;
import com.longnd.vn.entity.AttendeeEntity;
import com.longnd.vn.repository.AttendeeRepository;
import com.longnd.vn.service.AttendeeService;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.HttpStatus;
import org.springframework.stereotype.Service;

import javax.persistence.EntityNotFoundException;
import java.util.List;

@Service
@Slf4j
public class AttendeeServiceImpl implements AttendeeService {

    private final AttendeeRepository attendeeRepository;

    public AttendeeServiceImpl(AttendeeRepository attendeeRepository) {
        this.attendeeRepository = attendeeRepository;
    }

    @Override
    public List<AttendeeDTO> getAll() {
        return attendeeRepository.findAllAttendees();
    }

    @Override
    public AttendeeDTO getById(Long id) {
        log.info("AttendeeServiceImpl.getById()");
        return new AttendeeDTO(attendeeRepository.findById(id).orElseThrow(EntityNotFoundException::new));
    }

    @Override
    public AttendeeDTO save(AttendeeDTO dto) {
        if (dto.getUsername() == null) {
            throw CommonException.create(HttpStatus.BAD_REQUEST).code(ErrorConstants.USERNAME_REQUIRE);
        }

        AttendeeEntity entity;
        if (dto.getId() != null) {
            entity = attendeeRepository.findById(dto.getId()).orElseThrow(NullPointerException::new);
        } else {
            entity = new AttendeeEntity();
        }

        entity.setUsername(dto.getUsername());
        entity.setName(dto.getName());
        entity.setYearOfBirth(dto.getYearOfBirth());
        entity.setSex(dto.getSex());
        entity.setSchool(dto.getSchool());
        entity.setMajor(dto.getMajor());

        return new AttendeeDTO(attendeeRepository.save(entity));
    }

    @Override
    public Boolean deleteById(Long id) {
        if (!attendeeRepository.findById(id).isPresent()) {
            throw new EntityNotFoundException();
        }
        attendeeRepository.deleteById(id);
        return true;
    }
}
