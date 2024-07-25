import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from query_generator import generate_sql_query
from data_retrieval import execute_sql_query
from visualization import plot_data

# Set the page config to wide mode
st.set_page_config(page_title="High-Tech SQL Chat", layout="wide")

# Sidebar for schema updates and settings
with st.sidebar:
    st.title("Settings & Schema Updates")
    st.markdown("## Update Database Schema")
    # Option to upload a new schema file
    schema_file = st.file_uploader("Upload new schema", type=["sql", "csv"])
    
    if schema_file:
        st.success("Schema file uploaded successfully!")
    
    st.markdown("---")
    st.markdown("## Application Settings")
    # Options to customize the visualization
    theme = st.selectbox("Select Theme", ["Light", "Dark"])
    st.color_picker("Choose Primary Color", "#00f900")
    st.markdown("---")

# Main interface
st.title("Chat with PostgreSQL Data")
st.markdown("### Enter your query in natural language:")
user_query = st.text_area("Your query here...", height=100)

# If the user submits a query
if st.button("Submit Query"):
    if user_query:
        st.markdown("### Generated SQL Query:")
        sql_query = generate_sql_query(user_query)
        st.code(sql_query, language="sql")
        
        # Execute the SQL query
        data = execute_sql_query(sql_query)
        
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
    else:
        st.error("Please enter a query to proceed.")

# Adding interactive elements
with st.expander("See Advanced Options"):
    st.markdown("### Advanced Query Options")
    max_rows = st.slider("Select max rows to display", 10, 100, 20)
    show_raw_data = st.checkbox("Show raw data")
    
    if show_raw_data and 'data' in locals():
        st.markdown("### Raw Data")
        st.write(data.head(max_rows))

st.markdown("---")
st.markdown("## Recent Queries")
recent_queries = ["Show top 10 albums", "List all artists", "Find tracks by genre"]
selected_query = st.selectbox("Select a recent query", recent_queries)

if st.button("Use Selected Query"):
    st.text_area("Your query here...", value=selected_query, height=100, key="recent_query")

# Footer with additional information
st.markdown("---")
st.markdown("### About this App")
st.info("This application allows you to interact with a PostgreSQL database using natural language queries. Built with Streamlit, OpenAI, and LangChain.")

# Displaying current settings in the sidebar
with st.sidebar:
    st.markdown("### Current Settings")
    st.write(f"Theme: {theme}")
    st.write(f"Primary Color: {st.session_state.get('color_picker', '#00f900')}")
