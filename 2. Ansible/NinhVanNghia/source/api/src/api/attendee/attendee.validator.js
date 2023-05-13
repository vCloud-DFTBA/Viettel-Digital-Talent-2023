import { body, param } from "express-validator";

import { catchValidateError } from "../../middlewares";


export const getById = [
    param('attendeeId')
        .isInt({min: 0})
        .withMessage('attendeeId không hợp lệ'),

    catchValidateError,
]


export const create = [
    body('username')
        .trim()
        .notEmpty(),
    body('fullname')
        .trim()
        .notEmpty()
        .escape(),
    body('birthYear')
        .optional()
        .isInt({min: 1900, max: 2100}),
    body('gender')
        .optional()
        .isIn(['Nam', 'Nữ', 'Khác']),
    body('university')
        .optional()
        .trim()
        .escape(),
    body('major')
        .optional()
        .trim()
        .escape(),

    catchValidateError,
]


export const update = [
    param('attendeeId')
        .isInt({min: 0})
        .withMessage('attendeeId không hợp lệ'),

    body('fullname')
        .optional()
        .trim()
        .escape(),
    body('birthYear')
        .optional()
        .isInt({min: 1900, max: 2100}),
    body('gender')
        .optional()
        .isIn(['Nam', 'Nữ', 'Khác']),
    body('university')
        .optional()
        .trim()
        .escape(),
    body('major')
        .optional()
        .trim()
        .escape(),

    catchValidateError,
]


export const remove = [
    body('attendeeIds')
        .isArray({min: 1})
        .withMessage('attendeeIds phải là mảng khác rỗng'),

    catchValidateError,
]
