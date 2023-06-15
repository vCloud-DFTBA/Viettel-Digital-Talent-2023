import {BaseHttpError} from './base-http-error';
import {ERROR_CONFLICT} from '../'


export class ConflictError extends BaseHttpError {
    statusCode = 409;

    constructor(message = ERROR_CONFLICT) {
        super(message);

        Object.setPrototypeOf(this, ConflictError.prototype);
    }
  
    respond() {
        return {
            message: [this.message],
        };
    }
}
