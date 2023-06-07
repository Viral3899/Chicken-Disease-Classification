import os
import urllib.request as request
import zipfile
from Chicken_Disease_classification import  logger
from Chicken_Disease_classification.utils.common import get_file_size
from Chicken_Disease_classification.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config = config
    
    def download_file(self):
        try:
            if not os.path.exists(self.config.local_data_file):
                filename, headers = request.urlretrieve(
                    url=self.config.source_URL,
                    filename=self.config.local_data_file
                )
                logger.info(f"{filename} downloaded to the following info:\n{headers}")
            else:
                print(self.config.local_data_file)
                logger.info(f"{self.config.local_data_file} already exists with size of {get_file_size(path=self.config.local_data_file)}")
        except Exception as e:
            logger.error(f"An error occurred while downloading the file: {e}")
            
    def extract_zip_file(self):
        try:
            unzip_path = self.config.unzip_dir
            os.makedirs(unzip_path, exist_ok=True)
            print(self.config.local_data_file)
            with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
                zip_ref.extractall(unzip_path)
        except Exception as e:
            logger.error(f"An error occurred while extracting the zip file: {e}")