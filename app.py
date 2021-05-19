from flask import Flask,render_template,url_for,request
import pandas as pd 
from werkzeug.utils import secure_filename
import timeit

import mediapipe as mp # Import mediapipe
import cv2 # Import opencv
import csv
import os
import numpy as np
import pandas as pd
import os.path
import pickle

from main import pose_detection

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = r'./upload/'



@app.route('/', methods=['GET', 'POST'])
def dash_board():
    if request.method == 'GET':
        return render_template("index.html")
    
    elif request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        age = request.form['age']
        weight = request.form['weight']
        height = request.form['height']
        feed_type = request.form['feed_type']

        if feed_type=='video_file':
            file = request.files['file_upload']
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print(feed_type)
            # Prediction
            pose_history = pose_detection.pose_detection(video_path=os.path.join(app.config['UPLOAD_FOLDER'], filename),
            train=False)
        else:
            print('Live Feed')
            start = timeit.default_timer()
            pose_history = pose_detection.pose_detection(video_path=0,
            train=False)
            stop = timeit.default_timer()

            total_time = stop - start
            total_time = round(total_time/60,1)
        return render_template('Dashboard.html',f_name=first_name,l_name=last_name,age_info=age,weight_info=weight,height_info=height, total_pose=len(set(pose_history[0])), total_time=total_time)


if __name__ == '__main__':
	app.run(debug=True)