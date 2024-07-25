#!/bin/bash

# Create main application file
touch app.py

# Create requirements.txt
touch requirements.txt

# Create .env file
touch .env

# Create utils directory and files within it
mkdir services
cd services
touch query_generator.py
touch data_retrieval.py
touch visualization.py
touch streamlit_ui.py

# Print a message indicating the setup is complete
echo "Project structure created successfully."
