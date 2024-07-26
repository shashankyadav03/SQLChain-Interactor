import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from services.query_generator import generate_sql_query
from services.data_retrieval import execute_sql_query, get_table_schema
from services.visualization import plot_data
import os

# Set the page config to wide mode
st.set_page_config(page_title="SQL Chat", layout="wide")

# Initialize session state for user_query and data
if 'user_query' not in st.session_state:
    st.session_state.user_query = ""

if 'data' not in st.session_state:
    st.session_state.data = pd.DataFrame()

# Sidebar for schema updates and settings
with st.sidebar:
    # Option to upload a new schema file
    st.markdown("## Database Schema")
    
    schema_file = st.file_uploader("Upload New Schema", type=["sql", "csv"], key="schema_file_uploader", accept_multiple_files=False)
    
    if schema_file:
        st.success("Schema file uploaded successfully!")
        # Update the schema file if it already exists
        if os.path.exists("utilities/temp/schema.sql"):
            os.remove("utilities/temp/schema.sql")

        # Save the uploaded .sql file to a temporary location
        with open("utilities/temp/schema.sql", "wb") as file:
            file.write(schema_file.getvalue())

# Schema section in sidebar
with st.sidebar:
    st.markdown("## Table Schema")
    table_name = st.text_input("Enter table name to view schema")
    if table_name:
        schema_df = get_table_schema(table_name)
        if not schema_df.empty:
            st.write(schema_df)
        else:
            st.error("Table not found or error retrieving schema")

# Recent queries section in the sidebar
with st.sidebar:
    st.markdown("## Recent Queries")
    # Load recent queries from the file
    if os.path.exists("utilities/queries/user_queries.txt"):
        with open("utilities/queries/user_queries.txt", "r") as file:
            recent_queries = file.readlines()
            recent_queries = [query.strip() for query in recent_queries]
    else:
        recent_queries = []

    # Display the recent queries
    if recent_queries:
        query_selected = st.selectbox("Select a recent query", recent_queries)
        if query_selected:
            st.session_state.user_query = query_selected
    else:
        st.info("No recent queries found.")

# Main interface
st.markdown("### Enter your query in natural language:")
user_query = st.text_area("Your query here...", value=st.session_state.user_query, height=50)

# If the user submits a query
if st.button("Submit Query"):
    if user_query:
        with st.spinner("Processing your query..."):
            
            # Check if schema file is uploaded
            if not os.path.exists("utilities/temp/schema.sql"):
                st.error("Please upload a schema file to proceed.")
                st.stop()

            # Read temp/schema.sql from the uploaded file
            with open("utilities/temp/schema.sql", "r") as file:
                schema = file.read()
            # Check if user_query is already in the recent_queries list
            if user_query not in recent_queries:
                recent_queries.append(user_query)
                # Add the user_query to utilities/queries/user_queries.txt
                with open("utilities/queries/user_queries.txt", "a") as file:
                    file.write(user_query + "\n")

            try:
                sql_query = generate_sql_query(user_query, schema)
                st.markdown("### Generated SQL Query:")
                st.code(sql_query, language="sql")
                
                # Execute the SQL query
                data = execute_sql_query(sql_query)
                st.session_state.data = data  # Store the data in session state
                
                if not data.empty:
                    st.markdown("### Query Results:")
                    st.dataframe(data)
                    
                    st.markdown("### Data Visualization:")
                    # Plotting the data using matplotlib
                    fig, ax = plt.subplots()
                    plot_data(data, ax)
                    st.pyplot(fig)
                else:
                    st.error("No data returned from the query. Please try a different query.")
            except Exception as e:
                st.error(f"An error occurred while executing this query: {e}")
    else:
        st.error("Please enter a query to proceed.")

# Adding interactive elements
# Show advanced option only when data is returned
if not st.session_state.data.empty:
    with st.expander("See Advanced Options"):
        st.markdown("### Advanced Query Options")
        max_rows = st.slider("Select max rows to display", 5, 100, 10)
        show_raw_data = st.checkbox("Show raw data")
        
        if show_raw_data:
            st.markdown("### Raw Data")
            st.write(st.session_state.data.head(max_rows))


# Displaying current settings in the sidebar
with st.sidebar:
    st.markdown("---")
    st.markdown("## Application Settings")
    # Options to customize the visualization
    theme = st.selectbox("Select Theme", ["Light", "Dark"])
    if theme == "Dark":
        st.write("Imagine Dark theme")
    else:
        st.write("Imagine Light theme")