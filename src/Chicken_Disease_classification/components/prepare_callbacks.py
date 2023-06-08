import os
import urllib.request as request
from zipfile import ZipFile
import tensorflow as tf
import time
from Chicken_Disease_classification.config.configuration import PrepareCallbacksConfig



class PrepareCallback:
    def __init__(self,config:PrepareCallbacksConfig):
        self.config = config
        
    @property
    def _create_tb_callback(self):
        timestamp = time.strftime("%Y-%m-%dT%H:%M:%S")
        
        tb_running_lo_dir = os.path.join(self.config.tensorboard_root_log_dir,f"tb_logs_at_{timestamp}")
        return tf.keras.callbacks.TensorBoard(log_dir=tb_running_lo_dir)
    
    @property
    def _create_ckpt_callback(self):
        return tf.keras.callbacks.ModelCheckpoint(
            filepath=self.config.checkpoint_model_filepath,
            save_best_only=True
        )
    
    def get_tb_ckpt_callback(self):
        
        return [
            self._create_tb_callback,
            self._create_ckpt_callback
        ]