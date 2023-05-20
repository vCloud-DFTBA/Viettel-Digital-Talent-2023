package com.longnd.vn.controller.advice;

import com.longnd.vn.common.exception.CommonException;
import com.longnd.vn.dto.ApiResponse;
import com.longnd.vn.utils.StringUtil;
import com.longnd.vn.utils.Translator;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.lang.NonNull;
import org.springframework.orm.jpa.JpaSystemException;
import org.springframework.validation.FieldError;
import org.springframework.web.bind.MethodArgumentNotValidException;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.RestControllerAdvice;
import org.springframework.web.context.request.WebRequest;
import org.springframework.web.servlet.mvc.method.annotation.ResponseEntityExceptionHandler;

import java.util.*;

@RestControllerAdvice
public class APIControllerAdvisor extends ResponseEntityExceptionHandler {

    private final Translator translator;

    public APIControllerAdvisor(Translator translator) {
        this.translator = translator;
    }

    @ExceptionHandler({CommonException.class})
    public ResponseEntity<?> handleCommonException(CommonException commonException) {
        if (!StringUtil.isBlank(commonException.getCode())) {
            if (commonException.getMessage() == null) {
                String message = this.translator.getMessage(commonException.getCode());
                if (!commonException.getMessageParams().isEmpty()) {
                    message = StringUtil.format(message, commonException.getMessageParams());
                }
                commonException.setMessage(message);
            }
        }
        if (commonException.getErrors() != null) {
            List<Map<String, String>> localizeErrors = new ArrayList<>();
            for (Map<String, String> item : commonException.getErrors()) {
                if (item.containsKey("code")) {
                    item.put("message", translator.getMessage(item.get("code")));
                }
                localizeErrors.add(item);
            }
            commonException.setErrors(localizeErrors);
        }
        return ResponseEntity.status(commonException.getHttpStatus()).body(ApiResponse.failed(commonException.getCode(), commonException.getMessage(), commonException.getErrors()));
    }

    @Override
    @NonNull
    protected ResponseEntity<Object> handleMethodArgumentNotValid(MethodArgumentNotValidException ex,
                                                                  @NonNull HttpHeaders headers,
                                                                  @NonNull HttpStatus status,
                                                                  @NonNull WebRequest request) {
        String message = ex.getMessage();
        logger.error(message);
        Map<String, String> errors = new HashMap<>();
        ex.getBindingResult().getAllErrors().forEach((error) -> {
            String fieldName = ((FieldError) error).getField();
            String errorMessage = error.getDefaultMessage();
            errors.put(fieldName, errorMessage);
        });
        return ResponseEntity.status(HttpStatus.BAD_REQUEST)
                .body(ApiResponse.failed(HttpStatus.BAD_REQUEST.toString(), null, Collections.singletonList(errors)));
    }

    @ExceptionHandler(value = JpaSystemException.class)
    public ResponseEntity<ApiResponse<?>> handleJpaSystemException(JpaSystemException e) {
        return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR)
                .body(ApiResponse.failed(HttpStatus.INTERNAL_SERVER_ERROR.value(), e.getCause().getCause().toString()));
    }


    @ExceptionHandler({Exception.class})
    public ResponseEntity<ApiResponse<?>> handleException(Exception exception) {
        return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body(ApiResponse.failed(null, exception.getMessage(), null));
    }

}

