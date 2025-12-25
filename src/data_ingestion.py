import os 
import pandas as pd
import sys
from google.cloud import storage
from sklearn.model_selection import train_test_split
from src.logger import get_logger
from src.custom_exception import CustomException
from config.paths_config import RAW_DIR, RAW_File_Path, Train_File_Path, Test_File_Path
from utils.common_functions import read_yaml_file

logger = get_logger(__name__)

class DataIngestion:
    def __init__(self, config_path: str):
        self.config = read_yaml_file(config_path)
        self.bucket_name = self.config['data_ingestion']['bucket_name']
        self.bucket_file_name = self.config['data_ingestion']['bucket_file_name']
        self.train_ratio = self.config['data_ingestion']['train_ratio']

        os.makedirs(RAW_DIR, exist_ok=True)

        logger.info("DataIngestion instance created with configuration.")

    def download_data_from_gcs(self) -> str:
        """Downloads data from Google Cloud Storage and saves it locally."""
        try:
            os.makedirs(RAW_DIR, exist_ok=True)
            client = storage.Client()
            bucket = client.bucket(self.bucket_name)
            blob = bucket.blob(self.bucket_file_name)
            blob.download_to_filename(RAW_File_Path)
            logger.info(f"Data downloaded from GCS bucket {self.bucket_name} to {RAW_File_Path}")
            return RAW_File_Path
        except Exception as e:
            logger.error(f"Error downloading data from GCS: {e}")
            raise CustomException("Error downloading data from GCS", sys) from e

    def split_data(self, file_path: str):
        """Splits the data into training and testing sets."""
        try:
            df = pd.read_csv(file_path)
            train_df, test_df = train_test_split(df, train_size=self.train_ratio, random_state=42)
            train_df.to_csv(Train_File_Path, index=False)
            test_df.to_csv(Test_File_Path, index=False)
            logger.info(f"Data split into train and test sets at {Train_File_Path} and {Test_File_Path}")
        except Exception as e:
            logger.error(f"Error splitting data: {e}")
            raise CustomException("Error splitting data", sys) from e

    def initiate_data_ingestion(self):
        """Initiates the data ingestion process."""
        try:
            raw_data_path = self.download_data_from_gcs()
            self.split_data(raw_data_path)
            logger.info("Data ingestion process completed successfully.")
        except Exception as e:
            logger.error(f"Error in data ingestion process: {e}")
            raise CustomException("Error in data ingestion process", sys) from e
        
if __name__ == "__main__":
    config_path = "config/config.yaml"
    data_ingestion = DataIngestion(config_path)
    data_ingestion.initiate_data_ingestion()