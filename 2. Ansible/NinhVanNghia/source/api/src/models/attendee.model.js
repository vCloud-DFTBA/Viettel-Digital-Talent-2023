import {DataTypes, Sequelize} from 'sequelize';

import {sequelize} from './sequelize';


export const Attendee = sequelize.define('attendee',
    {
        attendeeId: {
            type: DataTypes.BIGINT.UNSIGNED,
            primaryKey: true,
            allowNull: false,
        },
        username: {
            type: DataTypes.STRING(50),
            unique: true,
            allowNull: false,
        },
        fullname: {
            type: DataTypes.STRING(100),
            allowNull: false,
        },
        birthYear: {
            type: DataTypes.SMALLINT.UNSIGNED,
        },
        gender: {
            type: DataTypes.STRING(10),
        },
        university: {
            type: DataTypes.STRING(400),
        },
        major: {
            type: DataTypes.STRING(400),
        },
        createdAt: {
            type: DataTypes.DATE,
            defaultValue: Sequelize.literal('CURRENT_TIMESTAMP'),
            allowNull: false,
        },
        updatedAt: {
            type: DataTypes.DATE,
            defaultValue: Sequelize.literal('CURRENT_TIMESTAMP'),
            allowNull: false,
        },
    }, {
        timestamps: false,
    }
)
