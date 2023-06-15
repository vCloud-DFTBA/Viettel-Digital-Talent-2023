(async () => {
    const fs = await import('fs/promises')
    const {resolve} = await import('path')
    const { Attendee } = await import('../models')

    const attendees = await fs.readFile(resolve('src/init/data/attendee-data.json'), 'utf8').then(JSON.parse)

    await Attendee.bulkCreate(attendees, { ignoreDuplicates: true })
})()

