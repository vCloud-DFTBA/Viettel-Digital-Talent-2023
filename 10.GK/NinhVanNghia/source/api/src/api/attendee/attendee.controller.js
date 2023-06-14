import { NotFoundError, ConflictError } from 'errors';
import * as attendeeService from './attendee.service';


export async function all(req, res) {
    const result = await attendeeService.all({...req.query, ...req.user});
    res.send(result);
}


export async function getById(req, res) {
    const attendee = await attendeeService.getById({...req.params});
    if (!attendee) throw new NotFoundError();
    res.send({attendee});
}


export async function create(req, res) {
    const attendee = await attendeeService.create({...req.body})
        .catch(attendeeErrorHandler);
    res.status(201).send({attendee});
}


export async function update(req, res) {
    await attendeeService.update({...req.body, ...req.params})
        .catch(attendeeErrorHandler);
    res.status(204).end()
}


export async function remove(req, res) {
    await attendeeService.remove({...req.body})
    res.status(204).end()
}


// -----------------------------------------------------


function attendeeErrorHandler(error) {
    if (error.name === 'SequelizeUniqueConstraintError')
        throw new ConflictError('username đã tồn tại')

    throw error
}
