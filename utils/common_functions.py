import yaml
import sys
from src.custom_exception import CustomException
from src.logger import logging
import pandas as pd

def read_yaml(file_path):
    try:
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    except Exception as e:
        raise CustomException(f"Error reading yaml file at {file_path}: {e}", sys)

def load_data(path):
    try:
        logging.info(f"Loading data from {path}")
        return pd.read_csv(path)
    except Exception as e:
        logging.error(f"Error loading data from {path}: {e}", sys)
        raise CustomException(f"Error loading data from {path}: {e}", sys)
    