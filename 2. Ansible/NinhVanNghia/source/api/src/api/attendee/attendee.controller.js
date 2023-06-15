import * as attendeeService from './attendee.service';


export async function all(req, res) {
    const result = await attendeeService.all({...req.query, ...req.user});
    res.send(result);
}


export async function getById(req, res) {
    const attendee = await attendeeService.getById({...req.params});
    res.send({attendee});
}


export async function create(req, res) {
    const attendee = await attendeeService.create({...req.body});
    res.status(201).send({attendee});
}


export async function update(req, res) {
    await attendeeService.update({...req.body, ...req.params});
    res.status(204).end()
}


export async function remove(req, res) {
    await attendeeService.remove({...req.body});
    res.status(204).end()
}
