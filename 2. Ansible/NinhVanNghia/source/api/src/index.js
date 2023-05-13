import "dotenv/config";

import app from "./app.js";
import { sequelize } from "./models";


async function start() {
    const PORT = process.env.PORT || 8000;

    try {
        await sequelize.authenticate();
        console.log('Connected to database.');
        await sequelize.sync({ alter: true });
        console.log("All models were synchronized successfully.");
    } catch (error) {
        console.error("Unable to connect to the database:", error);
    }

    await import("./init");

    app.listen(PORT, () => {
        console.log(`Listening on Port ${PORT} ...`);
    });
}


start();
