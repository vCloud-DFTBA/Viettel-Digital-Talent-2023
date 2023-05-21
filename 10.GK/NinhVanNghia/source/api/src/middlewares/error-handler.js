import {ValidationError} from 'sequelize';

import {BaseHttpError, ERROR_INTERNAL, ERROR_NOT_VALID_PARAMETERS} from 'errors';


export async function errorHandler(err, req, res, next) {
    if (err instanceof BaseHttpError) return res.status(err.statusCode).send(err.respond());

    console.error(err);

    if (err instanceof ValidationError) return res.status(400).send({message: [ERROR_NOT_VALID_PARAMETERS]});

    res.status(500).send({
        message: ERROR_INTERNAL,
    })
}
