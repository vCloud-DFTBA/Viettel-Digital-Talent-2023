import {BaseHttpError} from './base-http-error';
import {ERROR_NOT_FOUND} from '../'


export class NotFoundError extends BaseHttpError {
    statusCode = 404;
  
    constructor(message) {
        super(message || ERROR_NOT_FOUND);

        Object.setPrototypeOf(this, NotFoundError.prototype);
    }
  
    respond() {
        return {
            message: [this.message],
        };
    }
}
