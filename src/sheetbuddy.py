# eda/sheetbuddy.py

import time
import pandas as pd
import requests
from io import StringIO
from tqdm import tqdm
import openpyxl
from openpyxl.styles import PatternFill, Alignment, Font
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Expanded predefined dictionary for column descriptions
COLUMN_DESCRIPTIONS = {
    'name': 'The name of the individual or entity.',
    'age': 'The age of the individual.',
    'date': 'The date of the event or record.',
    'salary': 'The salary of the individual.',
    'country': 'The country associated with the record.',
    'city': 'The city associated with the record.',
    'gender': 'The gender of the individual.',
    'email': 'The email address of the individual or entity.',
    'phone': 'The phone number of the individual or entity.',
    'id': 'The unique identifier for the record.',
    'address': 'The street address of the individual or entity.',
    'zip code': 'The postal code for the address.',
    'state': 'The state or province associated with the record.',
    'department': 'The department within the organization.',
    'position': 'The job title or position of the individual.',
    'hire date': 'The date the individual was hired.',
    'birthdate': 'The birthdate of the individual.',
    'score': 'A score or rating associated with the individual or entity.',
    'status': 'The current status of the record.',
    'comment': 'Additional comments or notes about the record.',
    'category': 'The category or classification of the record.',
    'type': 'The type or nature of the record.',
    'quantity': 'The quantity associated with the record.',
    'price': 'The price or cost associated with the record.',
    'discount': 'Any discount applied to the price.',
    'total': 'The total amount for the record.',
    'description': 'A detailed description of the record.',
    'product': 'The product name or identifier.',
    'service': 'The service name or identifier.',
    'rating': 'A rating or review score for the record.',
    'review': 'A written review or feedback for the record.',
    'tag': 'A tag or label associated with the record.',
    'timestamp': 'The date and time when the record was created or updated.',
    'username': 'The username associated with the individual or entity.',
    'password': 'The password associated with the individual or entity.',
    'role': 'The role or permissions associated with the individual.',
    'group': 'The group or team associated with the individual.',
    'session': 'The session identifier for the record.',
    # Add any additional column descriptions if needed
}

class SheetBuddy:
    """
    A class to handle various EDA (Exploratory Data Analysis) operations on datasets.

    Attributes:
    -----------
    file_path_or_url : str
        The file path or URL to the dataset.

    Methods:
    --------
    read_csv():
        Reads a CSV file into a DataFrame.
    
    read_json(url):
        Reads JSON data from a URL into a DataFrame.
    
    read_data():
        Determines the file type and reads the data accordingly.
    
    generate_eda_report(file_name):
        Generates an EDA report and saves it to an Excel file.
    
    style_excel_sheet(sheet):
        Styles the Excel sheet with formatting.
    
    get_column_info():
        Retrieves information about the columns in the dataset.
    
    get_shape():
        Retrieves the shape (dimensions) of the dataset.
    
    get_summary_statistics():
        Retrieves summary statistics of the dataset.
    
    get_null_values():
        Retrieves the count of null values for each column.
    
    get_null_percentage():
        Retrieves the percentage of null values for each column.
    
    get_standard_deviation():
        Retrieves the standard deviation for numerical columns.
    
    get_unique_values():
        Retrieves the count of unique values for each column.
    
    get_most_frequent_values():
        Retrieves the most frequent value for each column.
    
    get_basic_math():
        Retrieves basic mathematical calculations for numerical columns.
    """
    
    def __init__(self, file_path_or_url):
        """
        Initializes the SheetBuddy class with the file path or URL to the dataset.

        Parameters:
        -----------
        file_path_or_url : str
            The file path or URL to the dataset.
        """
        self.file_path_or_url = file_path_or_url
        self.data = self.read_data()

    def read_csv(self):
        """
        Reads a CSV file into a DataFrame.

        Returns:
        --------
        DataFrame
            The dataset read from the CSV file.
        """
        try:
            if self.file_path_or_url.startswith("http"):
                response = requests.get(self.file_path_or_url)
                response.raise_for_status()
                data = StringIO(response.text)
                return pd.read_csv(data, encoding='unicode_escape')
            else:
                return pd.read_csv(self.file_path_or_url, encoding='unicode_escape')
        except Exception as e:
            logging.error(f"Error reading CSV file: {e}")
            return None

    def read_json(self, url):
        """
        Reads JSON data from a URL into a DataFrame.

        Parameters:
        -----------
        url : str
            The URL to the JSON data.

        Returns:
        --------
        DataFrame
            The dataset read from the JSON URL.
        """
        try:
            response = requests.get(url)
            response.raise_for_status()
            json_data = response.text
            # Attempt to load the JSON data, handle trailing data issue
            try:
                data = pd.read_json(StringIO(json_data))
            except ValueError as e:
                logging.error(f"Initial JSON read error: {e}. Attempting to clean data...")
                # Remove trailing data and try again
                json_data = json_data.strip().rstrip(',}')
                data = pd.read_json(StringIO(json_data))
            return data
        except Exception as e:
            logging.error(f"Error reading JSON data from URL: {e}")
            return None

    def read_data(self):
        """
        Determines the file type (CSV or JSON) and reads the data accordingly.

        Returns:
        --------
        DataFrame
            The dataset read from the file or URL.
        """
        for _ in tqdm(range(100), desc="Loading data..."):
            time.sleep(0.05)  # Simulate some delay for progress bar

        if self.file_path_or_url.endswith('.csv') or self.file_path_or_url.startswith("http"):
            data = self.read_csv()
        elif self.file_path_or_url.endswith('.json'):
            data = self.read_json(self.file_path_or_url)
        else:
            logging.error("Unsupported file format. Please provide a CSV or JSON file.")
            data = None

        return data

    def generate_eda_report(self, file_name):
        """
        Generates an EDA report and saves it to an Excel file.

        Parameters:
        -----------
        file_name : str
            The name of the output Excel file.
        """
        logging.info("Loading data...")
        if self.data is not None:
            logging.info("Data loaded successfully.")
            logging.info("Generating report...")

            with pd.ExcelWriter(file_name, engine='openpyxl') as writer:
                # Write Column Info
                column_info = self.get_column_info()
                column_info.to_excel(writer, sheet_name='Column Info', index=False)

                # Write Shape Info
                shape_info = pd.DataFrame({'Shape': [self.get_shape()]})
                shape_info.to_excel(writer, sheet_name='Shape Info', index=False)

                # Write Summary Statistics
                summary_stats = self.get_summary_statistics().reset_index()
                summary_stats.to_excel(writer, sheet_name='Summary Statistics', index=False)

                # Write Null Values
                null_values = self.get_null_values().reset_index()
                null_values.columns = ['Column', 'Null Values']
                null_values.to_excel(writer, sheet_name='Null Values', index=False)

                # Write Null Percentage
                null_percentage = self.get_null_percentage().reset_index()
                null_percentage.columns = ['Column', 'Null Percentage']
                null_percentage.to_excel(writer, sheet_name='Null Percentage', index=False)

                # Write Standard Deviation
                std_dev = self.get_standard_deviation().reset_index()
                std_dev.columns = ['Column', 'Standard Deviation']
                std_dev.to_excel(writer, sheet_name='Standard Deviation', index=False)

                # Write Unique Values
                unique_values = self.get_unique_values().reset_index()
                unique_values.columns = ['Column', 'Unique Values']
                unique_values.to_excel(writer, sheet_name='Unique Values', index=False)

                # Write Most Frequent Values
                most_frequent_values = self.get_most_frequent_values().reset_index()
                most_frequent_values.columns = ['Column', 'Most Frequent Value']
                most_frequent_values.to_excel(writer, sheet_name='Most Frequent Values', index=False)

                # Write Correlation Matrix
                numerical_data = self.data.select_dtypes(include=['number'])
                correlation_matrix = numerical_data.corr()
                correlation_matrix.to_excel(writer, sheet_name='Correlation Matrix')

                # Write Basic Mathematics
                basic_math = self.get_basic_math().reset_index()
                basic_math.to_excel(writer, sheet_name='Basic Mathematics', index=False)

                # Style all sheets
                workbook = writer.book
                for sheet_name in workbook.sheetnames:
                    sheet = workbook[sheet_name]
                    self.style_excel_sheet(sheet)

            logging.info(f"Report generated: {file_name}")

        else:
            logging.error("Failed to load data. Report generation aborted.")

    def style_excel_sheet(self, sheet):
        """
        Styles the Excel sheet with formatting.

        Parameters:
        -----------
        sheet : openpyxl.worksheet.worksheet.Worksheet
            The Excel sheet to be styled.
        """
        header_fill = PatternFill(start_color='4B4B4B', end_color='4B4B4B', fill_type='solid')
        header_font = Font(color='FFFFFF', bold=True, size=12)  # White font color, bold, increased size
        center_alignment = Alignment(horizontal='center', vertical='center')
        row_fill = PatternFill(start_color='D3D3D3', end_color='D3D3D3', fill_type='solid')

        for row in sheet.iter_rows():
            for cell in row:
                cell.alignment = center_alignment
                if cell.row == 1:  # Header row
                    cell.fill = header_fill
                    cell.font = header_font
                elif cell.row % 2 == 0:  # Apply alternating row color
                    cell.fill = row_fill

    def get_column_info(self):
        """
        Retrieves information about the columns in the dataset.

        Returns:
        --------
        DataFrame
            A DataFrame containing the column names, data types, descriptions, and whether they are categorical or numerical.
        """
        normalized_columns = [col.lower().replace('_', ' ') for col in self.data.columns]
        descriptions = [COLUMN_DESCRIPTIONS.get(col, None) for col in normalized_columns]
        return pd.DataFrame({
            'Column': self.data.columns,
            'Data Type': self.data.dtypes,
            'Description': descriptions,
            'Categorical/Numerical': ['Categorical' if self.data[col].dtype == 'object' else 'Numerical' for col in self.data.columns]
        })

    def get_shape(self):
        """
        Retrieves the shape (dimensions) of the dataset.

        Returns:
        --------
        tuple
            The shape of the dataset as a tuple (rows, columns).
        """
        return self.data.shape

    def get_summary_statistics(self):
        """
        Retrieves summary statistics of the dataset.

        Returns:
        --------
        DataFrame
            The summary statistics of the dataset.
        """
        try:
            return self.data.describe()
        except Exception as e:
            logging.error(f"Error generating summary statistics: {e}")
            return pd.DataFrame()

    def get_null_values(self):
        """
        Retrieves the count of null values for each column.

        Returns:
        --------
        Series
            A series containing the count of null values for each column.
        """
        return self.data.isnull().sum()

    def get_null_percentage(self):
        """
        Retrieves the percentage of null values for each column.

        Returns:
        --------
        Series
            A series containing the percentage of null values for each column.
        """
        return self.data.isnull().mean() * 100

    def get_standard_deviation(self):
        """
        Retrieves the standard deviation for numerical columns.

        Returns:
        --------
        Series
            A series containing the standard deviation for each numerical column.
        """
        try:
            numerical_data = self.data.select_dtypes(include=['number'])
            return numerical_data.std()
        except Exception as e:
            logging.error(f"Error calculating standard deviation: {e}")
            return pd.Series()

    def get_unique_values(self):
        """
        Retrieves the count of unique values for each column.

        Returns:
        --------
        Series
            A series containing the count of unique values for each column.
        """
        return self.data.nunique()

    def get_most_frequent_values(self):
        """
        Retrieves the most frequent value for each column.

        Returns:
        --------
        Series
            A series containing the most frequent value for each column.
        """
        try:
            return self.data.mode().iloc[0]
        except Exception as e:
            logging.error(f"Error finding most frequent values: {e}")
            return pd.Series()

    def get_basic_math(self):
        """
        Retrieves basic mathematical calculations for numerical columns.

        Returns:
        --------
        DataFrame
            A DataFrame containing mean, median, mode, and range for each numerical column.
        """
        try:
            numerical_data = self.data.select_dtypes(include=['number'])
            return pd.DataFrame({
                'Mean': numerical_data.mean(),
                'Median': numerical_data.median(),
                'Mode': numerical_data.mode().iloc[0],
                'Range': numerical_data.max() - numerical_data.min()
            })
        except Exception as e:
            logging.error(f"Error calculating basic mathematics: {e}")
            return pd.DataFrame()
