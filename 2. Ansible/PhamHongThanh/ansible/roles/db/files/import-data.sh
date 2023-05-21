#!/bin/bash
mongoimport --db vdt23 --collection attendee --authenticationDatabase admin --username thanh --password thanh --drop --type json --jsonArray --file /data/data.json 