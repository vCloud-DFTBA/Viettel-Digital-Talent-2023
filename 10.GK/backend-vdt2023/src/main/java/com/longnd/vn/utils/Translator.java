package com.longnd.vn.utils;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.context.MessageSource;
import org.springframework.context.i18n.LocaleContextHolder;
import org.springframework.stereotype.Component;
import org.springframework.stereotype.Service;

import java.util.Locale;

@Component
public class Translator {

    Logger logger = LoggerFactory.getLogger(Translator.class);

    private final MessageSource messageSource;

    Translator(MessageSource messageSource) {
        this.messageSource = messageSource;
    }

    public String getMessage(String msgCode) {
        try {
            Locale locale = LocaleContextHolder.getLocale();
            return messageSource.getMessage(msgCode, null, locale);
        } catch (Exception e) {
            logger.error(e.getMessage());
            return msgCode;
        }
    }
}
