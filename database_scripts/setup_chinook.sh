#!/bin/bash

# Install PostgreSQL (uncomment if PostgreSQL is not already installed)
# brew install postgresql

# Start the PostgreSQL service
# brew services start postgresql

# Create the PostgreSQL user 'postgres' if it doesn't exist
create_user_output=$(psql postgres -tAc "SELECT 1 FROM pg_roles WHERE rolname='postgres'")
if [ "$create_user_output" != "1" ]; then
    createuser -s postgres
fi

# Set up the PostgreSQL user password
psql -U postgres -c "ALTER USER postgres PASSWORD 'sqldbai';"

# Define the database name
DB_NAME="chinook"

# Drop the database if it exists
psql -U postgres -c "DROP DATABASE IF EXISTS $DB_NAME;"

# Create the database
psql -U postgres -c "CREATE DATABASE $DB_NAME;"

# Connect to the database and execute the SQL script
psql -U postgres -d $DB_NAME -f database_scripts/Chinook_PostgreSql.sql
