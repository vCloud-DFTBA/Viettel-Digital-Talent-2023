import {sequelize} from 'models'


global.beforeAll(() => sequelize.sync({force: true}))

global.afterEach(async () => {
    await sequelize.truncate({ truncate: true, cascade: true, restartIdentity: true })
});
