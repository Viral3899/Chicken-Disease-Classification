from Chicken_Disease_classification import logger
from Chicken_Disease_classification.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from Chicken_Disease_classification.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from Chicken_Disease_classification.pipeline.stage_03_prepare_callbacks import PrepareCallbackTrainingPipeline


STAGE_NAME_INGESTION = 'Data Ingestion Stage'

try:
    logger.info(f'\n\n{"**"*50}\nStarted {STAGE_NAME_INGESTION}\n{"**"*50}\n')
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f'\n\n{"**"*50}\nCompleted {STAGE_NAME_INGESTION}\n{"**"*50}\n\n')
    
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME_PREPARE_BASE_MODEL = 'Prepare Base Model'

try:
    logger.info(f'\n\n{"**"*50}\nStarted {STAGE_NAME_PREPARE_BASE_MODEL}\n{"**"*50}\n')
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f'\n\n{"**"*50}\nCompleted {STAGE_NAME_PREPARE_BASE_MODEL}\n{"**"*50}\n\n')
    
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME_PREPARE_CALLBACKS= 'Prepare callbacks'

try:
    logger.info(f'\n\n{"**"*50}\nStarted {STAGE_NAME_PREPARE_CALLBACKS}\n{"**"*50}\n')
    obj = PrepareCallbackTrainingPipeline()
    obj.main()
    logger.info(f'\n\n{"**"*50}\nCompleted {STAGE_NAME_PREPARE_CALLBACKS}\n{"**"*50}\n\n')
    
except Exception as e:
    logger.exception(e)
    raise e