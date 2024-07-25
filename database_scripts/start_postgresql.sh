#!/bin/bash

# Define the database name
DB_NAME="chinook"

# Connect to the database and list all tables
psql -U postgres -d $DB_NAME -c "\dt"

psql -U postgres -d $DB_NAME 