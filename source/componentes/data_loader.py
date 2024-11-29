import pandas as pd
import os
import sys
from source.exception import CustomException
from source.custom_logging import logging

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataLoaderConfiguration:
    train_data_path: str=os.path.join('artifacts',"train.csv")
    test_data_path: str=os.path.join('artifacts',"test.csv")
    raw_data_path: str=os.path.join('artifacts',"data.csv")

class DataLoader:
    def __init__(self):
        self.ingestion_config=DataLoaderConfiguration()

    def initiate_DataLoader(self):
        logging.info("Data Loading to be started")
        try:
            file_path = r'C:\Users\manue\Desktop\DataScience\Datasets\car_web_scraped_dataset.csv'
            df = pd.read_csv(file_path)
            logging.info('dataset to be read as dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info("Train test split")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)

            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Loading is done")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path

            )
        except Exception as e:
            raise CustomException(e,sys)
        
if __name__=="__main__":
    obj=DataLoader()
    obj.initiate_DataLoader()