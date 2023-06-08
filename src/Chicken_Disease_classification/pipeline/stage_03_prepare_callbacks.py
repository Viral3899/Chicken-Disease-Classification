from Chicken_Disease_classification.components.prepare_callbacks import PrepareCallback
from Chicken_Disease_classification.config.configuration import ConfigurationManager
from Chicken_Disease_classification import logger
 
 
STAGE_NAME_PREPARE_CALLBACKS= 'Prepare callbacks'

class PrepareCallbackTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        try:
            config = ConfigurationManager()
            prepare_callbacks_config = config.get_prepare_callback_config()
            prepare_callbacks = PrepareCallback(config=prepare_callbacks_config)
            prepare_callbacks.get_tb_ckpt_callback()
        except Exception as e:
            raise e
        
        
if __name__ == '__main__':
    
    try:
        logger.info(f'\n\n{"**"*50}\nStarted {STAGE_NAME_PREPARE_CALLBACKS}\n{"**"*50}\n')
        obj = PrepareCallbackTrainingPipeline()
        obj.main()
        logger.info(f'\n\n{"**"*50}\nCompleted {STAGE_NAME_PREPARE_CALLBACKS}\n{"**"*50}\n\n')
        
    except Exception as e:
        logger.exception(e)
        raise e
    
    
    