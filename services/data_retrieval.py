import os
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from dotenv import load_dotenv

# Database connection details
DB_USER = "postgres"
DB_PASSWORD = "your_password"
DB_NAME = "chinook"
DB_HOST = "localhost"
DB_PORT = "5432"

# Create the database connection string
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Load environment variables from .env file
load_dotenv()
    

def get_db_engine():
    """Create a SQLAlchemy engine."""
    try:
        engine = create_engine(DATABASE_URL)
        return engine
    except SQLAlchemyError as e:
        print(f"Error creating database engine: {e}")
        return None

def execute_sql_query(query):
    """
    Execute an SQL query and return the results as a pandas DataFrame.

    Parameters:
        query (str): The SQL query to execute.

    Returns:
        pd.DataFrame: The results of the query as a pandas DataFrame.
    """
    engine = get_db_engine()
    if engine is None:
        return pd.DataFrame()  # Return an empty DataFrame if engine creation failed

    try:
        with engine.connect() as connection:
            df = pd.read_sql_query(query, connection)
        return df
    except SQLAlchemyError as e:
        print(f"Error executing query: {e}")
        return pd.DataFrame()  # Return an empty DataFrame in case of error

def get_table_schema(table_name):
    """
    Retrieve the schema of a specified table.

    Parameters:
        table_name (str): The name of the table whose schema to retrieve.

    Returns:
        pd.DataFrame: The schema of the table as a pandas DataFrame.
    """
    query = f"""
    SELECT column_name, data_type 
    FROM information_schema.columns 
    WHERE table_name = '{table_name}'
    """

    engine = get_db_engine()
    if engine is None:
        return pd.DataFrame()  # Return an empty DataFrame if engine creation failed

    try:
        with engine.connect() as connection:
            df = pd.read_sql_query(query, connection)
        return df
    except SQLAlchemyError as e:
        print(f"Error retrieving table schema: {e}")
        return pd.DataFrame()  # Return an empty DataFrame in case of error
