<h1 align="center"> <strong>Yoga Pose Detection</strong> </h1>


<img src="https://images.pexels.com/photos/6787408/pexels-photo-6787408.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940" alt="Italian Trulli" width="1000" height="550" style="display: block;
  margin-left: auto;
  margin-right: auto;
  width: 50%;">

> <p> <strong> "Yoga is the journey of the self, through the self, to the self." -- The Bhagavad Gita </strong> </p>

---

## **Table of Contents**
You're sections headers will be used to reference location of destination.

- [Description](#description)
- [How To Use](#how-to-use)
- [Repo Artitecture](#repo-artitecture)
- [Next Step](#next-step)
- [License](#license)
- [Author Info](#author-info)

---

## **Description**

<p align="justify">
Online Yoga coatching job is becoming challenging for the coaches because it's hard for them to keep track of the progress of each one of the participants. They would like to evaluate if the people are doing correctly the poses and provide custom-made training plans but it's hard to do when hundreds are joining the same class.
</p>
<p align="justify">
Project Goal is to to build an application able to track the poses done by the yoga practitioner, measure time, repetitions and evaluate if the poses are done correctly.
The MVP is where the customers receive a report of the yoga poses, which ones were done correctly, and metrics related to time and repetition.
</p>

<p align="justify">
We are using the MediaPipe one of the cutting edge tech to detect the body position and as for classification its RandomForest, an Machine Learning model which help produce a great result.
We came up with many conclusions, as we also tired to attemt many different models to completed the project. Inluding CNN model, and Neural Network model which is stated to be very advance and perfered Neural Network AI model for most of the digital visual analysis.
</p>

<br/>

## **Technologies**
<br/>

| Library       | Used to                                        |
| ------------- | :----------------------------------------------|
| Flask         | to scale up to complex applications.           |
| gunicorn      | a Python WSGI HTTP Server for UNIX.            |
| itsdangerous  | to ensure that a token has not been tampered.  |
| Jinja2        | a combination of Django templates and python.  |
| MarkupSafe    | to mitigates injection attacks                 |
| Werkzeug      | to build all sorts of end user applications    |
| numpy         | to scientific uses                             |
| scipy         | for fast N-dimensional array manipulation      |
| scikit-learn  | for machine learning built on top of SciPy     |
| matplotlib    | for creating visualizations                    |
| pandas        | to work with data structure and manupulate it  |
| mediapipe	| to with different body position 		 |


[**↥ Back To The Top**](#table-of-contents)

---

## **How To Use**

### **Installation** 

`Python Ver. '3.8'`

**Note:** Just use command below to install the required libary with correct version to run the program smoothly.

`pip install -r requiement.txt`


1. After the required libary install basic application can be run by just running `app.py` python script.

2. **(optional: <u>seprate training set</u>)** Download import file and move it to `\yoga_gesture_detection\pose_recognition_data\training data\training frames\videos`
3. **(optional: <u>generate different model</u>)** Inside `_Project_Analysis` directory run `body_pose_detection.ipynb`
	* Frame to video
	* Train model seprately
	* genereate different models for personal testing
4. Run the `app.py` file to host the application locally.


[**↥ Back To The Top**](#table-of-contents)

---

## **Repo Artitecture**
```
Yoga_Pose_Detection
│
│   README.md               :explains the project
│   requirements.txt        :packages to install to run the program
│   .gitignore              :specifies which files to ignore when pushing to the repository
│__   
│   _Project_Analysis       :directory contain all analysis done while doing this project.
│   │
│   │ body_pose_detection.ipynb     :frame-to-video geting coordinates. Classifing Body pose
│   │ Classification.ipynb  :analysing the best ML model to go with for classification
│   │ counting.py           :Performing the repitaiton and time counts.
│__   
│   data          		    :directory the main video/image fetures files.
│   │
│   │ coords.csv	        :csv file containg every classification coordinates in image/videos.
│__   
│   main          		    :directory the main video/image fetures files.
│   │
│   │ pose_detection.py     :main script file to detect the pose and classify it accordingly.
│__   
│   saved_model    		    :directory the saved training model of the classification.
│   │
│   │ body_language.pkl     :pickel/saved file of the trained model.
│__   
│   templates               :directory contain all the main html that work as a dashboard.
│   │
│   │ Dashboard.html        :dashboard for user to view the results.
│   │ index.html            :home page for website, provide the general informations.
│__   
│   upload          		:directory contains all the video file up^loaded by the user for analysis.
|
│	 app.py                 :python script file to deploy model and html files for web application.
```

[**↥ Back To The Top**](#table-of-contents)

---

## **Result Preview**

<img src="./Preview_images/index_page.PNG" alt="intial page" width="400" height="280"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<img src="./Preview_images/yoga_pose_analysis.PNG" alt="pose detection" width="400" height="230"> <br/><br/>
<img src="./Preview_images/dashboard.PNG" alt="dashboard result" width="400" height="200">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


[**↥ Back To The Top**](#table-of-contents)

---

## **Next Step**

- Web Dashboard for CV recent analysis.
- Improve Overall alaysis DAshboard.
- Use of Neural Network.
- Improve Accuracy, Object detection.
- Improvement of angle detection.

[**↥ Back To The Top**](#table-of-contents)

---
## **License**

Copyright (c) [2021] [Sijal Kumar Joshi, Simon Snyders, Vincent Rolin]

<p align="justify">
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
</p>
<p align="justify">
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
</p>
<p align="justify">
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
</p>

[**↥ Back To The Top**](#table-of-contents)

---

## **Author Info**

- Linkedin - [Sijal Kumar Joshi](https://www.linkedin.com/in/sijal-kumar-joshi-b1545584/), [Simon Snyders](https://www.linkedin.com/in/simon-snyders-9452aa146/), [Vincent Rolin](https://www.linkedin.com/in/vincent-rolin-/)
- Github   - [Sijal Kumar Joshi](https://github.com/sijal001), [Simon Snyders](https://github.com/simonsny), [Vincent Rolin](https://github.com/RolyVy)

[**↥ Back To The Top**](#table-of-contents)
