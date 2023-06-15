import {BaseHttpError} from './base-http-error';
import {ERROR_NOT_VALID_PARAMETERS} from '../'


export class BadRequestError extends BaseHttpError {
    statusCode = 400;

    constructor(errors = [{msg: ERROR_NOT_VALID_PARAMETERS}]) {
        super(ERROR_NOT_VALID_PARAMETERS);

        Array.isArray(errors)
            ? this.reason = errors.map(err => err.msg)
            : this.reason = errors || this.message
        

        Object.setPrototypeOf(this, BadRequestError.prototype);
    }

    respond() {
        return {
            message: this.reason
        };
    }
}
