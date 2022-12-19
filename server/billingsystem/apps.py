from django.apps import AppConfig
import os
import tensorflow as tf
from django.conf import settings



class BillingsystemConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "billingsystem"

class ApiConfig(AppConfig):
    name = 'api'
    MODEL_FILE = os.path.join(settings.MODELS, "test")

    model = tf.keras.models.load_model(MODEL_FILE)

