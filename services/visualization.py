import matplotlib.pyplot as plt
import pandas as pd

def plot_data(data, ax=None):
    """
    Create a visualization for the given data.

    Parameters:
        data (pd.DataFrame): The data to visualize.
        ax (matplotlib.axes.Axes, optional): The axes to plot on. Defaults to None.

    Returns:
        None: The function will plot the data on the provided axes or create a new figure.
    """
    if ax is None:
        fig, ax = plt.subplots()

    # Identify the type of data to determine the best plot type
    if data.empty:
        ax.text(0.5, 0.5, 'No data to display', horizontalalignment='center', verticalalignment='center')
        return

    # Check for numerical columns
    numerical_cols = data.select_dtypes(include=['number']).columns.tolist()
    
    if len(numerical_cols) == 0:
        ax.text(0.5, 0.5, 'No numerical data to display', horizontalalignment='center', verticalalignment='center')
        return

    # Check for categorical columns
    categorical_cols = data.select_dtypes(include=['object', 'category']).columns.tolist()

    if len(numerical_cols) == 1 and len(categorical_cols) >= 1:
        # Plotting a bar chart for a single numerical column with categories
        for cat_col in categorical_cols:
            ax.bar(data[cat_col], data[numerical_cols[0]])
            ax.set_xlabel(cat_col)
            ax.set_ylabel(numerical_cols[0])
            ax.set_title(f'Bar chart of {numerical_cols[0]} by {cat_col}')
            ax.tick_params(axis='x', rotation=90)
            break

    elif len(numerical_cols) == 2:
        # Plotting a scatter plot for two numerical columns
        ax.scatter(data[numerical_cols[0]], data[numerical_cols[1]])
        ax.set_xlabel(numerical_cols[0])
        ax.set_ylabel(numerical_cols[1])
        ax.set_title(f'Scatter plot of {numerical_cols[0]} vs {numerical_cols[1]}')

    elif len(numerical_cols) > 2:
        # Plotting a pair plot if there are more than two numerical columns
        pd.plotting.scatter_matrix(data[numerical_cols], ax=ax)
        plt.suptitle('Scatter matrix of numerical columns')

    else:
        ax.text(0.5, 0.5, 'Unable to determine appropriate plot', horizontalalignment='center', verticalalignment='center')

def plot_time_series(data, date_col, value_col, ax=None):
    """
    Create a time series plot for the given data.

    Parameters:
        data (pd.DataFrame): The data to visualize.
        date_col (str): The name of the column containing date information.
        value_col (str): The name of the column containing values to plot.
        ax (matplotlib.axes.Axes, optional): The axes to plot on. Defaults to None.

    Returns:
        None: The function will plot the data on the provided axes or create a new figure.
    """
    if ax is None:
        fig, ax = plt.subplots()

    # Convert the date column to datetime
    data[date_col] = pd.to_datetime(data[date_col])

    # Plotting the time series
    ax.plot(data[date_col], data[value_col])
    ax.set_xlabel('Date')
    ax.set_ylabel(value_col)
    ax.set_title(f'Time Series of {value_col} over {date_col}')
    ax.tick_params(axis='x', rotation=45)

def plot_histogram(data, col, ax=None):
    """
    Create a histogram for the given column.

    Parameters:
        data (pd.DataFrame): The data to visualize.
        col (str): The name of the column to plot.
        ax (matplotlib.axes.Axes, optional): The axes to plot on. Defaults to None.

    Returns:
        None: The function will plot the data on the provided axes or create a new figure.
    """
    if ax is None:
        fig, ax = plt.subplots()

    # Plotting the histogram
    ax.hist(data[col], bins=20, edgecolor='black')
    ax.set_xlabel(col)
    ax.set_ylabel('Frequency')
    ax.set_title(f'Histogram of {col}')

def plot_pie_chart(data, col, ax=None):
    """
    Create a pie chart for the given column.

    Parameters:
        data (pd.DataFrame): The data to visualize.
        col (str): The name of the column to plot.
        ax (matplotlib.axes.Axes, optional): The axes to plot on. Defaults to None.

    Returns:
        None: The function will plot the data on the provided axes or create a new figure.
    """
    if ax is None:
        fig, ax = plt.subplots()

    # Plotting the pie chart
    data[col].value_counts().plot.pie(ax=ax, autopct='%1.1f%%', startangle=90)
    ax.set_ylabel('')
    ax.set_title(f'Pie Chart of {col}')

