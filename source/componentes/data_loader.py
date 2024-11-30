import pandas as pd
import os
import sys
from source.exception import CustomException
from source.custom_logging import logging
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from source.componentes.data_processing import DataProcessing
from source.componentes.model_builder import ModelBuilderConfiguration
from source.componentes.model_builder import ModelBuilder

@dataclass
class DataLoaderConfiguration:
    train_data_path: str = os.path.join('artifacts', "train.csv")
    test_data_path: str = os.path.join('artifacts', "test.csv")
    raw_data_path: str = os.path.join('artifacts', "data.csv")


class DataLoader:
    def __init__(self):
        self.ingestion_config = DataLoaderConfiguration()

    def initiate_DataLoader(self):
        logging.info("Starting Data Loading process.")
        try:
            # Dataset path
            file_path = r'C:\Users\manue\Desktop\DataScience\Datasets\car_sales_preprocessed.csv'

            # Read dataset
            df = pd.read_csv(file_path)
            logging.info('Dataset loaded into DataFrame.')

            # Create artifacts directory if it doesn't exist
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            # Save raw data
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            logging.info("Raw data saved to artifacts.")

            # Train-test split
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            logging.info("Train-test split completed.")

            # Save train and test datasets
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Train and test data saved to artifacts.")

            return self.ingestion_config.train_data_path, self.ingestion_config.test_data_path

        except Exception as e:
            raise CustomException(e, sys)


if __name__ == "__main__":
    obj = DataLoader()
    train_data, test_data = obj.initiate_DataLoader()

    data_processing = DataProcessing()
    train_arr, test_arr, preprocessor_path = data_processing.initiate_DataProcessing(train_data, test_data)

    logging.info(f"Data processing completed. Preprocessor saved at: {preprocessor_path}")

    modeltrainer=ModelBuilder()
    print(modeltrainer.initiate_model_trainer(train_arr,test_arr))

    


    

