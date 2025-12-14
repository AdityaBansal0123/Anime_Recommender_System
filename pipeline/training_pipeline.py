from src.data_ingestion import DataIngestion
from src.data_processing import DataProcessor
from config.paths_config import *
from utils.common_functions import read_yaml
from src.model_training import ModelTraining

if __name__=="__main__":
    # data_ingestion = DataIngestion(read_yaml(CONFIG_PATH))
    # data_ingestion.run()

    data_processor = DataProcessor(ANIMELIST_CSV,PROCESSED_DIR)
    data_processor.run()
        
    model_trainer = ModelTraining(data_path=PROCESSED_DIR)
    model_trainer.train_model()