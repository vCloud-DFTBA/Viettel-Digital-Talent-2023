#!/bin/bash
mongoimport --db vdt23 --collection attendee  --drop --type json --jsonArray --file /data/data.json 