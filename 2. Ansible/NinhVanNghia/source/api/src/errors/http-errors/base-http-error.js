export class BaseHttpError extends Error {
    constructor(message) {
        super(message);

        Object.setPrototypeOf(this, BaseHttpError.prototype);
    }
}
