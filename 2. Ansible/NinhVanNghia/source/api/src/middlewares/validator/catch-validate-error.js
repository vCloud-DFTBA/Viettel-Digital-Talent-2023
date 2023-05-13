import {validationResult} from 'express-validator';

import {BadRequestError} from '../../errors';


export function catchValidateError(req, res, next) {
    const errors = validationResult(req);

    if (!errors.isEmpty()) {
        throw new BadRequestError(errors.array());
    }

    next();
};
