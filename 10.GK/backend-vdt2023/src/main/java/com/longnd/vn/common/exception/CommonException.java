package com.longnd.vn.common.exception;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.springframework.http.HttpStatus;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class CommonException extends RuntimeException {
    private HttpStatus httpStatus;
    private String code;
    private String message;
    private List<Map<String, String>> errors = new ArrayList<>();
    private List<String> messageParams = new ArrayList<>();

    public static CommonException create(HttpStatus httpStatus) {
        CommonException commonException = new CommonException();
        commonException.setHttpStatus(httpStatus);
        return commonException;
    }

    public CommonException message(String message) {
        this.message = message;
        return this;
    }

    public CommonException code(String code) {
        this.code = code;
        return this;
    }

    public CommonException errors(List<Map<String, String>> errors) {
        this.setErrors(errors);
        return this;
    }

//    public CommonException withError(String field, String code) {
//        Map<String, String> error = new HashMap<>() {{
//            put("field", field);
//            put("code", code);
//        }};
//        this.errors.add(error);
//        return this;
//    }

    public CommonException withMessageParams(List<String> messageParams) {
        this.setMessageParams(messageParams);
        return this;
    }
}
