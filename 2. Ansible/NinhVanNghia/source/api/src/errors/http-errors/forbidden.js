import {BaseHttpError} from './base-http-error';
import {ERROR_PERMISISON_DENIED} from '../'


export class ForbiddenError extends BaseHttpError {
    statusCode = 403;

    constructor(message) {
        super(message || ERROR_PERMISISON_DENIED);

        Object.setPrototypeOf(this, ForbiddenError.prototype);
    }
  
    respond() {
        return {
            message: [this.message],
        };
    }
}
