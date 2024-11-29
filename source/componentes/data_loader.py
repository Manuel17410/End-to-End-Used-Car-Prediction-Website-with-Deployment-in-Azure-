import pandas as pd  # Importing pandas for handling data manipulation and reading CSV files
import os  # Importing os for interacting with the file system (creating directories, paths, etc.)
import sys  # Importing sys for handling system-specific parameters and exceptions
from source.exception import CustomException  # Importing custom exception class from the source module
from source.custom_logging import logging  # Importing custom logging functionality for logging events

from sklearn.model_selection import train_test_split  # Importing train_test_split for splitting the dataset
from dataclasses import dataclass  # Importing dataclass to create a simple class for configuration settings

from source.componentes.data_processing import DataProcessing
from source.componentes.data_processing import DataProcessingConfiguration

# Defining a dataclass to store the paths for the training, testing, and raw data CSV files
@dataclass
class DataLoaderConfiguration:
    train_data_path: str = os.path.join('artifacts', "train.csv")  # Path for saving the training dataset
    test_data_path: str = os.path.join('artifacts', "test.csv")  # Path for saving the testing dataset
    raw_data_path: str = os.path.join('artifacts', "data.csv")  # Path for saving the raw dataset

# Creating a class to load, split, and save the data
class DataLoader:
    def __init__(self):
        # Initializing the DataLoader object and creating a configuration instance
        self.ingestion_config = DataLoaderConfiguration()

    def initiate_DataLoader(self):
        # Function to load the data, split it, and save the train/test sets
        logging.info("Data Loading to be started")  # Log information about the data loading process
        try:
            # File path to the dataset (change this if needed)
            file_path = r'C:\Users\manue\Desktop\DataScience\Datasets\car_sales_preprocessed.csv'

            # Reading the dataset from the specified file path into a DataFrame
            df = pd.read_csv(file_path)
            logging.info('Dataset read as dataframe')  # Log that the dataset has been successfully read

            # Create the directory for saving the data if it doesn't exist
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            # Saving the raw data into a CSV file (the original dataset)
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            logging.info("Raw data saved")  # Log that the raw data has been saved

            # Splitting the dataset into training (80%) and testing (20%) sets
            logging.info("Train test split")  # Log that the train/test split is happening
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            # Saving the training set to a CSV file
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            # Saving the testing set to a CSV file
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Data loading and splitting is done")  # Log that the process is complete

            # Returning the file paths of the training and testing datasets
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            # Handling any exceptions that occur during the data loading process
            raise CustomException(e, sys)

# Main block of code to run the DataLoader
if __name__ == "__main__":
    obj = DataLoader()  # Creating an instance of the DataLoader class
    train_data,test_data=obj.initiate_DataLoader()  # Calling the method to start the data loading process

    data_processing=DataProcessing()

    data_transformation=DataProcessing()
    train_arr,test_arr,_=data_transformation.initiate_DataProcessing(train_data,test_data)
    


    

