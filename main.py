import sys
from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
from networksecurity.logging.logger import logging
from networksecurity.exception.exception import NetworkSecurityException

if __name__ == "__main__":
    try:
        trainingpipelineconfig=TrainingPipelineConfig()
        dataingestionconfig=DataIngestionConfig(trainingpipelineconfig)
        data_ingestion=DataIngestion(dataingestionconfig)
        logging.info("Initiate the data ingestion")
        dataingestionartifact=data_ingestion.initiate_data_ingestion()
        logging.info("Data Ingestion Completed")
        print(dataingestionartifact)
    except Exception as e:
        NetworkSecurityException(e, sys)