from django.shortcuts import render
from django.http import JsonResponse
import base64
import tensorflow as tf
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.conf import settings 
from tensorflow.python.keras.backend import set_session
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.applications.imagenet_utils import decode_predictions
import matplotlib.pyplot as plt
import numpy as np
from tensorflow.keras.applications import mobilenet_v2
import datetime
import traceback
import pandas as pd
from .apps import ApiConfig

def index(request):
    if  request.method == "POST":
        f=request.FILES['sentFile'] 
        response = {}
        file_name = "pic.jpg"
        label_df = pd.read_csv("static/labels/labels.csv")
        temp_dict = label_df.to_dict()
        labels = temp_dict["0"]
        file_name_2 = default_storage.save(file_name, f)
        file_url = default_storage.url(file_name_2)
        urlstr = str(file_url)
        newurl = urlstr[1:]
        original = load_img(newurl, target_size=(224, 224))
        numpy_image = img_to_array(original)
        image_batch = np.expand_dims(numpy_image, axis=0)
        pred_img = mobilenet_v2.preprocess_input(image_batch.copy())
        model = ApiConfig.model
        #model = tf.keras.models.load_model('static/test')
        pred = model.predict(pred_img)
        pred = np.argmax(pred,axis=1)
        predicted_label = [labels[k] for k in pred]
        response['name'] = str(predicted_label[0])
        return render(request,'billingsystem/index.html',response)
    else:
        return render(request,'billingsystem/index.html')