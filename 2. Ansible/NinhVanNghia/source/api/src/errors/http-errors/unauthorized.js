import {BaseHttpError} from './base-http-error';
import {ERROR_UNAUTHORIZED} from '../'


export class UnauthorizedError extends BaseHttpError {
    statusCode = 401;
  
    constructor(message) {
        super(message || ERROR_UNAUTHORIZED);

        Object.setPrototypeOf(this, UnauthorizedError.prototype);
    }
  
    respond() {
        return {
            message: [this.message]
        };
    }
}
