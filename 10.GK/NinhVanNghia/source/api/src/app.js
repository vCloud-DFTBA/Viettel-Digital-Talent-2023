import express from 'express';
import 'express-async-errors';
import cors from 'cors';
import morgan from 'morgan';

import { apiRouter } from 'api';
import { errorHandler } from 'middlewares';


const app = express().disable('x-powered-by');


app.set('trust proxy', 1)


// Common Middlewares
app.use(morgan(':remote-addr :date[iso] :method :url  :status  :response-time ms'))
app.use(cors('*'));
app.use(express.json({ limit: '10mb' }));
app.use(express.urlencoded({ extended: true, limit: '10mb' }));


// Custom Middlewares
app.use("/api/v1", apiRouter);
app.use("/", (req, res) => res.send('pong'));
app.use(errorHandler);


export default app;
