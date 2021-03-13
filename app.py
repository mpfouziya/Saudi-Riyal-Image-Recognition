from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
import os
import cv2
from datetime import datetime


app=Flask(__name__,template_folder='template')
UPLOAD_FOLDER="static/frontend/uploads/"

@app.route('/')
def index():
    currency_dict={
            'SAR 1':0,
            'SAR 5':0,
            'SAR 10':0,
            'SAR 20':0,
            'SAR 50':0,
            'SAR 100':0,
            'SAR 200':0,
            'SAR 500':0
        }
    return render_template('index.html',prediction=currency_dict,image_url="../static/frontend/images/placeholder.jpg")

@app.route('/submit', methods=['POST'])  
def upload():
    pic=request.files['file']
    if not pic:
        return render_template('index.html', prediction=currency_dict,image_url="../static/frontend/images/placeholder.jpg")
    else:
        pic.filename = datetime.now().strftime("%M_%S_%p")
        image_location=os.path.join(
            UPLOAD_FOLDER,
            pic.filename,

        )    
        pic.save(image_location)
        img_array=cv2.imread(image_location)
        resized_img = cv2.resize(img_array,(224,224))
        X = np.array(resized_img)
        final_image=resized_img.reshape(-1,224,224,3)
        loaded_model = tf.keras.models.load_model('cnnModel.h5')
        prediction=loaded_model.predict(final_image)
        probabilities = loaded_model.predict_proba(final_image)
        currency_dict={
            'SAR 1':round(probabilities[0][0]*100,2),
            'SAR 5':round(probabilities[0][1]*100,2),
            'SAR 10':round(probabilities[0][2]*100,2),
            'SAR 20':round(probabilities[0][3]*100,2),
            'SAR 50':round(probabilities[0][4]*100,2),
            'SAR 100':round(probabilities[0][5]*100,2),
            'SAR 200':round(probabilities[0][6]*100,2),
            'SAR 500':round(probabilities[0][7]*100,2)
        }
        return render_template('index.html', prediction=currency_dict,image_url=image_location)

if __name__=='__main__':
    app.run(debug=True)