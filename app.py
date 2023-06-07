from Chicken_Disease_classification import logger
from Chicken_Disease_classification.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline


STAGE_NAME_INGESTION = 'Data Ingestion Stage'

try:
    logger.info(f'\n\n{"**"*50}\nStarted {STAGE_NAME_INGESTION}\n{"**"*50}\n')
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f'\n\n{"**"*50}\nCompleted {STAGE_NAME_INGESTION}\n{"**"*50}\n\n')
    
except Exception as e:
    logger.exception(e)
    raise e