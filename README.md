# Saudi-Riyal-Image-Recognition


## Demo
<p align="center">
<img width="500" alt="postgreSQL" src="https://user-images.githubusercontent.com/37532698/111037245-bb499d00-843c-11eb-9447-41687bacd105.jpg"></p>

## Overview
This is a simple image classification Flask app trained on the top of Keras API. The trained CNN model (`cnnModel.h5`) takes an image (Saudi Arabian Riyal) as an input and predict the class of image from __1, 5, 10, 20, 50, 100, 200, 500__ denomination.

## Motivation
 The idea of classifying currency image struck to me when I was browsing through some research papers. I couldn't find any relevant research paper (and of course dataset!) associated with it. And that led me to collect the images of Saudi Arabian Riyal to train a deep learning model using [bing-image-downloader](https://pypi.org/project/bing-image-downloader/) amazing tool.

## Technical Aspect
This project is divided into three part:
1. Data collection and preprocessing.
2. Training a deep learning model using Keras.
3. Building a Flask web app.
    - A user can upload image from the system.
    - After uploading the image, the predictions are displayed on a __Bar Chart__.

## Installation
The Code is written in Python 3.9.1. If you don't have Python installed you can find it [here](https://www.python.org/downloads/). If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip. To install the required packages and libraries, run this command in the project directory after [cloning](https://www.howtogeek.com/451360/how-to-clone-a-github-repository/) the repository:
```bash
pip install -r requirements.txt
```

## Technologies Used

![](https://forthebadge.com/images/badges/made-with-python.svg)

[<img target="_blank" src="https://keras.io/img/logo.png" width=200>](https://keras.io/) [<img target="_blank" src="https://flask.palletsprojects.com/en/1.1.x/_images/flask-logo.png" width=170>](https://flask.palletsprojects.com/en/1.1.x/) 
