(async () => {
    const fs = await import('fs/promises')
    const {join} = await import('path')
    const { Attendee } = await import('../models')

    const attendees = await fs.readFile(join(__dirname, '/data/attendee-data.json'), 'utf8').then(JSON.parse)

    await Attendee.bulkCreate(attendees, { ignoreDuplicates: true })
})()

