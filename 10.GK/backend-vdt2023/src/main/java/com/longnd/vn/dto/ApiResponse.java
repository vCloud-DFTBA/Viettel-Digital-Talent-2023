package com.longnd.vn.dto;

import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonInclude.Include;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;
import com.longnd.vn.common.constants.ApiStatus;

import java.util.List;
import java.util.Map;

@JsonInclude(Include.NON_EMPTY)
@JsonPropertyOrder({"status", "message", "data"})
public class ApiResponse<T> {
    @JsonProperty("status")
    private String status;

    @JsonProperty("code")
    private String code;

    @JsonProperty("message")
    private String message;

    @JsonProperty("errors")
    private List<Map<String, String>> errors;

    @JsonProperty("data")
    private T data;


    public ApiResponse() {
    }

    public static <T> ApiResponse<T> ok(T data) {
        ApiResponse<T> res = new ApiResponse<T>();
        res.status = ApiStatus.OK;
        res.data = data;
        return res;
    }

    public static <T> ApiResponse<T> ok() {
        ApiResponse<T> res = new ApiResponse<T>();
        res.status = ApiStatus.OK;
        return res;
    }


    public static <T> ApiResponse<T> failed(String code , String message) {
        ApiResponse<T> res = new ApiResponse<T>();
        res.status = ApiStatus.FAILED;
        res.code = code;
        res.message = message;
        return res;
    }

    public static <T> ApiResponse<T> failed(String message) {
        ApiResponse<T> res = new ApiResponse<T>();
        res.status = ApiStatus.FAILED;
        res.message = message;
        return res;
    }

    public static <T> ApiResponse<T> failed(String code , String message, List<Map<String, String>> errors) {
        ApiResponse<T> res = new ApiResponse<T>();
        res.status = ApiStatus.FAILED;
        res.code = code;
        res.message = message;
        res.errors = errors;
        return res;
    }

    public static <T> ApiResponse<T> failed(int code, String messages) {
        ApiResponse<T> ret = new ApiResponse<>();
        ret.status = ApiStatus.FAILED;
        ret.code = String.valueOf(code);
        ret.message = messages;
        return ret;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }

    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }

    public List<Map<String, String>> getErrors() {
        return errors;
    }

    public void setErrors(List<Map<String, String>> errors) {
        this.errors = errors;
    }

    public T getData() {
        return data;
    }

    public void setData(T data) {
        this.data = data;
    }
}
