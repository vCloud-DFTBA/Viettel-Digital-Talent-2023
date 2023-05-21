import {Router} from 'express';

import { attendeeRouter } from './attendee/attendee.router';


export const apiRouter = Router();


apiRouter.use(attendeeRouter);
