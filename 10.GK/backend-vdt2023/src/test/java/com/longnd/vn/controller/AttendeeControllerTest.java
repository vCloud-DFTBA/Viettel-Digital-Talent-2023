package com.longnd.vn.controller;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.longnd.vn.dto.AttendeeDTO;
import com.longnd.vn.service.AttendeeService;
import com.longnd.vn.utils.Translator;
import org.json.JSONArray;
import org.json.JSONObject;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.mockito.Mockito;
import org.mockito.MockitoAnnotations;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.WebMvcTest;
import org.springframework.boot.test.mock.mockito.MockBean;
import org.springframework.http.MediaType;
import org.springframework.test.web.servlet.MockMvc;
import org.springframework.test.web.servlet.MvcResult;
import org.springframework.test.web.servlet.setup.MockMvcBuilders;
import org.springframework.web.context.WebApplicationContext;

import java.util.ArrayList;
import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.mockito.Mockito.when;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.*;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.content;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

@WebMvcTest(AttendeeController.class)
public class AttendeeControllerTest {
    @Autowired
    private WebApplicationContext webApplicationContext;

    @MockBean
    private Translator translator;

    @Autowired
    private MockMvc mockMvc;
    private ObjectMapper objectMapper;

    @MockBean
    private AttendeeService attendeeService;

    private AttendeeController attendeeController;

    public AttendeeControllerTest() {
        MockitoAnnotations.initMocks(this);
        attendeeController = new AttendeeController(attendeeService);
    }

    @BeforeEach
    public void setup() {
        MockitoAnnotations.openMocks(this);
        mockMvc = MockMvcBuilders.webAppContextSetup(webApplicationContext).build();
        objectMapper = new ObjectMapper();
    }

    @Test
    public void testGetAll() throws Exception {
        // Arrange
        List<AttendeeDTO> attendeeDTOList = new ArrayList<>();
        attendeeDTOList.add(new AttendeeDTO(1L, "user1", "John Doe", 1990L, "Male", "School A", "Major A"));
        attendeeDTOList.add(new AttendeeDTO(2L, "user2", "Jane Smith", 1992L, "Female", "School B", "Major B"));

        when(attendeeService.getAll()).thenReturn(attendeeDTOList);

        // Gửi yêu cầu GET /api/attendees/{id}
        MvcResult mvcResult = mockMvc.perform(get("/api/attendees/all"))
                .andExpect(status().isOk())
                .andExpect(content().contentType("application/json"))
                .andReturn();

        // Lấy nội dung trả về từ MvcResult
        String responseContent = mvcResult.getResponse().getContentAsString();

        // Kiểm tra nội dung JSON trả về
        JSONObject jsonResponse = new JSONObject(responseContent);
        assertEquals("OK", jsonResponse.getString("status"));

        JSONArray jsonData = jsonResponse.getJSONArray("data");
        assertEquals("John Doe", jsonData.getJSONObject(0).getString("name"));
        assertEquals("Jane Smith", jsonData.getJSONObject(1).getString("name"));
    }

    @Test
    public void testGetAttendeeById() throws Exception {
        Long attendeeId = 1L;
        AttendeeDTO dto = new AttendeeDTO();
        dto.setId(attendeeId);
        dto.setName("John Doe");

        // Giả lập dữ liệu trả về từ service
        Mockito.when(attendeeService.getById(attendeeId)).thenReturn(dto);

        // Gửi yêu cầu GET /api/attendees/{id}
        MvcResult mvcResult = mockMvc.perform(get("/api/attendees/{id}", attendeeId))
                .andExpect(status().isOk())
                .andExpect(content().contentType("application/json"))
                .andReturn();

        // Lấy nội dung trả về từ MvcResult
        String responseContent = mvcResult.getResponse().getContentAsString();

        // Kiểm tra nội dung JSON trả về
        JSONObject jsonResponse = new JSONObject(responseContent);
        assertEquals("OK", jsonResponse.getString("status"));

        JSONObject jsonData = jsonResponse.getJSONObject("data");
        assertEquals("John Doe", jsonData.getString("name"));
    }

    @Test
    public void testCreateAttendee() throws Exception {
        AttendeeDTO attendeeDTO = new AttendeeDTO();
        attendeeDTO.setId(1L);
        attendeeDTO.setUsername("john");
        attendeeDTO.setName("John Doe");
        attendeeDTO.setYearOfBirth(2002L);
        attendeeDTO.setSex("Male");
        attendeeDTO.setSchool("TLU");
        attendeeDTO.setMajor("IT");

        // Giả lập dữ liệu trả về từ service
        Mockito.when(attendeeService.save(attendeeDTO)).thenReturn(attendeeDTO);

        // Gửi yêu cầu POST /api/attendees
        MvcResult mvcResult = mockMvc.perform(post("/api/attendees")
                        .contentType(MediaType.APPLICATION_JSON)
                        .content(objectMapper.writeValueAsString(attendeeDTO)))
                .andExpect(status().isOk())
                .andExpect(content().contentType("application/json"))
                .andReturn();

        // Lấy nội dung trả về từ MvcResult
        String responseContent = mvcResult.getResponse().getContentAsString();

        // Kiểm tra nội dung JSON trả về
        JSONObject jsonResponse = new JSONObject(responseContent);
        assertEquals("OK", jsonResponse.getString("status"));

        JSONObject jsonData = jsonResponse.getJSONObject("data");
        assertEquals("1", jsonData.getString("id"));
        assertEquals("John Doe", jsonData.getString("name"));
        assertEquals("john", jsonData.getString("username"));
        assertEquals("2002", jsonData.getString("yearOfBirth"));
        assertEquals("Male", jsonData.getString("sex"));
        assertEquals("TLU", jsonData.getString("school"));
        assertEquals("IT", jsonData.getString("major"));
    }

    @Test
    public void testUpdateAttendee() throws Exception {
        AttendeeDTO attendeeDTO = new AttendeeDTO();
        attendeeDTO.setId(1L);
        attendeeDTO.setUsername("john");
        attendeeDTO.setName("John Doe");
        attendeeDTO.setYearOfBirth(2002L);
        attendeeDTO.setSex("Male");
        attendeeDTO.setSchool("TLU");
        attendeeDTO.setMajor("IT");

        // Giả lập dữ liệu trả về từ service
        Mockito.when(attendeeService.save(attendeeDTO)).thenReturn(attendeeDTO);

        // Gửi yêu cầu PUT /api/attendees
        MvcResult mvcResult = mockMvc.perform(put("/api/attendees")
                        .contentType(MediaType.APPLICATION_JSON)
                        .content(objectMapper.writeValueAsString(attendeeDTO)))
                .andExpect(status().isOk())
                .andExpect(content().contentType("application/json"))
                .andReturn();

        // Lấy nội dung trả về từ MvcResult
        String responseContent = mvcResult.getResponse().getContentAsString();

        // Kiểm tra nội dung JSON trả về
        JSONObject jsonResponse = new JSONObject(responseContent);
        assertEquals("OK", jsonResponse.getString("status"));

        JSONObject jsonData = jsonResponse.getJSONObject("data");
        assertEquals("1", jsonData.getString("id"));
        assertEquals("John Doe", jsonData.getString("name"));
        assertEquals("john", jsonData.getString("username"));
        assertEquals("2002", jsonData.getString("yearOfBirth"));
        assertEquals("Male", jsonData.getString("sex"));
        assertEquals("TLU", jsonData.getString("school"));
        assertEquals("IT", jsonData.getString("major"));
    }

    @Test
    public void testDeleteAttendee() throws Exception {
        Long attendeeId = 1L;

        // Giả lập dữ liệu trả về từ service
        Mockito.when(attendeeService.deleteById(attendeeId)).thenReturn(true);

        // Gửi yêu cầu GET /api/attendees/{id}
        MvcResult mvcResult = mockMvc.perform(delete("/api/attendees/{id}", attendeeId))
                .andExpect(status().isOk())
                .andExpect(content().contentType("application/json"))
                .andReturn();

        // Lấy nội dung trả về từ MvcResult
        String responseContent = mvcResult.getResponse().getContentAsString();

        // Kiểm tra nội dung JSON trả về
        JSONObject jsonResponse = new JSONObject(responseContent);
        assertEquals("OK", jsonResponse.getString("status"));
        assertEquals("true", jsonResponse.getString("data"));
    }
}