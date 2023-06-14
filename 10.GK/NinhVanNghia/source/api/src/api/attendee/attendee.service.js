import { Attendee } from "models";
import { QueryBuilder } from "helpers";
import dayjs from "dayjs";


export async function all({page, limit}) {
    const query = new QueryBuilder()
        .paginate({page, limit})
        .toQuery()

    const {rows, count} = await Attendee.findAndCountAll(query)

    return {
        total: count,
        page,
        limit,
        attendees: rows,
    }
}


export async function getById({attendeeId}) {
    return await Attendee.findByPk(attendeeId)
}


export async function create({username, fullname, birthYear, gender, university, major}) {
    const [attendee] = await Attendee.bulkCreate([{username, fullname, birthYear, gender, university, major}])
    return attendee
}


export async function update({username, fullname, birthYear, gender, university, major, attendeeId}) {
    await Attendee.update(
        {username, fullname, birthYear, gender, university, major, updatedAt: dayjs()},
        { where: {attendeeId} }
    )
}


export async function remove({attendeeIds}) {
    await Attendee.destroy({ where: {attendeeId: attendeeIds} })
}
