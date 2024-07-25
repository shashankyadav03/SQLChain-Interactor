import os
import pandas as pd
import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get database connection details from environment variables
DATABASE_URL = os.getenv("DATABASE_URL")

def get_db_connection():
    """Establish a connection to the PostgreSQL database."""
    try:
        conn = psycopg2.connect(DATABASE_URL)
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None

def execute_sql_query(query):
    """
    Execute an SQL query and return the results as a pandas DataFrame.

    Parameters:
        query (str): The SQL query to execute.

    Returns:
        pd.DataFrame: The results of the query as a pandas DataFrame.
    """
    conn = get_db_connection()
    if conn is None:
        return pd.DataFrame()  # Return an empty DataFrame if connection failed

    try:
        df = pd.read_sql_query(query, conn)
        return df
    except Exception as e:
        print(f"Error executing query: {e}")
        return pd.DataFrame()  # Return an empty DataFrame in case of error
    finally:
        conn.close()

def get_table_schema(table_name):
    """
    Retrieve the schema of a specified table.

    Parameters:
        table_name (str): The name of the table whose schema to retrieve.

    Returns:
        pd.DataFrame: The schema of the table as a pandas DataFrame.
    """
    query = sql.SQL(
        "SELECT column_name, data_type FROM information_schema.columns WHERE table_name = {table}"
    ).format(table=sql.Identifier(table_name))

    conn = get_db_connection()
    if conn is None:
        return pd.DataFrame()  # Return an empty DataFrame if connection failed

    try:
        df = pd.read_sql_query(query, conn)
        return df
    except Exception as e:
        print(f"Error retrieving table schema: {e}")
        return pd.DataFrame()  # Return an empty DataFrame in case of error
    finally:
        conn.close()
