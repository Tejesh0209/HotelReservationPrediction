import os
import pandas
from src.logger import get_logger
from src.custom_exception import CustomException
import yaml
import sys

logger = get_logger(__name__)

def read_yaml_file(file_path: str) -> dict:
    """
    Reads a YAML file and returns its contents as a dictionary.
    
    Args:
        file_path (str): The path to the YAML file.
    Returns:
        dict: The contents of the YAML file.
    """
    try:
        with open(file_path, 'r') as file:
            content = yaml.safe_load(file)
        logger.info(f"YAML file {file_path} read successfully.")
        return content
    except Exception as e:
        logger.error(f"Error reading YAML file {file_path}: {e}")
        raise CustomException(f"Error reading YAML file {file_path}", sys) from e
    

def load_data(file_path: str) -> pandas.DataFrame:
    """
    Loads data from a CSV file into a pandas DataFrame.
    
    Args:
        file_path (str): The path to the CSV file.
    Returns:
        pandas.DataFrame: The loaded data.
    """
    try:
        data = pandas.read_csv(file_path)
        logger.info(f"Data loaded successfully from {file_path}.")
        return data
    except Exception as e:
        logger.error(f"Error loading data from {file_path}: {e}")
        raise CustomException(f"Error loading data from {file_path}", sys) from e
    