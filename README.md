
# SQLChain Interactor

# Chat with PostgreSQL Data using LangChain, OpenAI, and Streamlit

## Overview

This project aims to create a user-friendly interface that allows users to interact with the Chinook PostgreSQL database using natural language. The system leverages OpenAI's API for natural language processing, LangChain's SQL Database Toolkit for translating natural language into SQL queries, and Streamlit for the user interface. The retrieved data is visualized using Matplotlib.

## Features

- **Natural Language Querying**: Users can input questions in natural language, and the system will generate the corresponding SQL query.
- **Data Retrieval**: The system executes the SQL query on the Chinook PostgreSQL database and retrieves the relevant data.
- **Data Visualization**: Retrieved data is visualized using Matplotlib for better understanding and insights.
- **Advanced User Interface**: Built with Streamlit, providing a seamless and interactive user experience.

## Additional Features

- **Error Handling**: Graceful handling of invalid queries or data retrieval errors.
- **Query History**: Logs of previous queries and results for reference.
- **Customizable Visualizations**: Options to customize the type and style of visualizations.
- **User Authentication**: Secure access to the application using user authentication mechanisms.
- **Downloadable Reports**: Option to download query results and visualizations as reports.

## Use Cases

- **Business Intelligence**: Quickly generate insights from the Chinook database without needing to write SQL.
- **Data Analysis**: Visualize trends and patterns in the data with customizable charts.
- **Educational Tool**: Learn and understand SQL querying and data visualization interactively.
- **Ad-Hoc Reporting**: Generate on-demand reports for business or research purposes.

## Getting Started

### Prerequisites

- Python 3.7 or higher
- PostgreSQL database with the Chinook schema
- OpenAI API key
- Required Python packages (listed in `requirements.txt`)

### Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/shashankyadav03/sql-interactor.git
    cd chat-with-postgresql
    ```

2. **Install the required packages:**
    ```sh
    pip install -r requirements.txt
    ```

3. **Set up the Chinook PostgreSQL database:**
    - Download and execute the Chinook PostgreSQL SQL script from [Chinook Database](https://github.com/lerocha/chinook-database/blob/master/ChinookDatabase/DataSources/Chinook_PostgreSql.sql) to set up the database.

4. **Configure environment variables:**
    - Create a `.env` file and add your OpenAI API key:
    ```env
    OPENAI_API_KEY=your_openai_api_key
    DATABASE_URL=postgresql://username:password@localhost:5432/chinook
    ```

### Running the Application

1. **Start the Streamlit application:**
    ```sh
    streamlit run app.py
    ```

2. **Access the application:**
    - Open your web browser and go to `http://localhost:8501`.

## Project Structure

```plaintext
.
├── app.py                     # Main application file
├── requirements.txt           # List of required Python packages
├── README.md                  # Project documentation
├── .env                       # Environment variables
└── utils                      # Utility functions and modules
    ├── query_generator.py     # Module to generate SQL queries from natural language
    ├── data_retrieval.py      # Module to execute SQL queries and retrieve data
    ├── visualization.py       # Module to create visualizations using Matplotlib
    └── streamlit_ui.py        # Module to build the Streamlit user interface
```

## Usage

1. **Enter a natural language query:**
    - Example: "Show me the top 10 selling albums."

2. **View the generated SQL query:**
    - The system will display the SQL query generated from the natural language input.

3. **Retrieve and visualize data:**
    - The retrieved data will be visualized using Matplotlib and displayed on the Streamlit interface.

## Future Enhancements

- **Enhanced Natural Language Understanding**: Improve the accuracy of query generation using more advanced NLP models.
- **Support for More Databases**: Extend support to other SQL databases like MySQL, SQLite, etc.
- **Real-time Collaboration**: Allow multiple users to collaborate and share insights in real-time.
- **Integration with BI Tools**: Integrate with business intelligence tools like Tableau or Power BI for advanced analytics.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss changes.

## License

This project is Unlicensed free to use.

## Acknowledgements

- [LangChain](https://github.com/hwchase17/langchain) for the SQL Database Toolkit.
- [OpenAI](https://openai.com/) for the powerful language model API.
- [Streamlit](https://streamlit.io/) for the easy-to-use web application framework.
- [Chinook Database](https://github.com/lerocha/chinook-database) for the sample database.

---

Feel free to reach out with any questions or feedback!
