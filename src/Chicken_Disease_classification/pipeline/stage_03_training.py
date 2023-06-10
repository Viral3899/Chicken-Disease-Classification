from Chicken_Disease_classification.config.configuration import ConfigurationManager
from Chicken_Disease_classification.components.prepare_callbacks import PrepareCallback
from Chicken_Disease_classification.components.training import Training
from Chicken_Disease_classification import logger
import os
import tensorflow as tf

 
STAGE_NAME_TRAINING= 'Training'

class ModelTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        try:
            config = ConfigurationManager()
            prepare_callbacks_config = config.get_prepare_callback_config()
            prepare_callbacks = PrepareCallback(config=prepare_callbacks_config)
            callback_list= prepare_callbacks.get_tb_ckpt_callbacks()
        
        
            training_config = config.get_training_config()
            training = Training(config=training_config)
            training.get_base_model()
            training.train_valid_generator()
            
            # Check if checkpoint model exists
            checkpoint_filepath = prepare_callbacks_config.checkpoint_model_filepath
            if os.path.exists(checkpoint_filepath):
                training.model = tf.keras.models.load_model(checkpoint_filepath)
            
            training.train(callback_list=callback_list)
        except Exception as e:
            raise e
        
if __name__ == '__main__':
    try:
        logger.info(f'\n\n{"**"*50}\nStarted {STAGE_NAME_TRAINING}\n{"**"*50}\n')
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f'\n\n{"**"*50}\nCompleted {STAGE_NAME_TRAINING}\n{"**"*50}\n\n')
        
    except Exception as e:
        logger.exception(e)
        raise e