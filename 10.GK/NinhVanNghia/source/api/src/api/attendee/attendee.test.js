import { api } from "__test__"
import { Attendee } from "models"


const attendees = [
    {
        username: 'nghianv',
        fullname: 'Ninh Van Nghia',
        birthYear: 2001,
        gender: 'Nam',
        university: 'Dai hoc BKHN',
        major: 'Khoa hoc may tinh',
    },
    {
        username: 'annt',
        fullname: 'Nguyen Thị An',
        birthYear: 2002,
        gender: 'Nữ',
        university: 'UET',
        major: 'Khoa hoc may tinh',
    },
]


describe('Test GET /attendee', () => {
    test('It should response 200', async () => {
        await Attendee.bulkCreate(attendees)
        const {statusCode, body} = await api.get('/api/v1/attendee')

        expect(statusCode).toBe(200)
        expect(body?.attendees.length).toBe(2)
        expect(body.attendees.map(a => a.username)).toContain( 'annt', 'nghianv')
    })
})


describe('Test GET /attendee/:attendeeId', () => {
    test('It should response 404', async () => {
        const {statusCode} = await api.get(`/api/v1/attendee/9999`)
        expect(statusCode).toBe(404)
    })

    test('It should response 200', async () => {
        const [attendee] = await Attendee.bulkCreate(attendees)
        const {statusCode, body} = await api.get(`/api/v1/attendee/${attendee.attendeeId}`)

        expect(statusCode).toBe(200)
        expect(body.attendee.username).toBe(attendee.username)
    })
})


describe('Test POST /attendee', () => {
    test('It should catch Bad Request', async () => {
        const {statusCode, body} = await api
            .post('/api/v1/attendee')
            .send({
                username: '  ',
                fullname: '  ',
                birthYear: 1000,
                gender: 'Not Valid Gender',
            })

        expect(statusCode).toBe(400)
    })

    test('It should catch Conflict Creation', async () => {
        await Attendee.create(attendees[0])
        const {statusCode, body} = await api
            .post('/api/v1/attendee')
            .send({
                username: 'nghianv',
                fullname: 'Ninh Van Nghia 2',
                birthYear: 1900,
                gender: 'Nữ',
            })

        expect(statusCode).toBe(409)
    })

    test('It should create', async () => {
        const {statusCode, body} = await api
            .post('/api/v1/attendee')
            .send(attendees[0])
        
        const createdAttendee = await Attendee.findOne({
            attributes: {exclude: ['attendeeId', 'createdAt', 'updatedAt']},
            where: {username: attendees[0].username},
            raw: true
        })

        expect(statusCode).toBe(201)
        expect(createdAttendee).toEqual(attendees[0])
    })
})


describe('Test PUT /attendee/:attendeeId', () => {
    test('It should catch Bad Request', async () => {
        await Attendee.create(attendees[0])
        const {statusCode} = await api
            .put('/api/v1/attendee/1')
            .send({
                username: '  ',
                fullname: '  ',
                birthYear: 1000,
                gender: 'Not Valid Gender',
            })

        expect(statusCode).toBe(400)
    })

    test('It should catch Username Conflict', async () => {
        const [a1, a2] = await Attendee.bulkCreate(attendees)
        const {statusCode} = await api
            .put(`/api/v1/attendee/${a2.attendeeId}`)
            .send({ username: a1.username })

        expect(statusCode).toBe(409)
    })

    test('It should update', async () => {
        await Attendee.create(attendees[0])
        const {statusCode} = await api
            .put('/api/v1/attendee/1')
            .send({
                username: 'nghianv2',
                fullname: 'Ninh Van Nghia 2',
                birthYear: 1900,
                gender: 'Nữ',
            })

        expect(statusCode).toBe(204)
    })
})


describe('Test DELETE /attendee', () => {
    test('It should delete', async () => {
        const [{attendeeId}] = await Attendee.bulkCreate(attendees)
        const {statusCode} = await api
            .delete('/api/v1/attendee')
            .send({attendeeIds: [attendeeId]})

        const afterDelete = await Attendee.findAll({})

        expect(statusCode).toBe(204)
        expect(afterDelete.length).toBe(1)
    })
})
