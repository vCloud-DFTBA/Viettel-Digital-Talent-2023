import {Router} from 'express';

import { paginationValidator } from 'middlewares';
import * as attendeeController from './attendee.controller';
import * as attendeeValidator from './attendee.validator';


export const attendeeRouter = Router();


attendeeRouter.get('/attendee',
    paginationValidator,
    attendeeController.all,
)


attendeeRouter.get('/attendee/:attendeeId',
    attendeeValidator.getById,
    attendeeController.getById,
)


attendeeRouter.post('/attendee',
    attendeeValidator.create,
    attendeeController.create,
)


attendeeRouter.put('/attendee/:attendeeId',
    attendeeValidator.update,
    attendeeController.update,
)


attendeeRouter.delete('/attendee',
    attendeeValidator.remove,
    attendeeController.remove,
)
