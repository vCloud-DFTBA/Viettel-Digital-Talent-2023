package com.longnd.vn.utils;

import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Iterator;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class StringUtil {
    public static final String EMPTY = "";
    public static final String SPACE = " ";
    public static final String DOT = ".";
    public static final String COMMA = ",";
    public static final String COLON = ":";
    public static final String SEMICOLON = ";";
    public static final String UNDERSCORE = "_";

    public static final String paramCharacter = "\\{\\}";

    public StringUtil() {
    }

    public static String format(String format, List<String> params) {
        String res = format;
        for (String param : params) {
            res = res.replaceFirst(paramCharacter, param);
        }
        return res;
    }

    public static boolean isEmpty(String... args) {
        String[] var1 = args;
        int var2 = args.length;

        for (int var3 = 0; var3 < var2; ++var3) {
            String ele = var1[var3];
            if (ele == null || ele.trim().isEmpty()) {
                return true;
            }
        }

        return false;
    }

    public static int length(CharSequence cs) {
        return cs == null ? 0 : cs.length();
    }

    public static boolean isBlank(CharSequence cs) {
        int strLen = length(cs);
        if (strLen == 0) {
            return true;
        } else {
            for (int i = 0; i < strLen; ++i) {
                if (!Character.isWhitespace(cs.charAt(i))) {
                    return false;
                }
            }

            return true;
        }
    }

    public static boolean isEmpty(String value) {
        return value == null || value.isEmpty();
    }

    public static String concatenate(List<String> listOfItems, String separator) {
        StringBuilder sb = new StringBuilder();
        Iterator<String> iterator = listOfItems.iterator();

        while (iterator.hasNext()) {
            sb.append((String) iterator.next());
            if (iterator.hasNext()) {
                sb.append(separator);
            }
        }

        return sb.toString();
    }

    public static String toStringFromList(List<String> list, String separator) {
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < list.size(); ++i) {
            sb.append((String) list.get(i));
            if (i < list.size() - 1) {
                sb.append(separator);
            }
        }

        return sb.toString();
    }

    public static boolean checkSpecialCharacter(String value) {
        Pattern special = Pattern.compile("[!@#$%&*()_+=|<>?{}\\[\\]~ -]", Pattern.CASE_INSENSITIVE);
        Matcher m = special.matcher(value);
        return m.find();
    }

    public static String convertDateToString(Date date, String pattern) {
        String dateStr = null;
        if (date != null) {
            DateFormat dateFormat = new SimpleDateFormat(pattern);

            try {
                dateStr = dateFormat.format(date);
            } catch (Exception var5) {
                return null;
            }
        }

        return dateStr;
    }

    public static String escapePath(String path) {
        if (path == null || EMPTY.equals(path)) {
            return path;
        }

        String step1 = path.replace("\\", "\\\\");
        step1 = step1.replace("%", "\\%");
        return step1.replace("_", "\\_");
    }

}

