import { query } from 'express-validator';

import { catchValidateError } from './catch-validate-error';


export const paginationValidator = [
	query('page')
		.optional()
		.isInt({ min: 0 }).withMessage(`Tham số page không hợp lệ`),

	query('limit')
		.optional()
		.isInt({ min: 0, max: 100 }).withMessage(`Limit phải nhỏ hơn 100`),

	catchValidateError,

	parsePagination,
]


// --------------------------------------------------------


function parsePagination(req, res, next) {
	if (!req.query.page) req.query.page = 0
	else req.query.page = parseInt(req.query.page, 10)

	if (!req.query.limit) req.query.limit = 10
	else req.query.limit = parseInt(req.query.limit, 10)

	return next()
}
